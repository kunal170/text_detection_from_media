import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\tesseract.exe'
img = cv2.imread('image.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_hgt, img_wdt, _ = img.shape
boxes = pytesseract.image_to_data(img)
print(boxes)
for count, line in enumerate(boxes.splitlines()):
     if count != 0:
         line = line.split()
         print(line)
         if len(line) == 12:
             x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
             cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 255), 1)
             cv2.putText(img, line[11], (x, y), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
             print(line[11],end =" ")

cv2.imshow('img', img,)
cv2.waitKey(0)