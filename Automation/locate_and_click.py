import cv2
import numpy as np
import pyautogui as pg
import os
import time
import random

os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Automation') 


# list of image filenames to search for
#image_filenames = ["target.png", "target2.png", "target3.png"]
TARGET_FILENAMES = ["target.png","target1.png"]
HARVEST_FILENAMES = ["harvestall.png","harvestall2.png"]
PLANT_FILENAMES = ["plantall.png","plantall2.png"]


def find_targets(image_filenames, confidence=0.8):
    """
    Finds the locations of the target images and returns a list of tuples
    containing the (x, y) coordinates of each location.
    """
    locations = []
    for filename in image_filenames:
        location = pg.locateOnScreen(filename, confidence=confidence)
        if location is not None:
            locations.append(location)
    return locations

def click_targets(locations):
    """
    Clicks on all of the locations in the list of tuples containing the
    (x, y) coordinates of the target images.
    """
    for location in locations:
        center = pg.center(location)
        pg.click(center)


def search_for_targets():
    """
    Searches for the target images and performs the corresponding actions
    if they are found.
    """
    # Search for each target image and perform the corresponding action if found
    x, y = pg.position()
    for target_filename in TARGET_FILENAMES:
        target_location = pg.locateOnScreen(target_filename, confidence=0.9)
        if target_location is not None:
            print(f"Found {target_filename} at {target_location}")
            click_targets(find_targets(HARVEST_FILENAMES))
            pg.moveTo(x,y)
            time.sleep(random.uniform(5, 10))
            click_targets(find_targets(PLANT_FILENAMES))
            pg.moveTo(x,y)
        else:
            print(f"Did not find {target_filename}")

count = 0
#while True:
while count < 30:
    print(count)
    count+=1
    search_for_targets()    
    wait_time = random.uniform(10, 40)
    print(wait_time)
    time.sleep(wait_time)