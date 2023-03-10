import cv2
import numpy as np
import pyautogui as pg
import os
import time
import random
import keyboard

os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Automation') 


# list of image filenames to search for
#image_filenames = ["target.png", "target2.png", "target3.png"]
TARGET_FILENAMES = ["fish.png"]#,"fish1.png"]
Fish_area = "fish_area.png"
bluedot = "bluedot.png"

count = 0
#while True:

    x, y = pg.position()
    #boundaries = pg.locateOnScreen(Fish_area, confidence=0.6)
    #boundaries_tuple = (boundaries.left, boundaries.top, boundaries.width, boundaries.height)



while True: 
    if keyboard.is_pressed("q"):
        break
    bluedot_loc = pg.locateOnScreen(bluedot, confidence=0.9,region = (1747,799,339,111))
    if bluedot_loc == None:
        for target_filename in TARGET_FILENAMES:
            print(f"looking for fish {target_filename}")
            target_location = pg.locateOnScreen(target_filename, confidence=0.5,region=(1533,262,900,400))
            if target_location is not None:
                print(f"Found {target_filename} at {target_location}")
                pg.click(pg.center(target_location))
                print(target_location)
    else:
        pg.click(pg.center(bluedot_loc))
        bluedot_loc = pg.locateOnScreen(bluedot, confidence=0.9)
        bluedot_loc = None
        
                

    
    
    
    
    
    
    

