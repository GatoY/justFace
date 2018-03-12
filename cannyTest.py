import cv2
import gorgeous
import faceDetect
import picKit
import edge
import copy
img = cv2.imread('test.jpeg')
height, width =img.shape[:2]
img = picKit.resize(img,500,width*500/height)
faces = faceDetect.faceDetect(img)
newimg=copy.copy(img)
for (x,y,w,h) in faces:
    newimg = cv2.rectangle(newimg, (x,y),(x+w,y+h), (255,0,0),2)
    edgeImage = edge.canny(img[(y-20):(y+h+20),(x-20):(x+w+20)])
    image, contours, hierarchy = cv2.findContours(copy.copy(edgeImage), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image=cv2.drawContours(edgeImage, contours, 1, (255,255,255), 3)
    cv2.imshow('edges',image)
    cv2.waitKey()

cv2.imshow('image',newimg)
cv2.waitKey()
img=gorgeous.gorgeous(img, faces,8)
cv2.imshow('image2',img)
cv2.waitKey()
