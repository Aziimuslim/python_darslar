# ICT ACADEMY — AI & Data Science Engineering reklama videosi

Instagram Reels, Telegram, TikTok va YouTube Shorts uchun vertikal (9:16) reklama roligi.

| Parametr | Qiymat |
|---|---|
| Fayl | `video/ict_academy_reklama_ovozli.mp4` |
| O‘lcham | 1080 × 1920, 30 fps, H.264 |
| Davomiyligi | 60 soniya |
| Audio | O‘zbekcha ovoz + fon musiqasi (`_ovozli.mp4`), AAC 192 kbps |

## Nima tayyor

- **Animatsion boshlovchi**: 22–25 yoshli, to‘q ko‘k (navy) ko‘ylakda, cyan detallari bor
  fiktiv 2D IT mutaxassis. U butun video davomida bir xil ko‘rinishda, kameraga qaraydi,
  ko‘zini qisadi, boshini qimirlatadi, qo‘llari bilan ishora qiladi, holografik ekranlarni
  barmog‘i bilan “yoqadi” va 5-sahnada noutbukda ishlaydi.
- **Lab harakati**: o‘zbekcha matnning har bir so‘zi va harfiga qarab (a/o/e/i/u — ochiq,
  m/b/p — yopiq) sinxronlashtirilgan. Vaqtlar `audio/ovoz_ssenariy.srt` faylida.
- **7 ta sahna** ssenariy bo‘yicha: sarlavhalar, talablar ro‘yxati, 10 ta texnologiya,
  laptop ekrani (Python kodi → DataFrame → grafiklar → ML model → AI chatbot →
  Computer Vision → RAG tizimi), GitHub portfolio va sertifikat, yakuniy CTA.
- **Fon**: ko‘k neon nurlar, AI brain, neyron tarmoq, oqib turuvchi kod, data grafiklar,
  Python belgisi, database, ML elementlari, perspektiv pol to‘ri.
- **Subtitrlar**: gapirilayotgan so‘z karaoke uslubida yoritiladi.
- **Fon musiqasi**: futuristik elektron trek (120 BPM) va sahna o‘tishlarida “whoosh”
  effektlari (`music.py` orqali yaratilgan, shuning uchun mualliflik huquqi muammosi yo‘q).

CTA’dagi ma’lumotlar posterdagi bilan aynan bir xil:
`+998 (88) 333 88 09`, `+998 (20) 035 26 04`, `@ictacademy_official`, `ictacademy.uz/contact`.

## Ovoz

`video/ict_academy_reklama_ovozli.mp4` — **o‘zbekcha diktor ovozi + musiqa** bilan tayyor versiya.
`video/ict_academy_reklama.mp4` esa faqat musiqali versiya (boshqa ovoz qo‘yish uchun).

Ovoz `voice.py` orqali offline yaratilgan: **MBROLA `tr1` erkak ovozi** (yozib olingan nutq
bo‘laklaridan — difonlardan — yig‘iladi, shuning uchun formant sintezdan ancha silliqroq) + espeak-ng:
- o‘zbekcha matn turkcha imloga o‘giriladi (sh→ş, ch→ç, o‘→ö, q→k, x→h, j→c), chunki turkcha
  fonetika o‘zbekchaga juda yaqin; inglizcha atamalar o‘zbekcha talaffuzda (“Deyta Sayens”, “Ay-Si-Ti”);
- ovoz “to‘liqroq” bo‘lishi uchun: past chastota iliqligi (+4 dB, 140 Hz), aniqlik (2.8 kHz),
  de-esser, kompressor va yengil xona reverbi;
- har bir gap `audio/ovoz_ssenariy.srt` dagi vaqtga aniq moslangan (≈160 so‘z/daqiqa, bir tekis temp);
- lablar ovozning haqiqiy balandligiga ergashadi (`audio/ovoz_env.js`), pauzalarda og‘iz yopiladi;
- ovoz paytida musiqa avtomatik pasayadi (sidechain ducking).

Bu baribir sintetik ovoz. Eng yaxshi natija uchun jonli diktor yoki neyron TTS (ElevenLabs,
Edge TTS `uz-UZ-SardorNeural`) bilan qayta yozish mumkin:

```bash
# 1) audio/ovoz_ssenariy.srt bo‘yicha yozib oling -> audio/ovoz.wav (0:00 dan boshlanadi)
./ovoz_qoshish.sh audio/ovoz.wav      # -> video/ict_academy_reklama_ovozli.mp4
```

Yangi ovozga lablarni ham moslash uchun `audio/ovoz_env.js` ni qayta hisoblab (voice.py oxiridagi
qism), `node render.js` bilan videoni qayta render qiling.

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `reklama.html` | Butun animatsiya (brauzerda ochib ko‘rish mumkin: play/pause va vaqt slayderi bor) |
| `render.js` | HTML’ni kadrma-kadr MP4 ga render qiladi (Playwright + ffmpeg) |
| `music.py` | Fon musiqasini yaratadi → `audio/fon_musiqa.wav` |
| `voice.py` | MBROLA + espeak-ng bilan o‘zbekcha ovoz → `audio/ovoz.wav`, `audio/ovoz_env.js` |
| `ovoz_qoshish.sh` | Yozilgan ovozni musiqa bilan birga videoga qo‘shadi |
| `audio/ovoz_ssenariy.srt` | Diktor uchun vaqtlari ko‘rsatilgan ssenariy / subtitr |
| `fonts/` | Montserrat va JetBrains Mono shriftlari (lokal) |

## Qayta render qilish

```bash
npm i -g playwright          # yoki mahalliy o‘rnatish
python3 music.py             # musiqa (numpy kerak)
node render.js               # video/ict_academy_reklama_silent.mp4  (~3 daqiqa)
ffmpeg -i video/ict_academy_reklama_silent.mp4 -i audio/fon_musiqa.wav \
       -c:v copy -c:a aac -b:a 192k -shortest video/ict_academy_reklama.mp4
node render.js --snap 5,15,45   # faqat tanlangan soniyalardagi kadrlarni PNG qilib olish
```

## Sahnalar vaqti

| # | Vaqt | Sahna |
|---|---|---|
| 1 | 0:00–0:06.4 | Diqqatni tortish — AI & DATA SCIENCE ENGINEERING / ICT ACADEMY |
| 2 | 0:06.4–0:11.6 | QABUL BOSHLANDI! · 8 OY · AI + DATA SCIENCE |
| 3 | 0:11.6–0:20.6 | Boshlang‘ich talablar + Python kodi |
| 4 | 0:20.6–0:32.4 | 10 ta texnologiya birma-bir |
| 5 | 0:32.4–0:40.4 | Amaliyot: laptop, REAL PROJECTS … GITHUB PORTFOLIO |
| 6 | 0:40.4–0:47.6 | Natija: JUNIOR AI / DATA SCIENCE ENGINEER |
| 7 | 0:47.6–1:00 | Final CTA: kontaktlar |

Boshlovchi to‘liq to‘qima (fiktiv) personaj va hech qanday real shaxsga o‘xshatilmagan.
