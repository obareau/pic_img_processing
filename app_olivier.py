# coding: utf-8
# A quick & dirty IMG processing APP
import cv2
import numpy as np

# dummy function that does nothing
def dummy(value):
    pass

# Read ahead a image & make a grayscale copy
color_original = cv2.imread('test.jpg')
gray_original  = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)  
#  creating the window with opencv (windows & trackbars)
cv2.namedWindow('app')
# arguments: trackbarNamen windowName value (initial value), count(max value), onChange (event handler)
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
#  brightness, initial value=50, max value=100, event handler=dummy
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, 1, dummy) # TODO : update max value of filter
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

# Main UI loop
while True:
    # TODO : read all of the trackbars values
    grayscale = cv2.getTrackbarPos('grayscale', 'app')
    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    # TODO : apply the filters
    # Apply the brightness and contrast
    color_modified = cv2.addWeighted(color_original, contrast, np.zeros_like(color_original), 0, brightness - 50)
    gray_modified = cv2.addWeighted(gray_original, contrast, np.zeros_like(gray_original), 0, brightness - 50)
    
    # wait for keypress 100 milliseconds
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    elif key == ord('s'):
        # TODO : save image
        pass
    # show the image
    if grayscale == 0:
        cv2.imshow('app', color_modified)
    else:
        cv2.imshow('app', gray_modified)

#  window cleanup
cv2.destroyAllWindows()
