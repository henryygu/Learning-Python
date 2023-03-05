import pyautogui as py
import pygetwindow as gw
from math import floor
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

path = "D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Automation\\targetimg.jpg"
img = Image.open(path)

canvasOffset = (50, 144)
editColors = (999, 89)
editColorsR = (1467,592)
editColorsG = (1471,613)
editColorsB = (1473,640)
editColorsOK = (1105,660)

clamp = lambda n, minn, maxn: max(min(maxn, n), minn)
maxStrokes = 3
strokeOffset = 20
strokeLengthOffset = 35
strokeCount = 0
color = []
x1 = 0
x2 = 0
y1 = 0
y2 = 0


def randRange(start, end):
    return floor(random() * (end - start) + start)

def draw(startX, startY, endX, endY):
    py.moveTo(canvasOffset[0] + startX, canvasOffset[1] + startY)
    py.dragTo(canvasOffset[0] + endX, canvasOffset[1] + endY)

def setColor(r, g, b):
    # Move over edit colors
    py.moveTo(editColors[0], editColors[1])
    py.click()
    # Set R value
    py.moveTo(editColorsR[0], editColorsR[1])
    py.click(clicks=2)
    py.typewrite(str(r))
    # Set G value
    py.moveTo(editColorsG[0], editColorsG[1])
    py.click(clicks=2)
    py.typewrite(str(g))
    # Set B value
    py.moveTo(editColorsB[0], editColorsB[1])
    py.click(clicks=2)
    py.typewrite(str(b))
    # Click OK
    py.moveTo(editColorsOK[0], editColorsOK[1])
    py.click()



mspaintWin = gw.getWindowsWithTitle('Paint')[0]

mspaintWin.maximize()


#setColor(color[0], color[1], color[2])

width, height = img.size

original_img_array = np.array(img)
pixels = original_img_array.reshape(-1, 3)
n_colors = 16
kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(pixels)
new_pixels = kmeans.predict(pixels)
img_array = kmeans.cluster_centers_[new_pixels].reshape(img_array.shape).astype(np.uint8)

#check image
#import matplotlib.pyplot as plt
#fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
#ax[0].imshow(img)
#ax[0].set_title("Original")
#ax[1].imshow(new_img_array)
#ax[1].set_title(f"{n_colors} colors")
#plt.show()






unique_colors = np.unique(img_array.reshape(-1, img_array.shape[-1]), axis=0)
from tqdm import tqdm
# Loop through each color channel
for color in unique_colors:
    r, g, b = color
    # Find the x, y coordinates of pixels with this RGB color
    coords = np.argwhere(np.all(img_array == color, axis=-1))
    setColor(color[0], color[1], color[2])
    # Print the coordinates
    for x, y in tqdm(coords):
        #print(f"Pixel at ({x}, {y}) has RGB color ({r}, {g}, {b})")   
        py.moveTo(x+canvasOffset[0],y+canvasOffset[1])
        py.click()

