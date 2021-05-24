import cv2
import numpy as np

# canny edge를 사용할 때는 gray scale를 이용
img = cv2.imread('data/images/sample.jpg', 0)

cv2.imshow('canny_gray_scale', img)

threshold_1 = 150 # high : 0~255 중에 설정

threshold_2 = 90 # low

result = cv2.Canny(img, threshold_1, threshold_2)
cv2.imshow('canny', result)

cv2.waitKey()
cv2.destroyAllWindows()