# coding: utf-8
# A quick & dirty IMG processing APP
import cv2
import numpy as np

# dummy function that does nothing
def dummy(value):
    pass
    

#  creating the window with opencv (windows & trackbars)
cv2.namedWindow('app')
# arguments: trackbarNamen windowName value (initial value), count(max value), onChange (event handler)
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
#  brightness, initial value=50, max value=100, event handler=dummy
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, 1, dummy) # TODO : update max value of filter
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)
# TODO: remove this line
cv2.waitKey(0) 
#  window cleanup
cv2.destroyAllWindows()
