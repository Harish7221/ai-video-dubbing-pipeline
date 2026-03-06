import requests

API_KEY = "YOUR_SARVAM_API_KEY"

def transcribe(audio_file):

    url = "https://api.sarvam.ai/speech-to-text"


    headers = {
        "api-subscription-key": API_KEY
    }

    files = {
        "file": ("audio.wav", open(audio_file, "rb"), "audio/wav")
    }

    data = {
        "model": "saaras:v3",
        "language_code": "kn-IN",
        "enable_itn": True
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    result = response.json()

    print("\nSarvam API Response:")
    print(result)

    if "transcript" in result:
        return result["transcript"]
    else:
        raise Exception("Transcription failed: " + str(result))