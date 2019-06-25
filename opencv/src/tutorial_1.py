import numpy as np
import cv2 as cv


def extract_object_demo():
    capture = cv.VideoCapture('F:\\green.mp4')
    while (True):
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        low_hsv = np.array([35, 43, 46])
        heigh_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, low_hsv, heigh_hsv)
        dst = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('origin', frame)
        cv.imshow('mask', dst)
        c = cv.waitKey(40)
        if c == 27:
            break


# src = cv.imread('F:\\qing.jpg')
# cv.namedWindow('input imag', cv.WINDOW_AUTOSIZE)
# cv.imshow('input imag', src)
extract_object_demo()

# b, g, r = cv.split(src)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)
# src[:, :, 2] = 0
# cv.imshow('change', src)
cv.waitKey(0)
cv.destroyAllWindows()
