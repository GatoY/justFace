import cv2
import faceDetect
import copy
def gorgeous(img,faces, d):
    newImg = copy.copy(img)

    for (x,y,w,h) in faces:
        newImg[y:(y+h),x:(x+w)]=cv2.bilateralFilter(newImg[y:(y+h),x:(x+w)],d,75,75)
    return newImg
