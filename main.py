import time
import pyautogui
from win10toast import ToastNotifier

x = 1
while x > 0:
    time.sleep(5)
    cords = pyautogui.locateOnScreen("Capture.PNG", confidence=0.9)
    if cords is not None:
        print(cords)
        toaster = ToastNotifier()
        toaster.show_toast("ADUZEM!!!", "Bot hemen başlıyor", duration=4)
        pyautogui.leftClick(cords)
