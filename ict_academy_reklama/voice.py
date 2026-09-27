"""O‘zbekcha diktor ovozini MBROLA (mb-tr1, erkak ovozi) + espeak-ng bilan yaratadi va har bir gapni
reklama.html dagi SPEECH vaqt oralig‘iga moslaydi.

Natijalar:
  audio/ovoz.wav        — 60 soniyalik ovoz treki (0:00 dan)
  audio/ovoz_env.js     — lab sinxroni uchun ovoz balandligi (30 fps)

Talab: espeak-ng, mbrola, mbrola-tr1 (apt install espeak-ng mbrola mbrola-tr1), ffmpeg (FFMPEG muhit o‘zgaruvchisi), numpy.
Inglizcha atamalar o‘zbekcha talaffuzda yozilgan (ekrandagi matn o‘zgarmaydi).
"""
import os, re, subprocess, tempfile, wave, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FF = os.environ.get('FFMPEG', 'ffmpeg')
VOICE = os.environ.get('ESPEAK_VOICE', 'mb-tr1')   # 'uz+m3' — eski formant ovoz
SR = 44100; DUR = 60.0; FPS = 30

# Ekrandagi matn -> talaffuz (faqat ovoz uchun)
PRON = [
    ("ICT ACADEMY’dagi", "Ay-Si-Ti Akademidagi"),
    ("ICT ACADEMY", "Ay-Si-Ti Akademi"),
    ("AI & Data Science Engineering", "Ey-Ay end Deyta Sayens Enjiniring"),
    ("Data Science", "Deyta Sayens"),
    ("Machine Learning", "Mashin Lyorning"),
    ("Deep Learning", "Dip Lyorning"),
    ("Computer Vision", "Kompyuter Viʒin"),
    ("Prompt Engineering", "Prompt Enjiniring"),
    ("Python Basic", "Payton Beysik"),
    ("Python", "Payton"),
    ("GitHub", "Git-Hab"),
    ("NLP", "En-El-Pi"),
    ("LLM", "El-El-Em"),
    ("AI", "Ey-Ay"),
]

# O‘zbek lotin yozuvi -> turk imlosi (MBROLA turkcha difonlari o‘zbekchaga yaqin)
TR = [("o'", "ö"), ("g'", "g"), ("sh", "ş"), ("ch", "ç"), ("j", "c"), ("q", "k"), ("x", "h"),
      ("yo", "yo"), ("lyo", "lö"), ("'", ""), ("ʒ", "j")]

def pron(text):
    for a, b in PRON:
        text = text.replace(a, b)
    text = re.sub('[‘’ʻʼ`]', "'", text).replace('-', ' ')
    if VOICE.startswith('mb-tr'):
        text = text.replace('I', 'ı').lower()
        for a, b in TR:
            text = text.replace(a, b)
    return text

def speech_items():
    html = open(os.path.join(HERE, 'reklama.html'), encoding='utf-8').read()
    return [(float(a), float(b), t) for a, b, t in
            re.findall(r'\{a:([\d.]+),\s*b:([\d.]+),\s*text:"([^"]+)"\}', html)]

def synth(text, rate, path):
    if VOICE.startswith('mb-'):
        # espeak-ng fonemalar -> MBROLA; bazada yo‘q difonlarni yaqin fonemaga almashtiramiz
        pho = subprocess.run(['espeak-ng', '-v', VOICE, '-q', '--pho', '-s', str(rate), '-p', '38', text],
                             check=True, capture_output=True, text=True).stdout
        fix = {'&': 'e', 'l/': 'l', 'L/': 'L'}
        pho = '\n'.join((fix.get(l.split('\t')[0], l.split('\t')[0]) + l[len(l.split('\t')[0]):]) if l else l
                        for l in pho.splitlines())
        db = f"/usr/share/mbrola/{VOICE[3:]}/{VOICE[3:]}"
        with open(path + '.pho', 'w') as f: f.write(pho + '\n')
        r = subprocess.run(['mbrola', '-e', db, path + '.pho', path], capture_output=True, text=True)
        if r.returncode or 'unknown' in r.stderr: raise RuntimeError(r.stderr)
    else:
        subprocess.run(['espeak-ng', '-v', VOICE, '-s', str(rate), '-p', '40', '-g', '0', '-w', path, text], check=True)
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
            rate = int(np.clip(rate * d / slot, 110, 240))
        tempo = np.clip(d / slot, 0.8, 1.25)   # qolgan farqni atempo bilan
        y = ffmpeg_filter(x, sr, f'aresample={SR}:resampler=soxr,atempo={tempo:.4f},highpass=f=70,'
                                 f'bass=g=4:f=140:w=0.8,equalizer=f=320:t=q:w=1.4:g=-2,'
                                 f'equalizer=f=2800:t=q:w=1.4:g=2.5,treble=g=-2:f=7500,'
                                 f'deesser=i=0.4,acompressor=threshold=0.08:ratio=3.5:attack=8:release=120:makeup=2,'
                                 f'afade=t=in:d=0.03')
        y = y[:int(slot * SR)]
        fo = int(0.06 * SR); y[-fo:] *= np.linspace(1, 0, fo)
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
