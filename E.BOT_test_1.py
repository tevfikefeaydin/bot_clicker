import time
import pyautogui
from tkinter import *

root = Tk()
status = False
timeloop= 1000


def startApp():
    global status
    status = True
    exeButton.config(text='Durdur', comman=stopApp)
    print("str")
    bot()



def stopApp():
    global status
    status = False
    exeButton.config(text='Çalış', comman=startApp)
    print("stop1")


def bot():
    if status:


            time.sleep(5)
            cords = pyautogui.locateOnScreen("Capture.PNG", confidence=0.9)
            if cords is not None:
                print(cords)

                pyautogui.leftClick(cords)
    root.after(timeloop, bot)




global exeButton
exeButton = Button(root, text='Çalış', command=startApp, width=20, height=2)  # button büyüklüğü ve button
exeButton.pack()
root.mainloop()