import cv2
import numpy as np

img = cv2.imread('data/images/mountain.jpeg')


sharpen = np.array( [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0] 
    ], dtype='int')

# 이미지의 색깔을 커널(필터)를 이용해서 이미지 크기가 더 커진다

result = cv2.filter2D(img, -1, sharpen)

cv2.imshow('original', img)
cv2.imshow('result-sharpen', result)

cv2.waitKey()
cv2.destroyAllWindows()