

from PIL import Image
import numpy as np
import random
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


def mean_filter(image):
    K = ([1, 1, 1],
         [1, 1, 1],
         [1, 1, 1])
    K = np.array(K)
    H, W, C = image.shape
    result = image.copy()
    # 因为卷积核是以左上角为定位，所以遍历时最后要停到H-2处
    for h in range(1, H-2):
        for w in range(1, W-2):
            for c in range(C):
                result[h, w, c] = sum(sum(K * result[h:h+K.shape[0], w:w+K.shape[1], c])) // 9
    return result


def meanwork(imgname):
    img = cv.imread(imgname)
    #cv.imshow("original", img)
    noise_img = salt_and_pepper_noise(img)
    cv.imwrite("noise_res.jpg",noise_img)
    # cv.imshow("noise_img", noise_img)
    Mean_img=mean_filter(img)

    # cv.imshow("MedianFilter_img", Mean_img)
    cv.imwrite("mean_res.jpg",Mean_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


    

if __name__ == "__main__":

    img = cv.imread(r"hw2_picture1.jpg")
    cv.imshow("original", img)
    noise_img = salt_and_pepper_noise(img)
    cv.imshow("noise_img", noise_img)
    Mean_img=mean_filter(img)

    cv.imshow("MedianFilter_img", Mean_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


