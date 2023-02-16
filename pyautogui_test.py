import pyautogui
import time


numMin = 3

while True:
    x = 0
    while x < numMin:
        time.sleep(60)
        x += 1
        for i in range(0, 200):
            pyautogui.moveTo(0, i * 4)
            pyautogui.moveTo(1, 1)
            for i in range(0, 3):
                pyautogui.press("shift")
