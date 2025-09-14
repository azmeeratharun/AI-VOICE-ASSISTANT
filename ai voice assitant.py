import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

# Initialize Text-to-Speech

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty("voices")
print("Voices available:")
for i, v in enumerate(voices):
    print(i, v.id)

engine.setProperty("voice", voices[0].id) 

engine.setProperty("rate", 170)    
engine.setProperty("volume", 1.0)  



if len(voices) > 0:
    engine.setProperty("voice", voices[0].id)  # male
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)  # female (if needed)

# Set speaking speed and volume
engine.setProperty("rate", 170)    
engine.setProperty("volume", 1.0)  


def speak(text):
    engine.stop()  
    print("Assistant:", text) 
    engine.say(text)
    engine.runAndWait()

# Speech Recognition
recognizer = sr.Recognizer()

def listen():
    """Listen through microphone and return recognized text"""
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""

# Assistant Functions
def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you?")


def run_assistant():
    greet()
    while True:
        command = listen()

        if not command:
            continue

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif "open youtube" in command or "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in command or "google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "play music" in command:
            music_dir = "C:\\Users\\Public\\Music"  # change if needed
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                speak(f"Playing {song}")
                os.startfile(os.path.join(music_dir, song))
            else:
                speak("No music files found")

        elif any(word in command for word in ["exit", "quit", "stop", "close"]):
            speak("Goodbye! Have a nice day.")
            break

        elif "weather" in command:
            speak("Please tell me the city name")
            city = listen()
            if city:
                speak(f"Showing weather in {city} on Google")
                webbrowser.open(f"https://www.google.com/search?q=weather+in+{city}")
            else:
                speak("City name not recognized")

        else:
            speak("I can search that for you")
            webbrowser.open(f"https://www.google.com/search?q={command}")


if __name__ == "__main__":
    run_assistant()