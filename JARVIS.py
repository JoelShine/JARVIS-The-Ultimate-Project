import random
import datetime
import pyautogui
import time
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

################################################

# Place for creating the password if needed !

################################################

time.sleep(1)
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
        speak.Speak('Good Morning Boss !')
elif hour>=12 and hour<15:
        speak.Speak('Good Afternoon Boss !')
elif hour>=15 and hour<19:
        speak.Speak('Good Evening Boss !')
elif hour>=19 and hour<23:
        speak.Speak('Good Night Boss !')
        

hello = ["hi", "hello","hello jarvis","hi jarvis","Hi","Hello"]
gm = ["good morning","good morning jarvis","Good morning","Good morning jarvis"]
ge = ["good evening","good evening jarvis","Good evening","Good evening jarvis"]
gn = ["good night","good night jarvis","Good night","Good night jarvis"]
bye = ["see you later","see you later jarvis","bye","bye jarvis","goodbye","have a good day","See you later","See you later jarvis","Bye","Bye jarvis","Goodbye","Have a good day"]
howare = ["how are you","whats up","how you doing","how are you jarvis","How are you","Whats up","How you doing","How are you jarvis"]
name = ["what is your name","your name","do you have any name","what should i call you","Name","What is your name","What should i call you","What should I call you","name"]
time = ["what is the time","the current time","current time","open time","show time","What is the time","The current time","Current time","Open time","Show time"]
weather = ["what is the weather","weather report","current weather","open weather","open weather report","What is the weather","Weather report","Current weather","Open weather","Open weather report"]
bc = ["brilliant class","brilliant class jarvis","open brilliant class","Brilliant class","Brilliant class jarvis","Open brilliant class"]
bes = ["brilliant prmo","brilliant nsejs","brilliant scholarship","brilliant scholarships","open brilliant prmo","open brilliant nsejs","Brilliant prmo","Brilliant nsejs","Brilliant scholarship","Brilliant scholarships","Open brilliant prmo","Open brilliant nsejs"]
be = ["brilliant exam","brilliant exams","open brilliant exam","Brilliant exam","Brilliant exams","Open brilliant exam"]
google = ["open google","google","Open google","Google"]
date = ["open date","what is the date","show date","Open date","What is the date","Show date"]
calendar = ["open calendar","show calendar","Open calendar","Show calendar"]
whatsapp = ["open whatsapp","show whatsapp","Open whatsapp","Show whatsapp"]
news = ["open news","show news","Open news","Show news"]
wolframalpha = ["open wolframalpha","show wolframalpha","Open wolframalpha","Show wolframalpha"]
entertain = ["entertain me","play a song","Entertain me","Play a song"]
youtube = ["open youtube","show youtube","Open youtube","Show youtube"]
sandweb = ["open sand website","show sand website","Open sand website","Show sand website"]
desmos = ["graphing calculator","open graphing calculator","show graphing calculator","Graphing calculator","Open graphing calculator","Show graphing calculator"]
asoft = ["open soft murmur","show soft murmur","Open soft murmur","Show soft murmur"]
wind = ["windows 93","open windows 93","show windows 93","Windows 93","Open windows 93","Show windows 93"]
uf = ["open ultra folder","show ultra folder","Open ultra folder","Show ultra folder"]
bluej = ["bluej","open bluej","show bluej","Bluej","Open bluej","Show bluej"]
mac = ["mac os yellowstone","open mac os yellowstone","show mac os yellowstone","Mac os yellowstone","Open mac os yellowstone","Show mac os yellowstone"]
introduce = ["introduce yourself","please introduce yourself","who are you","iy","Introduce yourself","Please introduce yourself","Who are you"]
fe = ["open file explorer","show file explorer","open fe","show fe","Open file explorer","Show file explorer","Open fe","Show fe"]
note = ["open notepad","show notepad","Open notepad","Show notepad"]
gmail = ["open gmail","show gmail","gmail","Open gmail","Show gmail","Gmail"]
vi = ["increase the volume","increase volume","volume increase","iv","vi","volume up","up volume","Increase the volume","Increase volume","Volume increase","Volume up","Up volume"]
vd = ["decrease the volume","decrease volume","volume decrease","dv","vd","volume down","down volume","Decrease the volume","Decrease volume","Volume decrease","Volume down","Down volume"]
vm = ["mute the volume","mute volume","volume mute","mv","vm","Mute the volume","Mute volume","Volume mute","mv","vm"]
vum = ["unmute volume","unmute the volume","volume unmute","umv","vum","Unmute volume","Unmute the volume","Volume unmute","umv","vum"]
zoom = ["open zoom","show zoom","Open zoom","Show zoom"]
mon = ["monday's timetable","timetable of monday","monday's time table","time table of monday","Monday's timetable","Timetable of monday","Monday's time table","Time table of monday"]
tue = ["tuesday's timetable","timetable of tuesday","tuesday's time table","time table of tuesday","Tuesday's timetable","Timetable of tuesday","Tuesday's time table","Time table of tuesday"]
wed = ["wednesday's timetable","timetable of wednesday","wednesday's time table","time table of wednesday","Wednesday's timetable","Timetable of wednesday","Wednesday's time table","Time table of wednesday"]
thurs = ["thursday's timetable","timetable of thursday","thursday's time table","time table of thursday","Thursday's timetable","Timetable of thursday","Thursday's time table","Time table of thursday"]
fri = ["friday's timetable","timetable of friday","friday's time table","time table of friday","Friday's timetable","Timetable of friday","Friday's time table","Time table of friday"]
sat = ["saturday's timetable","timetable of saturday","saturday's time table","time table of saturday","Saturday's timetable","Timetable of saturday","Saturday's time table","Time table of saturday"]
sun = ["sunday's timetable","timetable of sunday","sunday's time table","time table of sunday","Sunday's timetable","Timetable of sunday","Sunday's time table","Time table of sunday"]
sel = ["import selenium","get selenium","open selenium","show selenium","Import selenium","Get selenium","Open selenium","Show selenium"]
takepicture = ["take a picture","please take a picture","take my picture please","take my picture","can you take my picture","can you take a picture","Take a picture","Please take a picture","Take my picture please","Take my picture","Can you take my picture","Can you take a picture"]
gmailsent = ["sent gmail","sent a message","send a message","Sent gmail","Sent a message","Send a message"]
screenshot = ["take screenshot","take a screenshot","please take a screenshot","take a screen shot","take the screenshot","take sreen shot","take the screen shot","Take screenshot","Take a screenshot","Please take a screenshot","Take a screen shot","Take the screenshot","Take sreen shot","Take the screen shot"]

