from Bard import Chatbot
from bardapi import Conversation, secret_token
from talking import theengine

chat = theengine()

while True:
    chat.get_command()

