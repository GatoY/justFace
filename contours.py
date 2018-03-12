import cv2
import picKit
import numpy as np
import edge
np.set_printoptions(threshold=np.inf)
img =cv2.imread('test.jpeg')
height, width =img.shape[:2]
img = picKit.resize(img,500,width*500/height)
img = edge.canny(img)
image, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow('im',contours)
#cv2.waitKey()
print contours
