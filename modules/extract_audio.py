import subprocess

def extract_audio(video_path, audio_path):

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        "-af", "highpass=f=200, lowpass=f=3000",
        audio_path
    ]

    subprocess.run(command)