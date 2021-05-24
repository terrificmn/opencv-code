import cv2
import numpy as np

img = cv2.imread('data/images/sample.jpg', 1)

cv2.imshow('color', img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', gray_img)


# hsv는 채도 명도
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# BGR로만 되어 있는 것만 표현하기 때문에 hsv로 변환하면 이미지가 이상하게 나옴
cv2.imshow('hsv', hsv_img)

# h는 hue, hsv_img[0]
hsv_img[2] = hsv_img[2] - 200

bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
cv2.imshow('bgr_img', bgr_img)

# hsv_img[0]
# print(hsv_img)

cv2.waitKey()
cv2.destroyAllWindows()