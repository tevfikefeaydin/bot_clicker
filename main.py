import pyautogui
import time

for i in range(5000):
    time.sleep(1)
    cords=pyautogui.locateOnScreen("Capture.PNG")
    if cords != None:
      print(pyautogui.locateOnScreen("Capture.PNG"))
      pyautogui.leftClick(cords)
