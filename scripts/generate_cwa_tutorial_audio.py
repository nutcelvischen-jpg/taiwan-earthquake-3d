#!/usr/bin/env python3
"""Generate TTS voiceover for CWA Earthquake Tutorial Video using OpenRouter Gemini 3.8 Flash TTS."""

import os
import sys
import subprocess
import requests

VOICE_DIR = "earthquake_data/voice_tutorial"
os.makedirs(VOICE_DIR, exist_ok=True)
FFMPEG = os.environ.get("FFMPEG_PATH", "ffmpeg")

API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
if not API_KEY and os.path.exists("OPR-KEY.txt"):
    with open("OPR-KEY.txt", "r", encoding="utf-8") as f:
        API_KEY = f.readline().strip().split()[0]

lines = [
    {
        "id": "line_01",
        "text": "想要一次抓下臺灣所有的歷史地震資料嗎？帶你看氣象署開放平臺該怎麼找與怎麼下載！"
    },
    {
        "id": "line_02",
        "text": "第一步，來到氣象署開放資料平臺，登入後在會員專區點擊取得個人 API 授權碼。"
    },
    {
        "id": "line_03",
        "text": "第二步，進入 Swagger 說明文件，找到地震海嘯分類，有感地震 REST API 就在這裡，輸入授權碼就能直接測試呼叫。"
    },
    {
        "id": "line_04",
        "text": "如果要下載所有年份的完整歷史目錄，關鍵在這裡！資料集 E-A0073-002，收錄了一九九零年至今全量的地震觀測紀錄。"
    },
    {
        "id": "line_05",
        "text": "用 Python 搭配授權碼一鍵發送下載請求，解開 ZIP 即可獲得三十六個年度 XML，清洗匯出超過七萬筆完整地震紀錄！"
    }
]

def generate_voice(item):
    raw_pcm = os.path.join(VOICE_DIR, f"{item['id']}.raw")
    out_wav = os.path.join(VOICE_DIR, f"{item['id']}.wav")
    
    print(f"Generating TTS for {item['id']}...")
    resp = requests.post(
        url="https://openrouter.ai/api/v1/audio/speech",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "google/gemini-3.8-flash-tts",
            "input": item["text"],
            "voice": "Zephyr"
        },
        timeout=30
    )
    if resp.status_code != 200:
        print(f"Error {resp.status_code}: {resp.text}")
        return False
        
    with open(raw_pcm, "wb") as f:
        f.write(resp.content)
        
    # OpenRouter Gemini 3.8 Flash TTS returns raw PCM: 24kHz, 1ch, s16le
    cmd = [
        FFMPEG, "-y",
        "-f", "s16le",
        "-ar", "24000",
        "-ac", "1",
        "-i", raw_pcm,
        "-ar", "44100",
        "-ac", "2",
        out_wav
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # Get duration
    probe_cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", out_wav
    ]
    dur = float(subprocess.check_output(probe_cmd).decode().strip())
    print(f"Saved {out_wav} (Duration: {dur:.2f}s)")
    return dur

def main():
    durations = {}
    total_dur = 0
    for item in lines:
        dur = generate_voice(item)
        durations[item["id"]] = dur
        total_dur += dur
        
    print(f"\nTotal pure voice duration: {total_dur:.2f}s")
    
    # Timeline
    timeline = []
    curr = 0.8
    for item in lines:
        d = durations[item["id"]]
        timeline.append({
            "id": item["id"],
            "start": round(curr, 2),
            "duration": round(d, 2),
            "end": round(curr + d, 2),
            "text": item["text"]
        })
        curr += d + 1.2
        
    final_audio_duration = round(curr + 1.5, 2)
    print(f"Planned final audio length: {final_audio_duration}s")
    
    # Write timeline json
    with open("earthquake_data/voice_timeline.json", "w", encoding="utf-8") as f:
        import json
        json.dump({
            "total_duration": final_audio_duration,
            "timeline": timeline
        }, f, ensure_ascii=False, indent=2)
        
    # Build ffmpeg audio filter complex
    filter_inputs = []
    filter_delays = []
    for i, t in enumerate(timeline):
        wav_path = os.path.join(VOICE_DIR, f"{t['id']}.wav")
        filter_inputs.extend(["-i", wav_path])
        delay_ms = int(t["start"] * 1000)
        filter_delays.append(f"[{i}]adelay={delay_ms}|{delay_ms}[v{i}]")
        
    mix_args = "".join([f"[v{i}]" for i in range(len(timeline))]) + f"amix=inputs={len(timeline)}:dropout_transition=0:normalize=0[voice]"
    
    voice_track = os.path.join(VOICE_DIR, "combined_voice.wav")
    cmd = [FFMPEG, "-y"] + filter_inputs + [
        "-filter_complex", ";".join(filter_delays) + ";" + mix_args,
        "-map", "[voice]", "-ac", "2", "-ar", "44100", voice_track
    ]
    subprocess.run(cmd, check=True)
    print(f"Combined voice track saved to {voice_track}")
    
    # Mix with BGM music_focused_60s.wav
    bgm_path = "music_focused_60s.wav"
    master_wav = os.path.join(VOICE_DIR, "master_narration_with_bgm.wav")
    
    bgm_filter = f"[0:a]volume=1.4[voice];[1:a]atrim=0:{final_audio_duration},afade=t=out:st={final_audio_duration - 2}:d=2,volume=0.18[bgm];[voice][bgm]amix=inputs=2:duration=longest[out]"
    mix_cmd = [
        FFMPEG, "-y",
        "-i", voice_track,
        "-i", bgm_path,
        "-filter_complex", bgm_filter,
        "-map", "[out]",
        "-ac", "2", "-ar", "44100",
        master_wav
    ]
    subprocess.run(mix_cmd, check=True)
    print(f"Master soundtrack mixed with BGM: {master_wav}")

if __name__ == "__main__":
    main()
