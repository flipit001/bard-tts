import pyttsx3 as tts
import speech_recognition as sr
from bardapi import Conversation, secret_token



class theengine:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.microphone = sr.Microphone()
        # initialize engine
        self.engine = tts.init()

        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.chat = Conversation(secret_token())

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


    def get_command(self):
        with self.microphone as source:
            print('listening...')
            user_input = self.listener.listen(source)                # get user input (voice)
            voice = self.listener.recognize_google(user_input)       # uses Google API
            voice = ' '+voice.lower()+' '                               # makes sure input string is lowercase
        print(voice)
        if " bard " in voice:
            voice = voice.replace(voice[0:voice.find(" bard ")])
            print(voice)
            self.talk("ok, I will now answer")
            response = self.chat.start(voice)
            print(response)
            self.talk(response)
        
        