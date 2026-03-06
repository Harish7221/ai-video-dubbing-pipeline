from modules.extract_clip import extract_clip
from modules.extract_audio import extract_audio
from modules.transcribe import transcribe
from modules.translate import translate
from modules.generate_voice import generate_voice
from modules.merge_audio_video import merge_audio_video
from modules.audio_segment import split_audio

from pydub import AudioSegment
import os


input_video = "input/video.mp4"
clip_video = "outputs/clip.mp4"
audio_file = "outputs/audio.wav"
hindi_audio = "outputs/hindi_audio.wav"
dubbed_video = "outputs/dubbed_video.mp4"


# Step 1: Clip video
extract_clip(input_video, clip_video)
print("Video clip created")

# Step 2: Extract audio
extract_audio(clip_video, audio_file)
print("Audio extracted")


# Step 3: Split audio into speech segments (handles long audio)
segments = split_audio(audio_file)

print(f"\nAudio split into {len(segments)} segments")


hindi_audio_segments = []


# Step 4: Process each segment
for i, seg in enumerate(segments):

    print(f"\nProcessing Segment {i+1}")

    # Transcribe
    text = transcribe(seg)

    print("Kannada Transcription:")
    print(text)

    # Translate
    hindi = translate(text)

    print("Hindi Translation:")
    print(hindi)

    # Generate Hindi voice
    seg_hindi_audio = seg.replace(".wav", "_hi.wav")

    generate_voice(hindi, seg, seg_hindi_audio)

    hindi_audio_segments.append(seg_hindi_audio)


# Step 5: Merge Hindi audio segments
combined = AudioSegment.empty()

for seg in hindi_audio_segments:
    combined += AudioSegment.from_wav(seg)

combined.export(hindi_audio, format="wav")

print("\nHindi voice generated and merged")


# Step 6: Merge Hindi audio with video
merge_audio_video(clip_video, hindi_audio, dubbed_video)

print("\nHindi Dubbed Video Created!")