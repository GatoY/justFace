import cv2
import numpy as np
import gorgeous
import faceDetect
import picKit
import copy

    #def switchToZero(s):
#s=0
    #img=gorgeous.gorgeous(img, faces, d)
    #cv2.imshow('image',img)
#k=cv2.waitKey(1)&0xFF
img = cv2.imread('test.jpeg')
def nothing(d):
    print d
    global img
    global gImg
    gImg=copy.copy(img)
    gImg=gorgeous.gorgeous(gImg, faces, d)
height, width =img.shape[:2]
img = picKit.resize(img,500,500*width/height)
faces = faceDetect.faceDetect(img)
gImg=copy.copy(img)
for (x,y,w,h) in faces:
    cv2.rectangle(gImg, (x-20,y-20),(x+w+20,y+h+20), (255,0,0),2)
cv2.namedWindow('image')
cv2.createTrackbar('Dermabrasion','image',2,40,nothing)
#switch='0:OFF\n1:ON'
#cv2.createTrackbar(switch,'image',0,1,switchToZero)
while(1):
    #d=cv2.getTrackbarPos('Dermabrasion','image')
    #s=cv2.getTrackbarPos(switch,'image')
    #if s==1:
    #newImg=gorgeous.gorgeous(img, faces, d)
    cv2.imshow('image',gImg)
    k=cv2.waitKey(1)&0xFF
    #    try:
    #   cv2.imshow('image',newImg)
    #   k=cv2.waitKey(1)&0xFF
    #except:
    #   cv2.imshow('image',img)
    #   k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    if k==115:
        cv2.imwrite('newImage.jpeg',gImg)
cv2.destroyAllWindows()
