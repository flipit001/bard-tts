from Bard import Chatbot
def secret_token(tokenfile):
    with open(tokenfile, "r") as fh:  
        return fh.read().replace("\n", "") 
class Conversation:
    def __init__(self, token):
        self.token = token
        self.chatbot = Chatbot(token)
    def start(self, question):
        return self.chatbot.ask(question)["content"]

