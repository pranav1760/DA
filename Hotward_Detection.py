import os
import speech_recognition as sr



def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio, language='en-in')
            print(f"You said : {query}")

        except Exception as Error:
            return "none"

        return query.lower()
    
while True:
    
    wake_up = takecommand()

    if 'wake up' in wake_up:
        os.startfile('C:\\Jarvis_Project\\hydra.py')
        

    else:
        print("say again.....")    