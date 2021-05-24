import cv2
import numpy as np

image = cv2.imread('data2/test_image.JPG')
print('Height = ', int(image.shape[0]), 'pixels')
print('Width = ', int(image.shape[1]), 'pixels')

#cv2.imshow('Self Driving Car!', image )

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('SDC Gray', gray_img)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# imshow()는 BGR로 보여주기 때문에 HSV로 하면 이상하게 나옴
#cv2.imshow('HSV', hsv_image)

# Hue 채널만 표시
H, S, V = cv2.split(hsv_image)

# 또는 numpy array로 가져오기  (마지막의 차원의 0번째만 가져오면 됨)
# H = hsv_image[: ,: ,0 ]

#cv2.imshow('Hue', H)


# 갭 차이가 커질 수록 더 선명하게 된다
sharp_kernel_1 = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# 위의 커널을 그레이 이미지에 컨볼루션 한다
sharpened_img_1 = cv2.filter2D(gray_img, -1, sharp_kernel_1)
#cv2.imshow('Gray', gray_img)
#cv2.imshow('sharpened_img_1', sharpened_img_1)


sharp_kernel_2 = np.array([
    [0, -1, 0],
    [-1, 9, -1],
    [0, -1, 0]
])

# 마찬가지로 컨볼루션 해준다
sharpened_img_2 = cv2.filter2D(gray_img, -1, sharp_kernel_2)
#cv2.imshow('Sharpened_img_2', sharpened_img_2)

# Blurring
# 가우시안 블러 처리하기 (커널사이즈는 홀수로 많이 사용)
blur_img = cv2.GaussianBlur(gray_img, (5, 5), 1)
#cv2.imshow('Blur', blur_img)


# Sobel을 이용한 edge detection
# 우선 x 수평부분을 잡는다
x_sobel = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize= 7)
#cv2.imshow('Sobel_X', x_sobel)

# 수직을 
y_sobel = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize= 7)
#cv2.imshow('Sobel_Y', y_sobel)

# 라플라시안은 한번에 수직 수평 다 잡는다, 단 노이즈 부분도 다 잡아냄
laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)
#cv2.imshow('Laplacian', laplacian)

# 그래서 더 좋은 게 Canny edge, low_threshold 와 high_threshold 값을 설정해준다
low_threshold = 120
high_threshold = 200

canny_img = cv2.Canny(gray_img, low_threshold, high_threshold)
#cv2.imshow("Canny Edge", canny_img)


# transformation
image = cv2.imread('data2/test_image2.JPG')
#cv2.imshow('origin', image)

print(image.shape)


# affine, 아파인 평행이 유지가 되면서 변형이 됨, 
# 이미지의 컬럼이 x가 [1]된다 | | | | ... | 이런식으로 되어 있으므로 
# 이미지의 row가 y가 [0]된다  - - - - - - ...---- 이런식이므로 0번째가 row(행)
# 어쨋든 행과 열을 각각 2로 나누면 센터값이 된다
M_rotation = cv2.getRotationMatrix2D( ( image.shape[1] / 2, image.shape[0] /2 ), 90, 0.5 )
rotated_img = cv2.warpAffine(image, M_rotation, (image.shape[1], image.shape[0] ))

#cv2.imshow('rotated_img', rotated_img)

image = cv2.imread('data2/test_image3.JPG')
cv2.imshow('origin', image)

height = image.shape[0]
width = image.shape[1]

# identity 행렬, 1, 0, 
# identity 행렬, 0, 1
# 은 그대로 두고 마지막 배열만 바꾸면 이동이 된다
T_matrix = np.array( [
    [1, 0, 120],
    [0, 1, -150]
], dtype='float32')

print(T_matrix)

# 이동
translation_image = cv2.warpAffine(image, T_matrix, (width, height))
cv2.imshow('translation', translation_image)


# Resizing
resized_img = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized_image', resized_img)


