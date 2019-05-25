# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:55:45 2019

@author: Varun
"""

import sys
import cv2
imagePath="C:\\Users\\admin\\Pictures\\Screenshots\\v.jpg"
casc_path="E:\\opencv-3.4.6\\data\\haarcascades\\haarcascade_frontalface_default.xml"
# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
