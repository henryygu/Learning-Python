import cv2
import numpy as np
import pyautogui as pg
import os
import time
import random

os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Automation') 


# list of image filenames to search for
#image_filenames = ["target.png", "target2.png", "target3.png"]
image_filenames = ["target.png","target1.png"]
harvest_filenames = ["harvestall.png","harvestall2.png"]
plant_filenames = ["plantall.png","plantall2.png"]


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

# locations = find_targets(image_filenames)
# harvest_locations = find_targets(harvest_filenames)
# plant_locations = find_targets(plant_filenames)

# click_targets(locations)





while True:
    x, y = pg.position()

    # Take a screenshot of the desktop
    # screenshot = pg.screenshot()

    #adjust colours
    # screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    harvest_locations = find_targets(harvest_filenames)
    plant_locations = find_targets(plant_filenames)

    # search for each image and print its location if found
    for filename in image_filenames:
        target = pg.locateOnScreen(filename, confidence=0.8)
        if target is not None:
            print(f"Found {filename} at {target}")
            print(target)
           
           
            click_targets(harvest_locations)
            pg.moveTo(x,y)
            time.sleep(random.randint(5, 10))
            click_targets(plant_locations)
            pg.moveTo(x,y)
        else:
            print(f"Did not find {filename}")
    
    time.sleep(random.randint(10, 40)) # Wait for a second before checking again