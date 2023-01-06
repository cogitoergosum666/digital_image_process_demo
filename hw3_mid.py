from PIL import Image
import numpy as np
import random
from skimage import io
import cv2 as cv
import numpy as np
import math

def salt_and_pepper_noise(img, proportion=0.05):
    noise_img = img
    height, width = noise_img.shape[0], noise_img.shape[1]
    num = int(height * width * proportion)  # 多少个像素点添加椒盐噪声
    for i in range(num):
        w = random.randint(0, width - 1)
        h = random.randint(0, height - 1)
        if random.randint(0, 1) == 0:
            noise_img[h, w] = 0
        else:
            noise_img[h, w] = 255
    return noise_img


def median_filter(image, win=3):
    H, W, C = image.shape
    result = image.copy()
    for h in range(1, H-2):
        for w in range(1, W-2):
            for c in range(C):
                result[h, w, c] = np.median(result[h:h+win, w:w+win, c])
    return result

def midwork(imgname):
    img = cv.imread(imgname)
    #cv.imshow("original", img)
    noise_img = salt_and_pepper_noise(img)
    cv.imwrite("noise_res.jpg",noise_img)
    # cv.imshow("noise_img", noise_img)
    mid_img=median_filter(img)

    # cv.imshow("MedianFilter_img", Mean_img)
    cv.imwrite("midan_res.jpg",mid_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":

    img = cv.imread(r"E:/pythontupian/5.jpg")
    cv.imshow("original", img)
    noise_img = salt_and_pepper_noise(img)
    cv.imshow("noise_img", noise_img)
    MedianFilter_img=median_filter(img)

    cv.imshow("MedianFilter_img", MedianFilter_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

