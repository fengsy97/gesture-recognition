import cv2
import os
import numpy as np
filePath = "./give_set/stone/"

def cr_otsu(image):
    """YCrCb颜色空间的Cr分量+Otsu阈值分割
    :param image: 图片路径
    :return: None
    """
    img = cv2.imread(filePath+image, cv2.IMREAD_COLOR)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
 
    (y, cr, cb) = cv2.split(ycrcb)
    cr1 = cv2.GaussianBlur(cr, (5, 5), 0)
    _, skin = cv2.threshold(cr1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
 
    # cv2.namedWindow("image raw", cv2.WINDOW_NORMAL)
    # cv2.imshow("image raw", img)
    # cv2.namedWindow("image CR", cv2.WINDOW_NORMAL)
    # cv2.imshow("image CR", cr1)
    # cv2.namedWindow("Skin Cr+OTSU", cv2.WINDOW_NORMAL)
    # cv2.imshow("Skin Cr+OTSU", skin)
 
    dst = cv2.bitwise_and(img, img, mask=skin)
    # cv2.namedWindow("seperate", cv2.WINDOW_NORMAL)
    # cv2.imshow("seperate", dst)
    cv2.imwrite('./stone/'+image, dst)
    # cv2.waitKey()

# cr_otsu("015.jpg")

names =os.listdir(filePath)
# print(names)
for name in names:
    cr_otsu(name)
# for i,j,k in os.walk(filePath):