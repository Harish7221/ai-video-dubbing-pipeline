import requests
import base64
import subprocess

API_KEY = "YOUR_SARVAM_API_KEY"

def generate_voice(text, reference_audio, output_audio):

    url = "https://api.sarvam.ai/text-to-speech"

    headers = {
        "api-subscription-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "model": "bulbul:v3",
        "text": text,
        "target_language_code": "hi-IN",
        "speaker": "priya"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception("TTS failed: " + response.text)

    data = response.json()

    print("Sarvam TTS Response:", data)

    # Correct field
    audio_base64 = data["audios"][0]

    audio_bytes = base64.b64decode(audio_base64)

    temp_audio = "outputs/temp_hindi.wav"

    with open(temp_audio, "wb") as f:
        f.write(audio_bytes)

    print("Hindi voice generated")

    # Convert audio for SadTalker compatibility
    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", temp_audio,
        "-ac", "1",
        "-ar", "16000",
        output_audio
    ])

    print("Final Hindi audio saved:", output_audio)