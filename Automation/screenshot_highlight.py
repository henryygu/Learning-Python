import cv2
import numpy as np
import pyautogui as pg
import os

os.chdir("D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Automation")

screenshot = pg.screenshot()
screenshot = np.array(screenshot)
pawn = pg.locateOnScreen("fish_area.png", confidence=0.6)
pawn_tuple = (pawn.left, pawn.top, pawn.width, pawn.height)
pawn = pg.locateOnScreen("fish1.png", region=pawn, confidence=0.6)
cv2.rectangle(
    screenshot,
    (pawn.left, pawn.top),
    (pawn.left + pawn.width, pawn.top + pawn.height),
    (0, 0, 255),
    2,
)
pg.moveTo(pg.center(pawn))

cv2.imshow("image", screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()
