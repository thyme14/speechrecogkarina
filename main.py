import speech_recognition as sr
import pyautogui
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import mouseinfo

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 70)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'karina' in command:
                command = command.replace('karina', 'garena','')
                print(command)
    except:
        pass
    return command


def run_karina():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    
    elif 'who is your boss' in command:
        talk('miftah its my boss')
    elif ' are you there' in command:
        talk('yes bos')
    elif 'where are you' in command:
        talk('Im here for you boss')
    elif 'can you speak indonesian' in command:
        talk('yap saya bisa')
    elif 'siapa kiki' in command:
        talk('kiki adalah si botak suka main roblox')
    elif 'who are you' in command:
        talk('I am Karina, artificial intelligence, developed by Miftah')



    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('tolong berbahasa inggris')


while True:
    run_karina()
