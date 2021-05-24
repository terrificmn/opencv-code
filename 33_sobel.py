import cv2
import numpy as np

img = cv2.imread('data/images/truth.png')

# sobel함수의 파라미터는 (src, ddepth, dx, dy, ksize)
# ddepth의 CV_8U, CV_16U, CV_32F, CV_64F 가 있고, 이미지값을 각각 uint8, uint16, float32, float64로 설정
# dx, dy는 x방향, y방향으로 미분을 찾는 것
# 1, 0 이면 x축으로 찾겠다는 것
sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0)  

# 0, 1 이면 y축으로 
sobely = cv2.Sobel(img, cv2.CV_32F, 0, 1)  

# 소벨 방식은 흰색에서 검정색은 잘 못찾는 듯

cv2.imshow('image', img)

cv2.imshow('sobel X', sobelx)

cv2.imshow('sobel Y', sobely)

cv2.waitKey()
cv2.destroyAllWindows()