from PIL import ImageGrab, Image
import numpy as np
import os
import pyautogui as py
import cv2
import keyboard
os.chdir("D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\image_recog")


# Load target and bluedot images
target_img = cv2.imread('fish1.png')
bluedot_img = cv2.imread('bluedot.png')


while True:
    if keyboard.is_pressed("q"):
        break

    # Take a screenshot of the screen
    screen = np.array(ImageGrab.grab())

    # Search for target image in screenshot
    target_loc = cv2.matchTemplate(screen, target_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(target_loc)

    print('best match %s' % str(max_loc))
    print('best match %s' % str(max_val))

    target_size_w = target_img.shape[1]/2
    target_size_h = target_img.shape[0]/2
    target_loc_center = (max_loc[0]+target_size_w, max_loc[1]+target_size_h)

    py.click(target_loc_center)












while True:
    # Take a screenshot of the screen
    screen = np.array(ImageGrab.grab())

    # Search for target image in screenshot
    target_loc = cv2.matchTemplate(screen, target_img, cv2.TM_CCOEFF_NORMED)

    # If target found, click on it and start searching for bluedot
    if len(target_match[0]) > 0:
        # Click on target using mouse events
        target_x, target_y = target_loc[::-1][0]
        print(f"Target found at ({target_x}, {target_y})")
        # Add code to click on the target image here
        
        # Start searching for bluedot
        while True:
            # Take another screenshot of the screen
            screen = np.array(ImageGrab.grab())
            
            # Convert the screenshot to grayscale
            screen_gray = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
            
            # Search for bluedot image in screenshot
            bluedot_loc = cv2.matchTemplate(screen_gray, bluedot_img, cv2.TM_CCOEFF_NORMED)
            bluedot_thresh = 0.8
            bluedot_match = np.where(bluedot_loc >= bluedot_thresh)
            
            # If bluedot found, click on it
            if len(bluedot_match[0]) > 0:
                bluedot_x, bluedot_y = bluedot_match[::-1][0]
                print(f"Bluedot found at ({bluedot_x}, {bluedot_y})")
                # Add code to click on the bluedot image here
            # If bluedot not found, go back to searching for target
            else:
                print("Bluedot not found, searching for target again")
                break
    # If target not found, keep searching
    else:
        print("Target not found, searching again")
        continue