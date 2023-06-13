def run(testing):    
    from Bard import Chatbot
    from bardapi import Conversation, secret_token
    from talking import theengine

    chat = theengine()


    chat.get_command(testing)

if __name__ == "__main__":
    run(testing=None)