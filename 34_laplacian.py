import cv2
import numpy as np

img = cv2.imread('data/images/truth.png', 1)

# sobel방식과는 다르게 
#미분에 2차 미분까지 수행을 해서 한 laplacian 수학자의 이름

laplacian = cv2.Laplacian(img, cv2.CV_32F, ksize=3, scale=1)

cv2.imshow('original', img)
cv2.imshow('laplacian', laplacian)

cv2.waitKey()
cv2.destroyAllWindows()