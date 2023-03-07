import logging
import os
import random
import threading
import time

import cv2
import numpy as np
import pyautogui as pg


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.FileHandler("automation.log"), logging.StreamHandler()],
)
logger = logging.getLogger()


# Define image file names and other parameters
image_filenames = ["target.png", "target1.png"]
harvest_filenames = ["harvestall.png", "harvestall2.png"]
plant_filenames = ["plantall.png", "plantall2.png"]
confidence = 0.8


def find_targets(image_filenames, confidence):
    """
    Finds the locations of the target images and returns a list of tuples
    containing the (x, y) coordinates of each location.
    """
    locations = []
    for filename in image_filenames:
        try:
            location = pg.locateOnScreen(filename, confidence=confidence)
        except Exception as e:
            logger.warning(f"Error locating {filename}: {e}")
            continue
        if location is not None:
            locations.append(location)
    return locations


def click_targets(locations):
    """
    Clicks on all of the locations in the list of tuples containing the
    (x, y) coordinates of the target images.
    """
    for location in locations:
        try:
            center = pg.center(location)
            pg.click(center)
            logger.info(f"Clicked at {center}")
        except Exception as e:
            logger.warning(f"Error clicking at {location}: {e}")


def automation_loop():
    while True:
        try:
            # Locate target images
            target_locations = find_targets(image_filenames, confidence)

            # Perform actions on target images
            if target_locations:
                logger.info(f"Found {len(target_locations)} targets")
                harvest_locations = find_targets(harvest_filenames, confidence)
                click_targets(harvest_locations)
                time.sleep(random.uniform(5, 10))
                plant_locations = find_targets(plant_filenames, confidence)
                click_targets(plant_locations)
                time.sleep(random.uniform(5, 10))
            else:
                logger.info("No targets found")

            # Sleep for a random duration
            sleep_duration = random.uniform(10, 40)
            logger.info(f"Sleeping for {sleep_duration:.1f} seconds")
            time.sleep(sleep_duration)

        except Exception as e:
            logger.error(f"Error in automation loop: {e}", exc_info=True)
            time.sleep(5)


if __name__ == "__main__":
    # Change working directory to image folder
    os.chdir("D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Automation")

    # Start multiple automation threads
    num_threads = 3
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=automation_loop, name=f"Automation-{i+1}")
        t.start()
        threads.append(t)

    # Wait for threads to finish
    for t in threads:
        t.join()

    logger.info("All automation threads have stopped")
