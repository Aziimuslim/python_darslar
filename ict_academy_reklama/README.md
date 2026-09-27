# ICT ACADEMY — AI & Data Science Engineering reklama videosi

Instagram Reels, Telegram, TikTok va YouTube Shorts uchun vertikal (9:16) reklama roligi.

| Parametr | Qiymat |
|---|---|
| Fayl | `video/ict_academy_reklama.mp4` |
| O‘lcham | 1080 × 1920, 30 fps, H.264 |
| Davomiyligi | 60 soniya |
| Audio | Fon musiqasi (AAC 192 kbps) |

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

## ⚠️ Ovoz haqida

Videoda hozircha **diktor ovozi yo‘q**, faqat musiqa va subtitrlar bor. Bu muhitda o‘zbekcha
neyron TTS xizmatlariga (Microsoft Edge TTS, HuggingFace MMS-TTS) tarmoq kirishi
bloklangan edi. Boshlovchining lablari esa ovoz qo‘yilishiga tayyor qilib animatsiya qilingan.

Ovozni qo‘shish uchun:

1. `audio/ovoz_ssenariy.srt` bo‘yicha matnni yozib oling. Har bir gap SRT’dagi vaqt
   oralig‘iga sig‘ishi kerak (energetik reklama tempi, taxminan 16–17 belgi/soniya). Buning uchun
   diktor, ElevenLabs yoki `uz-UZ-SardorNeural` / `uz-UZ-MadinaNeural` (Edge TTS) ishlatish mumkin.
2. Faylni `audio/ovoz.wav` qilib saqlang (0:00 dan boshlanadigan yagona trek).
3. Ishga tushiring:

   ```bash
   ./ovoz_qoshish.sh audio/ovoz.wav
   ```

   Natija `video/ict_academy_reklama_ovozli.mp4` bo‘ladi. Ovoz paytida musiqa avtomatik
   pasayadi (sidechain ducking), shuning uchun u diktorni bosib ketmaydi.

Agar yozilgan ovoz tempi boshqacha chiqsa, `reklama.html` ichidagi `SPEECH` massividagi
`a`/`b` vaqtlarini moslang va videoni qayta render qiling. Lablar va subtitrlar yangi
vaqtlarga avtomatik moslashadi.

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `reklama.html` | Butun animatsiya (brauzerda ochib ko‘rish mumkin: play/pause va vaqt slayderi bor) |
| `render.js` | HTML’ni kadrma-kadr MP4 ga render qiladi (Playwright + ffmpeg) |
| `music.py` | Fon musiqasini yaratadi → `audio/fon_musiqa.wav` |
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
