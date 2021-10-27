import time

import pyautogui
#for i in range(5000): bundan sonra time.sleep() komutu olacak - x = 1 while x > 0: bu ikincikod
x = 1
while x > 0:
    time.sleep(5)
    cords=pyautogui.locateOnScreen("Capture.PNG", confidence=0.9)
    if cords != None:
      print(cords)
      from win10toast import ToastNotifier

      toaster = ToastNotifier()
      toaster.show_toast("ADUZEM!!!",
                         "Bot hemen başlıyor",
                         duration=4)
      pyautogui.leftClick(cords)




