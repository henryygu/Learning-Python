import cv2
import numpy as np
import pyautogui as pg
import os
import time
import random
import logging
from threading import Thread

logging.basicConfig(level=logging.INFO)

os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Automation')

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

def find_and_click_targets(image_filenames, harvest_filenames, plant_filenames):
    x, y = pg.position()
    harvest_locations = find_targets(harvest_filenames)
    plant_locations = find_targets(plant_filenames)

    # search for each image and print its location if found
    for filename in image_filenames:
        target = pg.locateOnScreen(filename, confidence=0.8)
        if target is not None:
            logging.info(f"Found {filename} at {target}")
            click_targets(harvest_locations)
            pg.moveTo(x,y)
            time.sleep(random.randint(5, 10))
            click_targets(plant_locations)
            pg.moveTo(x,y)
        else:
            logging.info(f"Did not find {filename}")

def run_script():
    while True:
        try:
            find_and_click_targets(image_filenames, harvest_filenames, plant_filenames)
            time.sleep(random.randint(10, 40))
        except Exception as e:
            logging.error(e)

if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = Thread(target=run_script)
        t.daemon = True
        t.start()
        threads.append(t)
    for t in threads:
        t.join()