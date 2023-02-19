import cv2
import numpy as np
import pyautogui as pg
import os
import time
import random

os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Automation') 

screenshot = pg.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
plantall = pg.locateOnScreen('plantall.png', confidence=0.8)
harvestall = pg.locateOnScreen('harvestall.png', confidence=0.8)

# list of image filenames to search for
#image_filenames = ["target.png", "target2.png", "target3.png"]
image_filenames = ["target.png"]





while True:
    x, y = pg.position()

    # Take a screenshot of the desktop
    screenshot = pg.screenshot()

    #adjust colours
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    plantall = pg.locateOnScreen('plantall.png', confidence=0.8)
    harvestall = pg.locateOnScreen('harvestall.png', confidence=0.8)

    # search for each image and print its location if found
    for filename in image_filenames:
        target = pg.locateOnScreen(filename, confidence=0.8)
        if target is not None:
            print(f"Found {filename} at {target}")
            print(target)
            harvest_center = pg.center(harvestall)
            plant_center = pg.center(plantall)
            pg.click(harvest_center)
            time.sleep(random.randint(5, 10))
            pg.click(plant_center)
            pg.moveTo(x,y)
        else:
            print(f"Did not find {filename}")
    
    time.sleep(random.randint(10, 40)) # Wait for a second before checking again