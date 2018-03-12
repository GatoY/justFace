import cv2
import numpy as np
import picKit
import copy
def canny(img):

#img=cv2.imread('test.jpeg',0)
#img = picKit.resize(img,500, img.shape[1]*500/img.shape[0])
    edges = cv2.Canny(img, 100, 200) #get the edges by Canny.
#cv2.imshow('image',img)
#cv2.waitKey()
#cv2.imshow('edges',edges)
#   cv2.waitKey()

    return edges

