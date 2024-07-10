import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import datetime
from playsound import playsound
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voice', voices[1].id)  # Use 'voice' instead of 'voices'
Assistant.setProperty('rate',150)

def speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
    print("  ")
    Assistant.runAndWait()

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


def TaskExe():
    
    speak("Hello , I AM Hydra.")
    speak("How Can I Help You ???")


    

    def Music():
        speak("Tell me the name of the song!!")
        musicname = takecommand()

        if 'Jab Tak' in musicname:
            os.startfile('C:\Jarvis_Project\songs\Jab Tak')

        elif'animal'in  musicname:
            os.startfile('C:\Jarvis_Project\songs\Animal')

        else:
            pywhatkit.playonyt(musicname)

        speak("Your song has been started!!,Enjoy sir!!")  

    def Whatsapp():
        speak("Tell me the name of the person!!")
        name = takecommand()

        if 'rocky' in name:
            speak("Tell me the message!!")
            msg = takecommand()
            speak("Tell me the Time sir!")
            speak("Time in hour!!")
            hour = int(takecommand())
            speak("Time in minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+918483815032",msg,hour,min,20)
            speak("ok sir, sending Whatsapp message !")
                  
        elif 'Shubham' in name:
            speak("Tell me the message!!")
            msg = takecommand()
            speak("Tell me the Time sir!")
            speak("Time in hour!!")
            hour = int(takecommand())
            speak("Time in minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919309497820",msg,hour,min,20)
            speak("ok sir, sending Whatsapp message !")
                  
        else:
            speak("Tell me the phone number!")
            phone =int(takecommand())
            ph = '+91' + phone
            speak("Tell me the message!!")
            msg = takecommand()
            speak("Tell me the Time sir!")
            speak("Time in hour!!")
            hour = int(takecommand())
            speak("Time in minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            speak("ok sir, sending Whatsapp message !")          

    def openapps():
        speak("ok sir,wait a second!!")

        if 'vs code' in query:
            os.startfile("C:\\Users\\Prath\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            
        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'zoom' in query:
            os.startfile("C:\\Users\\Prath\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

        elif 'pycharm' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.4\\bin\\pycharm64.exe")

        elif 'word' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")    

        elif 'microsoft edge' in query:
            os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')    

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@18.4862337,74.0182495,15z?entry=ttu')
            
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/') 

        speak("Your Command Has Been Completed Sir!!!!!")   

    def Dict():
        speak("Activated Dictionary!!")
        speak("Tell me the problem!!")
        probl = takecommand()

        if 'meaning' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("hydra","")
            probl = probl.replace("of","")
            probl = probl.replace("meaning of","")
            result = Diction.meaning(probl)
            speak(f"The meaning for {probl} is {result}")
 

        elif 'synonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("hydra","")
            probl = probl.replace("of","")
            probl = probl.replace("synonym of","")
            result = Diction.synonym(probl)
            speak(f"The synonym for {probl} is {result}") 

        elif 'antonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("hydra","")
            probl = probl.replace("of","")
            probl = probl.replace("antonym of","")
            result = Diction.antonym(probl)
            speak(f"The antonym for {probl} is {result}")

        speak("Exited Dictionary!!")           


    def closeapps():
        speak("ok sir,wait a second!!")

        if 'vs code' in query:
           os.system("TASKKILL /F /im code.exe")  
            
        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'word' in query:
            os.system("TASKKILL /F /im WINWORD.EXE")    

        elif 'zoom' in query:
            os.system("TASKKILL /F /im zoom.exe")

        elif 'pycharm' in query:
            os.system("TASKKILL /F /im pycharm64.exe")

        elif 'microsoft edge' in query:
            os.startfile("TASKKILL /F /IM msedge.exe/T")

        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")      

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe") 
            
        elif 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe") 

        speak("Your Command Has Been Completed Sir!!!!!") 

    def YoutubeAuto():
        speak("Whats Your Command ?")
        comm = takecommand()


        if 'pause' in comm:
            keyboard.press('k')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        elif 'enter' in comm:
            keyboard.press('enter')


        speak("Done sir!!")            

    def takeHindi():
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


    def Tran():
        speak("Tell Me The Line!")
        line = takeHindi()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        speak("The Translation for This Line Is:"+Text)




    def ChromeAuto():
        speak("Chrome Automation started!!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

        elif 'print' in command:
            keyboard.press_and_release('ctrl + p')

        elif 'save this page' in command:
            keyboard.press_and_release('ctrl + s')

        elif 'bookmark' in command:
            keyboard.press_and_release('ctrl + d')

        elif 'show downloads' in command:
            keyboard.press_and_release('ctrl + j')                            
        

    def screenshot():
        speak("ok sir , What Should I Name That File ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "C:\\Jarvis_Project\\screenshot\\ss"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Jarvis_Project\\screenshot\\ss")
        speak("Here Is Your Screenshot")





    while True:

        query = takecommand().lower()  # Convert input to lowercase for consistent matching

        if 'hello' in query:
            speak("Hello Sir! I Am Hydra, Your Personal AI Assistant.")
            speak("How may I help you?")

        elif 'how are you' in query:
            speak("I am fine, thank you!")
            speak("What about you?")

        elif 'you need a break' in query:
            speak("Sure sir, You can call me anytime. Have a great day.")
            speak("Just Say Wake up Hydra!!")
            break

        elif 'by' in query:
            speak("Okay sir ,Goodbye!")
            break
          
        elif 'youtube search' in query:
            speak("ok sir , This is what I found for your search!!")
            query = query.replace("hydra","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir")

        elif 'google search' in query:
            speak("ok sir , This is what I found for your search!!")
            query = query.replace("hydra","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("Done Sir")

        elif 'website' in query:
            speak("ok sir , Launching....!!")
            query = query.replace("hydra","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launched")

        elif 'launch' in query: 
            speak("Tell me the name of the website!!!") 
            name = takecommand()
            web ='https://www.' + name + '.com'  
            webbrowser.open(web)
            speak("Done sir")

        elif 'facebook' in query:
            speak("ok sir!!!")
            webbrowser.open("https://www.facebook.com")
            speak("Done sir....!")
        
        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            speak(f"According to wikipedia : {wiki}")
        
        elif 'whatsapp message' in query:
            Whatsapp()

        elif 'screenshot' in query:
            screenshot()

        elif 'open facebook' in query:
            openapps()

        elif 'open instagram' in query:
            openapps()        
        
        elif 'open maps' in query:
            openapps()

        elif 'open vs code' in query:
            openapps()
       
        elif 'open chrome' in query:
            openapps()

        elif 'open pycharm' in query:
            openapps()

        elif 'open microsoft edge' in query:
            openapps()

        elif 'open youtube' in query:
            openapps()

        elif 'open zoom' in query:
            openapps()
        
        elif 'word' in query:
            openapps()

        elif 'close facebook' in query:
            closeapps()

        elif 'close instagram' in query:
            closeapps()        
        
        elif 'close maps' in query:
            closeapps()

        elif 'close vs code' in query:
            closeapps()
              
        elif 'close chrome' in query:
            closeapps()

        elif 'close pycharm' in query:
            closeapps()

        elif 'close microsoft edge' in query:
            closeapps()

        elif 'close youtube' in query:
            closeapps()

        elif 'close zoom' in query:
            closeapps()                    

        elif 'close word' in query:
            closeapps()

        elif 'Pause' in query:
            keyboard.press('k')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'print' in query:
            keyboard.press_and_release('ctrl + p')

        elif 'save this page' in query:
            keyboard.press_and_release('ctrl + s')

        elif 'bookmark' in query:
            keyboard.press_and_release('ctrl + d')

        elif 'show downloads' in query:
            keyboard.press_and_release('ctrl + j')    



        elif 'chrome automation' in query:
            ChromeAuto()  

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)    
        
        elif 'type' in query:
            query = query.replace("type", "")
            pyautogui.typewrite(f"{query}", 0.1)

        elif 'repeat my words' in query:
            speak("speal sir!!")
            jj = takecommand()
            speak(f"You said : {jj}")

        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            speak("Enter the time!!")
            time = input(": Enter the Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                     speak("Time to wake up sir!!")
                     speak("Time to wake up sir!!")
                     speak("Time to wake up sir!!")
                     speak("Time to wake up sir!!")
                    
                     speak("Alarm closed!")

                elif now>time:
                    break     

        elif 'translator' in query:
            Tran()        
        
        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("hydra","")
            speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("You Tell Me that" + remeber.read())

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("hydra","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("This Is What I Found For Your Search!!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,3)
                speak(result)

            except:
                speak("No Speakable Data Available")    



TaskExe()
       
                
          
          
           
          
           

                   







    