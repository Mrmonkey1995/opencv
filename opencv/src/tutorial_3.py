import numpy as np
import cv2 as cv


# 对比度和亮度
def liangAndDuibidu(image, duibidu, liangdu):
    h, w, ch = image.shape
    # imasge.dtype不写会报错
    blank = np.zeros([h, w, ch], image.dtype)
    after = cv.addWeighted(image, duibidu, blank, 1 - duibidu, liangdu)
    cv.imshow('after', after)


src = cv.imread('F:\\qing.jpg')
cv.namedWindow('input imag', cv.WINDOW_AUTOSIZE)
cv.imshow('input imag', src)
liangAndDuibidu(src, 1.5, 0)
cv.waitKey(0)
cv.destroyAllWindows()
