import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def speech_to_text(audio_binary):
    # Get values from .env
    base_url = os.getenv("WATSON_STT_URL")
    api_key = os.getenv("WATSON_STT_API_KEY")
    
    if not base_url or not api_key:
        return "Error: IBM STT Credentials missing in .env"

    api_url = f"{base_url}/v1/recognize"
    params = {'model': 'en-US_Multimedia'}

    # Use 'auth' for IBM's standard authentication
    response = requests.post(
        api_url, 
        params=params, 
        data=audio_binary, 
        auth=('apikey', api_key)
    ).json()

    # FIX: Added [0] indexing for results and alternatives
    if 'results' in response and len(response['results']) > 0:
        text = response['results'][0]['alternatives'][0]['transcript']
        print('Recognized text:', text)
        return text
    return None

def openai_process_message(user_message):
    prompt = "Act like a personal assistant. Keep responses concise - 2 to 3 sentences maximum."
    
    openai_response = openai_client.chat.completions.create(
        model="gpt-5-nano", 
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_message}
        ],
        max_completion_tokens=1000
    )
    # FIX: Added [0] indexing for choices
    return openai_response.choices[0].message.content

def text_to_speech(text, voice=""):
    # Get values from .env
    base_url = os.getenv("WATSON_TTS_URL")
    api_key = os.getenv("WATSON_TTS_API_KEY")

    if not base_url or not api_key:
        print("Error: IBM TTS Credentials missing")
        return None

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
        auth=('apikey', api_key)
    )
    return response.content
