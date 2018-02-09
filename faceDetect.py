import numpy as numpy
import cv2
def faceDetect(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)
        #for (x,y,w,h) in faces:
        #img = cv2.rectangle(img, (x,y),(x+w,y+h), (255,0,0),2)
        #img=cv2.resize(img,(800,800), interpolation=cv2.INTER_AREA)
    return faces
