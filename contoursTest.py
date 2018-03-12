import cv2
import gorgeous
import faceDetect
import picKit
import edge
import copy
img = cv2.imread('test.jpeg')
height, width =img.shape[:2]
img = picKit.resize(img,500,width*500/height)
edges = edge.canny(img)
cv2.imshow('image',edges)
cv2.waitKey()
