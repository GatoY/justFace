# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time

def capture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    x, y= frame.shape
    while(True):
        ret, frame = cap.read()
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


capture()
