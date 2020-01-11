import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

while True:
    ret, frame, = cap.read()
    if ret == True:
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv.destroyAllWindows()