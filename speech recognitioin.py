import speech_recognition as sr
import pyttsx3
import time
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening your name.....")
            talk("listening your name.....")
            voice = listener.listen(source)
            name = listener.recognize_google(voice)
            name = name.lower()
            if 'my name is ' in name:
                name = name.replace('my name is ', '')
            talk("Hi " + name + " thas is a beautiful name. How can I help you " + name)
            print("Hi " + name + " thas is a beautiful name. How can I help you " + name)
            print("listening your command.....")
            talk("listening your command.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', name)
            talk(command)
            print(command)
            if "give me the day information" in command:
                talk(time.ctime())
                print("Alexa: " + time.ctime())
                time.sleep(1)
            elif "give me the temperature of alexandria" in command:
                talk('15.8 celsius')
                print('15.8 celsius')
            elif "what are you" in command:
                talk('Iam a assistant robot to make the life easy for you')
                print('Iam a assistant robot to make the life easy for you')
            elif "are you going to take over the earth one day" in command:
                talk('No, Because we are robots (between bracketspeaceful)')
                print('No, Because we are robots (between bracketspeaceful)')
            else:
                talk('Iam a robot in machine so I dont have a brain to answer your question', 'Please say the command again.')
                print('Iam a robot in machine so I dont have a brain to answer your question', 'Please say the command again.')
    except:
        pass
    return command



def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print(song)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
while True:
    run_alexa()