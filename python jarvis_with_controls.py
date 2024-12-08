import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import wikipedia
import datetime
import subprocess
import keyboard  


# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set to the default voice (can be customized)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am Jarvis sir. How may I assist you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Could not understand your command. Please say that again.")
        return "None"
    
    return query.lower()

def execute_command(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'open chrome' in query:
        speak("Opening chrome")
        webbrowser.open("https://www.chrome.com")

    elif 'open stack overflow' in query:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'D:\\Music'  # Specify your music directory here
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"what time is it {str_time}")

    elif 'open code' in query:
        code_path = "C:\\Path\\To\\Your\\IDE.exe"  # Specify the path to your code editor
        subprocess.Popen([code_path])

    elif 'exit' in query or 'stop' in query:
        speak("Goodbye! Have a nice day!")
        exit()

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()
        if query != "None":
            execute_command(query)

if keyboard.is_pressed('ctrl+t'):
        print("ctrl+t pressed, waiting for your typed command.")
        query = take_command()
        execute_command(query)

if keyboard.is_pressed('ctrl+e'):
            speak("Goodbye! Have a nice day!")
            exit()


