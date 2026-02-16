import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def speech_to_text(audio_binary):
    base_url = os.getenv("WATSON_STT_URL")
    api_key = os.getenv("WATSON_STT_API_KEY")
    
    # Safety check: bypass if keys are placeholders or missing
    if not api_key or "your_" in api_key or "pending" in api_key:
        print("IBM STT not configured - skipping.")
        return None

    try:
        api_url = f"{base_url}/v1/recognize"
        params = {'model': 'en-US_Multimedia'}

        response = requests.post(
            api_url, 
            params=params, 
            data=audio_binary, 
            auth=('apikey', api_key),
            timeout=5
        ).json()

        if 'results' in response and len(response['results']) > 0:
            text = response['results'][0]['alternatives'][0]['transcript']
            print('Recognized text:', text)
            return text
    except Exception as e:
        print(f"STT Error: {e}")
    return None

def openai_process_message(user_message):
    prompt = "Act like a personal assistant. Keep responses concise - 2 to 3 sentences maximum."
    
    try:
        openai_response = openai_client.chat.completions.create(
            model="gpt-5-nano", 
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_message}
            ],
            max_completion_tokens=1000
        )
        return openai_response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return "Sorry, I'm having trouble connecting to my brain right now."

def text_to_speech(text, voice=""):
    base_url = os.getenv("WATSON_TTS_URL")
    api_key = os.getenv("WATSON_TTS_API_KEY")

    # Safety check: bypass if keys are placeholders or missing
    if not api_key or "your_" in api_key or "pending" in api_key:
        print("IBM TTS not configured - skipping voice synthesis.")
        return None

    try:
        api_url = f"{base_url}/v1/synthesize"
        if voice and voice != "default":
            api_url += f"?voice={voice}"

        headers = {
            'Accept': 'audio/wav',
            'Content-Type': 'application/json',
        }
        json_data = {'text': text}

        response = requests.post(
            api_url, 
            headers=headers, 
            json=json_data, 
            auth=('apikey', api_key),
            timeout=5
        )
        return response.content
    except Exception as e:
        print(f"TTS Error: {e}")
        return None
