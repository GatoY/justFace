import cv2
import faceDetect
def gorgeous(img,faces):
    for (x,y,w,h) in faces:
        img[x:(x+w), y:(y+h)]=cv2.bilateralFilter(img[x:(x+w), y:(y+h)],5,75,75)
    return img
