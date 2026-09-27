"""ICT ACADEMY reklamasi uchun fon musiqasi (60 s, 120 BPM, futuristik elektron).
Ovozni bosib ketmasligi uchun past o‘rta chastotalar yumshatilgan. Faqat numpy kerak.
Natija: audio/fon_musiqa.wav"""
import numpy as np, wave, os
SR = 44100; DUR = 60.0; BPM = 120; BEAT = 60 / BPM
N = int(SR * DUR); t = np.arange(N) / SR
out = np.zeros((N, 2))
rng = np.random.default_rng(7)
def note(m): return 440 * 2 ** ((m - 69) / 12)
def env(n, a, r):
    e = np.ones(n); a = min(int(a * SR), n); r = min(int(r * SR), n - a)
    e[:a] = np.linspace(0, 1, a); e[n - r:] *= np.linspace(1, 0, r); return e
def lp(x, k):  # oddiy bir qutbli past chastota filtri
    y = np.empty_like(x); acc = 0.0
    for i in range(len(x)): acc += k * (x[i] - acc); y[i] = acc
    return y
def add(start, sig, pan=0.0, gain=1.0):
    i = int(start * SR); j = min(N, i + len(sig)); sig = sig[:j - i] * gain
    out[i:j, 0] += sig * (1 - pan) ; out[i:j, 1] += sig * (1 + pan)

# akkordlar: Am – F – C – G (har biri 2 takt = 4 s)
CH = [[57, 60, 64], [53, 57, 60], [48, 55, 60, 64], [55, 59, 62]]
bar = 4 * BEAT
# pad
for b in range(int(DUR / (2 * bar)) + 1):
    ch = CH[b % 4]; st = b * 2 * bar; n = int(2 * bar * SR); tt = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * note(m) * tt * (1 + d)) for m in ch for d in (-0.003, 0.003))
    s = s / (2 * len(ch)) * env(n, 0.8, 0.8)
    add(st, s, pan=-0.2, gain=0.20); add(st, s, pan=0.2, gain=0.20)
    # sub bas
    bb = np.sin(2 * np.pi * note(ch[0] - 24) * tt) * env(n, 0.05, 0.3)
    add(st, bb, gain=0.30)
# arpedjio (16-lik notalar), 6.4 s dan keyin
step = BEAT / 4
for k in range(int(DUR / step)):
    st = k * step
    if st < 6.4 or st > 57: continue
    ch = CH[int(st // (2 * bar)) % 4]; m = ch[k % len(ch)] + 12 * (1 + (k // 8) % 2)
    n = int(0.22 * SR); tt = np.arange(n) / SR
    s = np.sign(np.sin(2 * np.pi * note(m) * tt)) * 0.3 + np.sin(2 * np.pi * note(m) * tt)
    s = lp(s * np.exp(-tt * 14), 0.25)
    add(st, s, pan=0.35 * np.sin(k * 0.7), gain=0.07)
# kick va hi-hat (1.6 s dan keyin), yakunda to‘xtaydi
kn = int(0.35 * SR); kt = np.arange(kn) / SR
kick = np.sin(2 * np.pi * (45 + 110 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 9)
hn = int(0.06 * SR); hh = rng.standard_normal(hn) * np.exp(-np.arange(hn) / SR * 70)
hh = hh - lp(hh, 0.5)
for k in range(int(DUR / BEAT)):
    st = k * BEAT
    if 1.6 <= st < 58: add(st, kick, gain=0.55)
    if 6.4 <= st < 58: add(st + BEAT / 2, hh, pan=0.2, gain=0.10)
# sahna o‘tishlaridagi "whoosh"
for s0 in [6.4, 11.6, 20.6, 32.4, 40.4, 47.6]:
    n = int(0.8 * SR); tt = np.arange(n) / SR
    w = lp(rng.standard_normal(n), 0.08) * np.sin(np.pi * tt / 0.8) ** 2
    add(s0 - 0.45, w, gain=0.9)
# boshida riser, oxirida fade
out[:int(0.5 * SR)] *= np.linspace(0, 1, int(0.5 * SR))[:, None]
fo = int(2.0 * SR); out[-fo:] *= np.linspace(1, 0, fo)[:, None]
out = out / np.max(np.abs(out)) * 0.7
os.makedirs('audio', exist_ok=True)
with wave.open('audio/fon_musiqa.wav', 'wb') as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR)
    f.writeframes((out * 32767).astype('<i2').tobytes())
print('audio/fon_musiqa.wav tayyor')
