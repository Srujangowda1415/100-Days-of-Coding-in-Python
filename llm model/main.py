import os
import sounddevice as sd
import wave
from groq import Groq
from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import numpy as np
import datetime
import requests
import time

# Recording settings
FILENAME = os.path.dirname(__file__) + "/audio.wav"
DURATION = 5  # Record for 5 seconds
SAMPLERATE = 44100

def record_audio():
    print("Recording...")
    audio_data = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype='int16')
    sd.wait()
    print("Recording finished.")
    
    with wave.open(FILENAME, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLERATE)
        wf.writeframes(audio_data.tobytes())

def transcribe_audio():
    client = Groq(api_key="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")
    
    with open(FILENAME, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(FILENAME, file.read()),
            model="whisper-large-v3-turbo",
            response_format="verbose_json",
        )
        prompt = transcription.text
        print("Transcription:", prompt)
        return prompt

def get_current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y %I:%M %p")

def get_weather(location):
    api_key = "your_weather_api_key_here"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in {location} is {weather_description} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't fetch the weather information."

if __name__ == "__main__":
    record_audio()
    user_input = transcribe_audio()
    
    if "time" in user_input.lower() or "date" in user_input.lower():
        assistant_response = get_current_datetime()
    elif "weather" in user_input.lower():
        location = user_input.split("in")[-1].strip()
        assistant_response = get_weather(location)
    else:
        client = Groq(api_key="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")
        completion = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.6,
            max_completion_tokens=4096,
            top_p=0.95,
            stream=True,
            stop=None,
        )
        assistant_response = ""
        print("Assistant:", end=" ")
        for chunk in completion:
            text_chunk = chunk.choices[0].delta.content or ""
            print(text_chunk, end="")
            assistant_response += text_chunk
        print()
    
    pipeline = KPipeline(lang_code='a')
    generator = pipeline(assistant_response, voice='af_heart', speed=1, split_pattern=None)
    full_audio = []
    
    for i, (gs, ps, audio) in enumerate(generator):
        print(i, gs, ps)
        full_audio.append(audio)
    
    final_audio = np.concatenate(full_audio)
    sf.write('full_output.wav', final_audio, 24000)
    
    # Wait for the file to be fully written before playing
    time.sleep(1)
    print("Playing generated audio...")
    os.system("start full_output.wav" if os.name == "nt" else "afplay full_output.wav" if os.name == "posix" else "aplay full_output.wav")