print("JARVIS - The Virtual Assistant cum ChatBot in Python.\n")




while True:
        #pyautogui.click(1138,748)
        #pyautogui.moveTo(296,463,duration=1)
        #pyautogui.click(296,463)
        #pyautogui.click(296,463)
        a = input('User - ')
        

        if a.lower() in time:
                now = datetime.datetime.now()
                speak.Speak("Sir, the current time is "+now.strftime("%H:%M")+'\n')
                print ("Sir, the Current Time is : ")
                print (now.strftime("%H:%M")+'\n')

        elif a.lower() in screenshot:
                speak.Speak("Preparing to take Screen shot !")
                pyautogui.hotkey('alt','space','n')
                pyautogui.hotkey('alt','space','n')
                pyautogui.hotkey('win','shift','s')
                pyautogui.moveTo(946,767,duration=5)
                pyautogui.click(728,29)
                pyautogui.moveTo(946,767,duration=5)
                pyautogui.click(1231,629)

        elif a.lower() in gmailsent:
                speak.Speak("Who is the reciever - ")
                print("Who is the reciever - ")
                x = input()
                print("     ")
                speak.Speak("What is the subject - ")
                print("What is the subject - ")
                y = input()
                print("     ")
                speak.Speak("What is the message - ")
                print("What is the message - ")
                z = input()
                print("     ")

                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.moveTo(946,767,duration=1)
                pyautogui.typewrite("mail.google.com")
                pyautogui.typewrite(["enter"])
                pyautogui.moveTo(946,767,duration=26)
                pyautogui.click(80,194)
                pyautogui.moveTo(946,767,duration=3)
                pyautogui.click(722,285)
                pyautogui.typewrite(x)
                pyautogui.click(735,332)
                pyautogui.typewrite(y)
                pyautogui.click(716,373)
                pyautogui.typewrite(z)
                pyautogui.click(731,690)

        elif a.lower() in takepicture:
                speak.Speak("Sure Boss. Opening Camera.")
                pyautogui.click(15,743)
                pyautogui.typewrite("cam",interval=0.25)
                pyautogui.typewrite(["enter"])
                pyautogui.moveTo(1318,373,duration=5)
                speak.Speak("Smile Please !")
                pyautogui.click(1318,373)
                print("     ")

        elif a.lower() in sel:
                speak.Speak("Selenium successfully imported. Sir, what do you want to open with selenium ?")
                print("Please enter the url of the website.")
                x = input()
                PATH = "C:\Program Files (x86)\msedgedriver.exe"
                driver = webdriver.Edge(PATH)
                driver.get(x)
                print("     ")

        elif a.lower() in mon:
                speak.Speak("Sir, today you have Physics at 11 AM and Mathematics by Reena Tecaher at 12 PM")
                print("Physics at 11:00 AM and Mathematics by Reena Teacher at 12:00 PM")
                print("     ")

        elif a.lower() in tue:
                speak.Speak("Sir, today you have Geography at 10 AM and Chemistry at 11 AM")
                print("Geography at 10:00 AM and Chemistry at 11:00 AM")
                print("     ")

        elif a.lower() in wed:
                speak.Speak("Sir, today you have Biology at 10 AM and History at 11 AM")
                print("Biology at 10:00 AM and History at 11:00 AM")
                print("     ")

        elif a.lower() in thurs:
                speak.Speak("Sir, today you have Malayalam at 11 AM and Computer at 12 PM")
                print("Malayalam at 11:00 AM and Computer at 12:00 PM")
                print("     ")

        elif a.lower() in fri:
                speak.Speak("Sir, today you have English at 11 AM and Mathematics by A K Sir at 12 PM")
                print("English at 11:00 AM and Mathematics by A K Sir at 12:00 PM")
                print("     ")

        elif a.lower() in sat:
                speak.Speak("Sir, today you have Brilliant Sir ! You also have music class Sir !")
                print("Sir, today you have Brilliant Sir ! You also have music class Sir !")
                print("     ")

        elif a.lower() in sun:
                speak.Speak("Sir, today you may have Brilliant exam and there is also class ! You also have sunday shool.")
                print("Sir, today you may have Brilliant exam and there is also class ! You also have sunday shool.")
                print("     ")

        elif a.lower() in zoom:
                speak.Speak("Opening Zoom Meetings")
                pyautogui.click(15,743)
                # Start Button - (x=15, y=743)
                pyautogui.typewrite("zoom")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in hello:
                speak.Speak("Welcome back Sir ! How can I help you ?")
                print ("Welcome back Sir ! How can I help you ?")
                print("     ")

        elif a.lower() in vi:
                speak.Speak("As you wish Sir !")
                pyautogui.hotkey('volumeup')
                print("Volume increased")
                print("     ")

        elif a.lower() in vd:
                speak.Speak("As you wish Sir !")
                pyautogui.hotkey('volumedown')
                print("Volume decreased")
                print("     ")

        elif a.lower() in vm:
                speak.Speak("As you wish Sir !")
                pyautogui.hotkey('volumemute')
                print("Volume muted")
                print("     ")

        elif a.lower() in vum:
                speak.Speak("As you wish Sir !")
                pyautogui.hotkey('volumemute')
                print("Volume unmuted")
                print("     ")

        elif a.lower() in vi:
                speak.Speak("As you wish Sir !")
                print("Increasing the volume.")
                print("     ")

        elif a.lower() in gm:
                speak.Speak("Good Morning Sir !")
                print ("Good Morning Sir !")
                print("     ")

        elif a.lower() in ge:
                speak.Speak("Good Evening Sir !")
                print ("Good Evening Sir !")
                print("     ")

        elif a.lower() in gn:
                speak.Speak("Good Night Sir !")
                print ("Good Night Sir !")
                print("     ")

        elif a.lower() in bye:
                speak.Speak("Bye Boss ! Have a good day !")
                botans = ["Bye Boss ! Have a good day !"]
                print(random.choice(botans)+'\n')

        elif a.lower() in howare:
                speak.Speak("I am Fine Boss ! I am Glad you asked !")
                botans = ["I am Fine Boss ! I am Glad you asked !"]
                print(random.choice(botans)+'\n')

        elif a.lower() in weather:
                speak.Speak("Opening Weather Forecast")
                PATH = "C:\Program Files (x86)\msedgedriver.exe" 
                driver = webdriver.Edge(PATH) 
                print("     ")
                driver.get("https://www.google.co.in/search?safe=active&sxsrf=ALeKk01u9G0PSIPrqMft3TvLgP2sQMMxdQ%3A1603689690920&ei=2lyWX6LlN4nB3LUPz-6FcA&q=Today%27s+weather&oq=Today%27s+weather&gs_lcp=CgZwc3ktYWIQAzIMCCMQJxCdAhBGEIACMgUIABCxAzIFCAAQsQMyAggAMgIIADICCAAyBQgAELEDMgIIADICCAAyAggAOgQIABBHOgcIIxDJAxAnOgcIABCxAxBDOgIILjoICAAQsQMQgwE6BwgjEOoCECc6BwguEOoCECc6BAgjECc6BwgAEMkDEEM6CggAELEDEIMBEEM6BwguEMkDEEM6BAguEEM6CgguEMcBEKMCEEM6BAgAEEM6DwgjELECECcQnQIQRhCAAjoHCAAQsQMQCjoECAAQClCP46wLWITSrQtg19itC2gDcAJ4AIABjgOIAfQXkgEIMC4yMi4wLjGYAQCgAQGqAQdnd3Mtd2l6sAEKyAEIwAEB&sclient=psy-ab&ved=0ahUKEwiiuu3SwdHsAhWJILcAHU93AQ4Q4dUDCA0&uact=5&safe=active")
                print(driver.title)

                try:
                    wob_tm = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "wob_tm"))
                    )
                    print("Sir, the current temperature is "+wob_tm.text+" degree celsius.")
                    speak.Speak("Sir, the current temperature is "+wob_tm.text+" degree celsius.")
                except:
                    driver.quit()
                
                driver.quit()

        elif a.lower() in fe:
                speak.Speak("Opening File Explorer")
                pyautogui.click(15,743)
                # Start Button - (x=15, y=743)
                pyautogui.typewrite("File")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in note:
                speak.Speak("Opening Notepad")
                pyautogui.click(15,743)
                # Start Button - (x=15, y=743)
                pyautogui.typewrite("Note")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in introduce:
                speak.Speak("Hello ! My name is JARVIS !I am a virtual assistant cum Chatbot.I can help you automate your desktop apps and your important websites. I was made using the package 'pyautogui' without selenium and other stuff.My creator is Mr.Joel Shine, currently studying in 8th standard.I am hoping you would be very helpful with this program.With regards, Your assistant, JARVIS")
                print("     ")
                
        elif a.lower() in bc:
                speak.Speak("Opening Brilliant Classes")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("brilliantpalaclasses.com")
                pyautogui.typewrite(["enter"])
                print("     ")
                
        elif a.lower() in bes:
                speak.Speak("Opening Brilliant Pala NSEJS or PRMO Exams")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("jeebrilliantpalaexams.com")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in be:
                speak.Speak("Opening Brilliant Pala Exams")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("www.palabrilliantexams.in")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in google:
                speak.Speak("Opening Google")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("google")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in whatsapp:
                speak.Speak("Opening Whatsapp")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("web.whatsapp.com")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in wolframalpha:
                speak.Speak("Opening Wolframalpha")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("wolframalpha")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in entertain:
                speak.Speak("Opening Interstellar Cornfield Chase")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("https://music.youtube.com/watch?v=dkWm59GfLz4&list=RDAMVMdkWm59GfLz4")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in youtube:
                speak.Speak("Opening Youtube")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("you")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in sandweb:
                speak.Speak("Opening Sand Website")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("thisi")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in desmos:
                speak.Speak("Opening Graphing calculator")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("desmos")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in asoft:
                speak.Speak("Opening a soft murmur")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("asoft")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in wind:
                speak.Speak("Opening Windows 93")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("wind")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in gmail:
                speak.Speak("Opening Gmail")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("mail.google.com")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in uf:
                speak.Speak("Opening Ultra Folder")
                pyautogui.click(1365,742)
                pyautogui.click(480,26)
                pyautogui.click(480,26)
                print("     ")

        elif a.lower() in bluej:
                speak.Speak("Opening Bluej")
                pyautogui.click(1365,742)
                pyautogui.click(334,25)
                pyautogui.click(334,25)
                print("     ")

        elif a.lower() in mac:
                speak.Speak("Opening Mac Os Yellowstone")
                pyautogui.click(1365,742)
                pyautogui.click(1306,40)
                pyautogui.click(1306,40)
                print("     ")

        elif a.lower() in news:
                speak.Speak("Showing today's news")
                pyautogui.click(15,743)
                pyautogui.typewrite("news")
                pyautogui.typewrite(["enter"])
                print("     ")

        elif a.lower() in calendar:
                speak.Speak("Opening Calendar")
                pyautogui.click(1218,746)
                print("     ")

        elif a.lower() in date:
                PATH = "C:\Program Files (x86)\msedgedriver.exe" 
                driver = webdriver.Edge(PATH) 
                print("     ")
                driver.get("https://www.google.co.in/search?safe=active&sxsrf=ALeKk00U0Q148cq078aL9Ry-5xh3dYSLIA%3A1603715962734&source=hp&ei=esOWX5qCKuWLmgeWg7awCQ&q=date&oq=date&gs_lcp=CgZwc3ktYWIQAzIKCAAQsQMQyQMQQzIKCAAQsQMQFBCHAjIHCAAQsQMQQzIECAAQQzIECAAQQzIHCC4QsQMQQzIFCAAQsQMyBQgAELEDMgIIADICCAA6CQgjECcQRhD5AToECCMQJzoICAAQsQMQgwE6AgguOgcIABDJAxBDOgQILhBDOgoIABCxAxCDARBDOgUILhCxA1CdPVj8QGCbSmgAcAB4AIABxAGIAYsFkgEDMC40mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwiap5vCo9LsAhXlheYKHZaBDZYQ4dUDCAc&uact=5&safe=active")
                print(driver.title)

                try:
                    xpath = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div"))
                    )
                    print("Sir, the current date is "+xpath.text)
                    speak.Speak("Sir, the current date is "+xpath.text)
                except:
                    driver.quit()
                
                driver.quit()
                

        elif a.lower() in name:
                speak.Speak("Sir, my name is Jarvis. I am a virtual desktop assistant cum Chatbot !")
                botans = ["Sir, my name is Jarvis. I am a virtual desktop assistant cum Chatbot !"]
                print(random.choice(botans)+'\n')

        else:
                speak.Speak("Searching for "+a)
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite(a)
                pyautogui.typewrite(["enter"])
                print("     ")
                
                
