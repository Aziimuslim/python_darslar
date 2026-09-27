#!/usr/bin/env bash
# Yozib olingan o‘zbekcha ovozni (audio/ovoz.wav yoki .mp3) videoga qo‘shadi.
# Musiqa ovoz paytida avtomatik pasayadi (sidechain ducking).
# Foydalanish: ./ovoz_qoshish.sh audio/ovoz.wav
set -euo pipefail
cd "$(dirname "$0")"
VOICE="${1:-audio/ovoz.wav}"
FF="${FFMPEG:-ffmpeg}"
"$FF" -y -i video/ict_academy_reklama.mp4 -i audio/fon_musiqa.wav -i "$VOICE" -filter_complex \
 "[2:a]aformat=channel_layouts=stereo,volume=1.6,asplit=2[v][sc];\
  [1:a]volume=0.55[m];[m][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[md];\
  [md][v]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart video/ict_academy_reklama_ovozli.mp4
echo "Tayyor: video/ict_academy_reklama_ovozli.mp4"
