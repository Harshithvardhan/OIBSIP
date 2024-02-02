import speech_recognition as sp
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyaudio

rec = sp.Recognizer()
eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[0].id)
def speaking(text):
    eng.say(text)
    eng.runAndWait()
def greetings():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speaking("Good morning! My Friend")

    elif 12 <= hour < 18:
        speaking("Good afternoon! My Friend")

    else:
        speaking("Good evening! My Friend")

    speaking("How can I Help you?")


def listening():
    with sp.Microphone() as source:
        print("Listening Your Command...")
        rec.pause_threshold = 1
        audio = rec.listen(source)

    try:
        print("Recognizing Your Command...")
        query = rec.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Sorry, I am unable to hear you. Can you please repeat once more?")
        return ""
    return query


def searching_web(q):
    speaking(f"Searching {q} for you my friend")
    link = "https://www.google.com/search?q=" + q
    webbrowser.open(link)


def executeing_command(order):
    if "hello"  in order or "Hi"  in order or "Good Morning"  in order or "Good Afternoon"  in order:
        speaking("Hello how are you doing!")
    elif 'wikipedia' in order or "meaning"  in order or "explain"  in order:
        speaking('Searching Wikipedia...')
        order = order.replace("wikipedia", "")
        req = wikipedia.summary(order, sentences=2)
        speaking("In wikipedia")
        print(req)
        speaking(req)    
    elif "search"  in order or "show" in order:
        searching_query = order.split("search")[-1].strip()
        searching_web(searching_query)
    elif 'open youtube'  in order or "youtube" in order:
        webbrowser.open("youtube.com")

    elif 'open google'  in order or "google" in order:
        webbrowser.open("google.com")

    elif 'play music' in order:
        if('spotify' in order):
            webbrowser.open("spotify.com")
        else:
            webbrowser.open('https://wynk.in/music')

    elif 'time' in order or "what are you doing" in order:
        t = datetime.datetime.now().strftime("%H:%M:%S")
        speaking(f"The time is {t}")

    elif 'date'  in order or "what is your birthday" in order:
        d = datetime.datetime.now().strftime("%D-%m-%Y")
        speaking(f"The date is {d}")

    elif 'exit'  in order or 'Goodbye!' in order  or 'bye' in order or 'thanks' in order or 'thank you' in order:
        speaking("Its a Pleasure ,Goodbye My friend!")
        exit()

    else:
        speaking("sorry, I can't get your command.")


if __name__ == "__main__":
    greetings()
    while True:
        listen= listening().lower()
        if listen:
            executeing_command(listen)