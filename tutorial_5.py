import cv2 as cv
import numpy as np


# 泛洪填充
def fill_color_demo(image):
    copyImage = image.copy()
    h, w = copyImage.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)
    cv.floodFill(copyImage, mask, (30, 30), (300, 300, 300), (100, 100, 100), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('flood', copyImage)

#二值填充
def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow('binary', image)
    mask = np.ones([402, 402, 1], np.uint8) #ones,+2
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)


src = cv.imread('F:\\qing.jpg')
cv.namedWindow('input imag', cv.WINDOW_AUTOSIZE)
cv.imshow('input imag', src)

fill = fill_color_demo(src)

# face = src[200:650, 150:550]
# gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
# backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
# src[200:650, 150:550] = backface
# cv.imshow('face', src)

cv.waitKey(0)
cv.destroyAllWindows()
