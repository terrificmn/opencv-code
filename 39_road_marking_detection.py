import cv2
import numpy as np

# 칼라 이미지
image_color = cv2.imread('data2/image.JPG')
cv2.imshow('origin', image_color)

# 우리가 필요한 건 그레이 스케일
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', image_gray)

image_copy = image_gray.copy()

# 값이 195 미만인 것들은 , 0으로 셋팅
print(image_color.shape)
# 그레이 스케일은 2차원인 것을 알 수 있다
print(image_copy.shape)

# 195 미만인 값들을 0으로 바꿔주기
image_copy[ image_copy[:, :] < 195 ]  = 0
# 바뀐 값들 출력
cv2.imshow('copy', image_copy)




cv2.waitKey()
cv2.destroyAllWindows()

