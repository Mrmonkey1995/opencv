import cv2 as cv
import numpy as np


def access_pixels(image, flag):
    if flag == 0:
        print(image.shape)
        height = image.shape[0]
        width = image.shape[1]
        channels = image.shape[2]
        print('width : %s ,height : %s ,channels : %s ' % (width, height, channels))
        for row in range(height):
            for col in range(width):
                for ch in range(channels):
                    pv = image[row, col, ch]
                    image[row, col, ch] = 255 - pv
        cv.imshow('pixels_demo', image)
    elif flag == 1:
        # 图像取反
        image = cv.bitwise_not(image)
        cv.imshow('reverse', image)


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


def create_image():
    '''
    img = np.zeros([400, 400, 3])
    img[:, :, 0] = np.ones([400, 400]) * 255
    cv.imshow('create_image', img)
    '''
    img = np.zeros([400, 400, 1])
    img = img * 0
    cv.imshow('255', img)


def video_demo():
    capture = cv.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if c == 27:
            break


src = cv.imread('F:\\qing.jpg')
cv.namedWindow('input imag', cv.WINDOW_AUTOSIZE)
cv.imshow('input imag', src)

# create_image()

# gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# cv.imwrite('F:\\gray.jpg', gray)
# get_image_info(src)


'''
改变图片样式
'''
t1 = cv.getTickCount()
access_pixels(src,1)
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency()
print('time : %s ms' % (time * 1000))

# video_demo()


cv.waitKey(0)
cv.destroyAllWindows()
