import cv2 as cv
import numpy as np


# 均值模糊
def blur_demo(image):
    dst = cv.blur(image, (5, 5))  # 可以通过（1,3）设置水平方向和竖直方向的模糊
    cv.imshow('blur_demo', dst)


# 中值模糊
def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)  # 去黑白噪声
    cv.imshow('blur_demo', dst)


# 用户自定义模糊
def costom_blur(image):
    # kernel = np.ones([5, 5], np.float32) / 25
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [-1, 0, 0]], np.float32)#总和为1，做增强（锐化）
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow('costom', dst)


src = cv.imread('F:\\qing.jpg')
cv.namedWindow('input imag', cv.WINDOW_AUTOSIZE)
cv.imshow('input imag', src)
blur_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
