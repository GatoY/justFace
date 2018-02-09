import os
import time
def openApp(appName):
    command = 'osascript -e \'tell app \"'+appName+'\" to activate\''
    os.system(command)
def play():
    command = 'osascript -e \'tell app \"System Events\" to keystroke \" \" using {command down, option down}\''
    os.system(command)
appName='NeteaseMusic'
openApp(appName)
time.sleep(5)
play()
