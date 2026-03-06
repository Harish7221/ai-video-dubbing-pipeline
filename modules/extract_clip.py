import subprocess

def extract_clip(input_video, output_video):

    command = [
        "ffmpeg",
        "-y",
        "-i", input_video,
        "-t", "15",
        "-c", "copy",
        output_video
    ]

    subprocess.run(command)