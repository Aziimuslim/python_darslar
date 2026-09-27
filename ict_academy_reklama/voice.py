"""O‘zbekcha diktor ovozini espeak-ng (uz) bilan yaratadi va har bir gapni
reklama.html dagi SPEECH vaqt oralig‘iga moslaydi.

Natijalar:
  audio/ovoz.wav        — 60 soniyalik ovoz treki (0:00 dan)
  audio/ovoz_env.js     — lab sinxroni uchun ovoz balandligi (30 fps)

Talab: espeak-ng (apt install espeak-ng), ffmpeg (FFMPEG muhit o‘zgaruvchisi), numpy.
Inglizcha atamalar o‘zbekcha talaffuzda yozilgan (ekrandagi matn o‘zgarmaydi).
"""
import os, re, subprocess, tempfile, wave, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FF = os.environ.get('FFMPEG', 'ffmpeg')
VOICE = os.environ.get('ESPEAK_VOICE', 'uz+m3')
SR = 44100; DUR = 60.0; FPS = 30

# Ekrandagi matn -> talaffuz (faqat ovoz uchun)
PRON = [
    ("ICT ACADEMY’dagi", "Ay-Si-Ti Akademidagi"),
    ("ICT ACADEMY", "Ay-Si-Ti Akademi"),
    ("AI & Data Science Engineering", "Ey-Ay end Deyta Sayens Enjiniring"),
    ("Data Science", "Deyta Sayens"),
    ("Machine Learning", "Mashin Lyorning"),
    ("Deep Learning", "Dip Lyorning"),
    ("Computer Vision", "Kompyuter Vijn"),
    ("Prompt Engineering", "Prompt Enjiniring"),
    ("Python Basic", "Payton Beysik"),
    ("Python", "Payton"),
    ("GitHub", "Git-Hab"),
    ("NLP", "En-El-Pi"),
    ("LLM", "El-El-Em"),
    ("AI", "Ey-Ay"),
]

def pron(text):
    for a, b in PRON:
        text = text.replace(a, b)
    return re.sub('[‘’ʻʼ`]', "'", text)

def speech_items():
    html = open(os.path.join(HERE, 'reklama.html'), encoding='utf-8').read()
    return [(float(a), float(b), t) for a, b, t in
            re.findall(r'\{a:([\d.]+),\s*b:([\d.]+),\s*text:"([^"]+)"\}', html)]

def synth(text, rate, path):
    subprocess.run(['espeak-ng', '-v', VOICE, '-s', str(rate), '-p', '42', '-g', '2', '-w', path, text], check=True)
    with wave.open(path) as w:
        sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), '<i2').astype(np.float32) / 32768
    # boshidagi/oxiridagi sukunatni kesish
    nz = np.where(np.abs(x) > 0.01)[0]
    x = x[nz[0]: nz[-1] + 1] if len(nz) else x
    return x, sr

def ffmpeg_filter(x, sr, filt):
    with tempfile.TemporaryDirectory() as d:
        i, o = os.path.join(d, 'i.wav'), os.path.join(d, 'o.wav')
        with wave.open(i, 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
            w.writeframes((np.clip(x, -1, 1) * 32767).astype('<i2').tobytes())
        subprocess.run([FF, '-loglevel', 'error', '-y', '-i', i, '-af', filt, '-ar', str(SR), '-ac', '1', o], check=True)
        with wave.open(o) as w:
            return np.frombuffer(w.readframes(w.getnframes()), '<i2').astype(np.float32) / 32768

track = np.zeros(int(SR * DUR), np.float32)
with tempfile.TemporaryDirectory() as tmp:
    for k, (a, b, text) in enumerate(speech_items()):
        slot = b - a; p = pron(text); tmpw = os.path.join(tmp, f'{k}.wav')
        rate = 175
        for _ in range(6):                      # tezlikni slotga moslash
            x, sr = synth(p, rate, tmpw)
            d = len(x) / sr
            if abs(d - slot) < 0.12: break
            rate = int(np.clip(rate * d / slot, 120, 260))
        tempo = np.clip(d / slot, 0.8, 1.25)   # qolgan farqni atempo bilan
        y = ffmpeg_filter(x, sr, f'atempo={tempo:.4f},highpass=f=90,equalizer=f=250:t=q:w=1:g=-3,'
                                 f'equalizer=f=3000:t=q:w=1.2:g=3,acompressor=threshold=0.1:ratio=3:attack=5:release=80')
        y = y[:int(slot * SR)]
        i = int(a * SR); track[i:i + len(y)] += y
        print(f'{k+1}. slot {slot:.2f}s  espeak -s {rate}  -> {len(y)/SR:.2f}s')

# engil xona effekti (qisqa reverb) va normalizatsiya
rev = np.zeros_like(track)
for dl, g in [(0.023, .18), (0.041, .12), (0.067, .08), (0.093, .05)]:
    n = int(dl * SR); rev[n:] += track[:-n] * g
track = track + rev
track = track / np.max(np.abs(track)) * 0.89
with wave.open(os.path.join(HERE, 'audio', 'ovoz.wav'), 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((track * 32767).astype('<i2').tobytes())

# lab sinxroni uchun kadr bo‘yicha ovoz balandligi (0..1)
hop = SR // FPS
env = np.array([np.sqrt(np.mean(track[i*hop:(i+1)*hop] ** 2)) for i in range(int(DUR * FPS))])
env = np.clip(env / (np.percentile(env[env > 0.01], 90) + 1e-9), 0, 1)
with open(os.path.join(HERE, 'audio', 'ovoz_env.js'), 'w') as f:
    f.write('window.VOICE_ENV=' + json.dumps([round(float(v), 3) for v in env]) + ';\n')
print('audio/ovoz.wav va audio/ovoz_env.js tayyor')
