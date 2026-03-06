from pydub import AudioSegment
from pydub.silence import split_on_silence
import os


def split_audio(audio_path, output_dir="segments"):

    os.makedirs(output_dir, exist_ok=True)

    sound = AudioSegment.from_wav(audio_path)

    chunks = split_on_silence(
        sound,
        min_silence_len=700,
        silence_thresh=sound.dBFS - 14,
        keep_silence=300
    )

    segment_paths = []

    for i, chunk in enumerate(chunks):
        segment_file = f"{output_dir}/segment_{i}.wav"
        chunk.export(segment_file, format="wav")
        segment_paths.append(segment_file)

    return segment_paths