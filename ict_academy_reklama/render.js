// ICT ACADEMY reklama — HTML animatsiyani 1080x1920, 30 fps MP4 ga render qiladi.
// Foydalanish:
//   node render.js                      -> video/ict_academy_reklama.mp4
//   node render.js --snap 3,9,15        -> faqat shu soniyalardagi kadrlar (PNG)
// Talab: playwright (Chromium) va ffmpeg (FFMPEG muhit o‘zgaruvchisi yoki PATH).
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const FPS = 30;
const FFMPEG = process.env.FFMPEG || 'ffmpeg';
const args = process.argv.slice(2);
const snapIdx = args.indexOf('--snap');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.join(__dirname, 'reklama.html') + '?render=1');
  await page.evaluate(() => document.fonts.ready);
  const dur = await page.evaluate(() => window.DUR);
  const stage = await page.$('#stage');

  if (snapIdx >= 0) {
    fs.mkdirSync(path.join(__dirname, 'kadrlar'), { recursive: true });
    for (const s of args[snapIdx + 1].split(',').map(Number)) {
      await page.evaluate(t => window.renderAt(t), s);
      await stage.screenshot({ path: path.join(__dirname, 'kadrlar', `kadr_${String(s).padStart(5, '0')}.png`) });
    }
    await browser.close();
    return;
  }

  fs.mkdirSync(path.join(__dirname, 'video'), { recursive: true });
  const out = path.join(__dirname, 'video', 'ict_academy_reklama_silent.mp4');
  const ff = spawn(FFMPEG, ['-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out],
    { stdio: ['pipe', 'ignore', 'inherit'] });
  const total = Math.round(dur * FPS);
  for (let f = 0; f < total; f++) {
    await page.evaluate(t => window.renderAt(t), f / FPS);
    const buf = await stage.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 150 === 0) console.log(`kadr ${f}/${total}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('Tayyor:', out);
})();
