import pyttsx3
import speech_recognition as sr

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voice', voices[0].id)  # Use 'voice' instead of 'voices'

def speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")  # This line should be indented properly
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio, language='en-in')
            print(f"You said : {query}")

        except Exception as Error:
            return "none"

        return query.lower()


def TaskExe():
    while True:
        query = takecommand().lower()  # Convert input to lowercase for consistent matching

        if 'hello' in query:
            speak("Hello Sir! I Am Hydra, Your Personal AI Assistant.")
            speak("How may I help you?")

        elif 'how are you' in query:
            speak("I am fine, thank you!")
            speak("What about you?")

        elif 'you need a break' in query:
            speak("Sure, sir. You can call me anytime. Have a great day.")
            break

        elif 'by' in query:
            speak("Okay, sir. Goodbye!")
            break










