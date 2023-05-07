import pyttsx3 as tts
import speech_recognition as sr
from bardapi import Conversation, secret_token
import json



class theengine:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.microphone = sr.Microphone()
        # initialize engine
        self.engine = tts.init()

        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.chat = Conversation(secret_token("token.txt"))
        self.engine.setProperty('rate', 210)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


    def get_command(self):
        try: 
            with self.microphone as source:
                print('listening...')
                user_input = self.listener.listen(source)                # get user input (voice)
                voice = self.listener.recognize_google(user_input, language="en")
                voice = json.dumps(voice, ensure_ascii=False).encode('utf8').decode("ascii")# uses Google API
                voice = voice.lower()                               # makes sure input string is lowercase

            if "bard" in voice:
                voice = voice.replace(voice[0:voice.find(" bard ")], "")
                print(voice)
                self.talk("ok, I will now answer")
                response = self.chat.start(voice)
                print(response)
                self.talk(response)
        except:
            self.talk("can you say that again, I could not understand you")
            print("can you say that again, I could not understand you")
            return self.get_command()
        
        