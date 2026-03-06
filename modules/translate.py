import requests

API_KEY = "YOUR_SARVAM_API_KEY"

def translate(text):

    url = "https://api.sarvam.ai/translate"

    headers = {
        "api-subscription-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mayura:v1",
        "input": text,
        "source_language_code": "kn-IN",
        "target_language_code": "hi-IN"
    }

    response = requests.post(url, headers=headers, json=payload)

    result = response.json()

    print("\nTranslation API Response:")
    print(result)

    if "translated_text" in result:
        return result["translated_text"]
    else:
        raise Exception("Translation failed: " + str(result))