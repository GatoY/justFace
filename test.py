import cv2
import gorgeous
import faceDetect
import picKit
img = cv2.imread('test.jpeg')
height, width =img.shape[:2]
img = picKit.resize(img,height/2,width/2)
faces = faceDetect.faceDetect(img)
for (x,y,w,h) in faces:
    newimg = cv2.rectangle(img, (x,y),(x+w,y+h), (255,0,0),2)
cv2.imshow('image',newimg)
cv2.waitKey()
img=gorgeous.gorgeous(img, faces)
cv2.imshow('image2',img)
cv2.waitKey()
