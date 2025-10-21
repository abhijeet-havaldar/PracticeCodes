import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak out the given text."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for a voice command and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Fixed typo
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please say it again.")
        return ""
    except sr.RequestError:
        speak("Sorry, I am having trouble connecting to the speech service.")
        return ""
    
    return query.lower()

# Greet the user
speak("Hello, I am your Python assistant. How can I help you?")

while True:
    command = take_command()

    if command == "":
        continue

    elif 'time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif 'open music' in command:
        speak("Opening your music folder")
        music_path = "C:\\Users\\Public\\Music"
        if os.path.exists(music_path):
            os.startfile(music_path)
        else:
            speak("Sorry, I couldn't find the music folder.")

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye! Have a nice day.")
        break

    else:
        speak("Sorry, I didn’t understand that command.")
