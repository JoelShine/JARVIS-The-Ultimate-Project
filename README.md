# JARVIS-The-Ultimate-Project
This is a project of mine which includes all the python skills I have learnt !

This project contains many modules which enhances the ability of this project. Some of the modules may 
be only supported in Windows or in Windows 10 as I am using Windows 10 for creating this project. This 
project is about a simple but efficient desktop or web assistant which can perform simple tasks like
showing the time or date, opening specific websites, giving us the current weather, opening apps in the 
desktop and start button using very simple automation and things like that. The main modules used in 
this project are :

      1 )importing random (default module)
      2 )importing datetime (default module)
      3 )importing pyautogui (needed to be installed)
      4 )importing time (default module)
      5 )importing win32com.client as wincl (default module)
      6 )importing selenium (needed to be installed)

These modules all have specific tasks in this project. For detailed explanatation, please read the following :

Random module
-------------

This module is used for inserting the most basic commands given to the computer to perform specific tasks.
For Eg: If we are asking the computer "what is the weather", we can do in many varieties like:

      1 ) what is the weather (everything in small letters)
      2 ) What is the weather (W in What is in capital letters)
      3 ) what is the Weather (W in Weather is in capital letters)
      4 ) What is the Weather (W in both What and Weather in capital letters)
      5 ) show weather 
      6 ) open weather 
      7 ) show weather report 
      8 ) open weather report etc...

For the last four options also, there are a no.of varieties. So in this case, I have taken everything 
as small letters as encoding all of these to the computer will take a millenia. So, the frequent 
command we use is encoded inside each type of random box which is in the square brackets if you look
in the code "[]" . Then from now on if you insert any text which are already inside these [], then the 
computer will detect it and give you the respective output.

This is a screenshot from the code - https://github.com/JoelShine/JARVIS-The-Ultimate-Project/blob/main/Random%20module%20in%20action.png

Datetime module
---------------

This is a very simple module as this module gives us the current date and time. You can see that from 
the code. Another thing using this module is that this can help greet you according to the time.
How the computer will greet you is covered in the fifth module.

This is a screenshot for giving current time - 
https://github.com/JoelShine/JARVIS-The-Ultimate-Project/blob/main/Datetime%20module%20giving%20the%20current%20time.png

This is a screenshot for giving current date - 
https://github.com/JoelShine/JARVIS-The-Ultimate-Project/blob/main/Datetime%20module%20giving%20the%20current%20date.png

Pyautogui module 
----------------

Now this is the module which we uses the most. This module is used to do the desktop automation , that is
through this module, we can do clicks, hover, scroll, or type anything without actually doing anything
by ourselves. You just write the codes and the computer will do that for you. This is very helpful but
the only disadvantage is that this module only works with the help of coordinates which are located in
our screen. 

What this means is that, if we are writing a program to open notepad which is in our Taskbar, we 
give the coordinates so that it can go there and and click and open the program. But if we changed the
position of Notepad and instead give the position of File Explorer, instead of opening notepad, it will 
open file explorer.

But, if you are not changing anything of it, then this is the best module for desktop as well as web
automation.

For more details, please visit - https://pyautogui.readthedocs.io/en/latest/

This is a screenshot from the code - https://github.com/JoelShine/JARVIS-The-Ultimate-Project/blob/main/Pyautogui%20module%20in%20action.png

Time module
-----------

Now, this module is mainly used in this program to pause the code. Using this, for example, if something
takes a while to load, then we can say "time.sleep(5)" and in this case, the code stops or pauses for
five seconds. For mode information, you can search about the time module.

"win32com.client as wincl" module or Microsoft Sapi voice module
----------------------------------------------------------------

Now, this is a text to speech module which is default and accessible only in Windows. For Mac, there is 
a module named mac-say which is the default text to speech module for mac. There are many other modules 
such as Google Speech api, pyttsx3 module etc. But in my case, only Sapi worked perfectly.

We can change the voice, by going to the Settings. For more, please search How to import Sapi in python.

This is a screenshot from the code - https://github.com/JoelShine/JARVIS-The-Ultimate-Project/blob/main/Microsoft%20Sapi%20module%20in%20action.png

Selenium module
---------------

Selenium is the perfect module for web automation. Using an application called webdriver which differs according to the browser, we can 
search on the browser without coordinates but with some id, names, class names which are in the page source of a webpage.

Selenium can be used for web scraping which means we can interact with the elements in a HTML webpage. Here we interacted with the element which was the google search bar. We wrote the code to click on the search bar and type our input there and press enter to get the search results without opening google !

Selenium Documentation - https://selenium-python.readthedocs.io/

The Main requirements for this program are:

1 ) Install Python on your computer. Python can be installed from the main site and for this project I have used Python 3.8.5 version. Also make sure that you have pip installed on your computer. For any problems with pip, just go to https://pip.pypa.io/en/stable/installing/#id7 . To download python, go to https://www.python.org/downloads/

2 ) Install Selenium on your computer. It can be done using the "pip install selenium" in command prompt for windows users. For Mac or Linux, they have to do it using "sudo".

3 ) Webdriver installed on your computer. This can be done using the following steps :

a ) First, go to your browser settings and select "About your browser". Just note down the version
    of your browser.

b ) Next search in the net for "yourbrowsername webdriver". Go to the link for downloading the webdriver
    and download it accoording to your browser version. 

    If you are using Chrome, then go to - https://sites.google.com/a/chromium.org/chromedriver/downloads
    If you are using Edge, then go to - https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

c ) After installing the webdriver, if you are windows user, go to the "Program Files (x86)" folder
    and paste the webdriver.exe file there. Normally it should work if we place the webdriver in any
    folder but in my case, it worked only when I moved that to the "Program Files (x86)" folder.
    If you are a Mac user or Linux, please make sure you have safely kept the webdriver.exe in an 
    important folder.

d ) Now we are ready to do web automation. I have used Microsoft Edge Driver for this but you can 
    change the name of the "PATH" according to your browser.
    
This is a screenshot from the code - https://github.com/JoelShine/JARVIS-The-Ultimate-Project/blob/main/Selenium%20module%20in%20action.png

**Important notice**

If you want to copy my taskbar apps, I have given the screenshot of it, but, you want to find the coordinates and replace it with the code,
I have also given the code to find the coordinates. It is in "Finding coordinates.py" and is very easy to memorize.

Link to my taskbar screenshot - https://github.com/JoelShine/JARVIS-The-Ultimate-Project/blob/main/My%20Taskbar.png

Link to find the coordinates in your screen - https://github.com/JoelShine/JARVIS-The-Ultimate-Project/blob/main/Finding%20coordinates.py
