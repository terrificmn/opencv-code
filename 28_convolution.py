import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png')

#cv2.imshow('origin', img)

# 커널사이즈는 행렬이 같은거로 만들기 때문에 
kernel_size = 5

# 1로 만드는 함수
# 1로 곱하게 되면 255가 (5x5이므로 255를 쉽게 넘어버림) 넘기 대문에 흰색으로 표시되게 된다
kernel = np.ones ( (kernel_size, kernel_size )) / kernel_size **2 

print(kernel)

# 컨볼루션 cv2.filter2D 함수
result = cv2.filter2D(img, -1, kernel)

print(result)
combined = np.vstack([img, result])
cv2.imshow('v_combined', combined)




cv2.waitKey()
cv2.destroyAllWindows()