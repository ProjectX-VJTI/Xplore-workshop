from moviepy import VideoFileClip, AudioFileClip
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

video = VideoFileClip(str(SCRIPT_DIR / "hollow_purple_evolution.mp4"))
audio = AudioFileClip(str(SCRIPT_DIR / "hollow_purple_sfx.mp3")) # You'll need this file
final_video = video.with_audio(audio)
final_video.write_videofile(str(SCRIPT_DIR / "gojo_final_cut.mp4"))
