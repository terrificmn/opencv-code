import cv2

source = cv2.imread('data/images/sample.jpg', 1) 
#source = cv2.imread('data/images/my_book.jpg', 1) 
#1 은 color, 상수로 되어있어서 대문자 IMREAD_COLOR
#2 는 grayscale

cv2.imshow('Original', source)

# 1은 100%, 0.6 60%, 1.8 은 180% 확대 / 축소 가능
scaleX = 0.6
scaleY = 0.6

scaleDown = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)
# cv2.INTER_LINEAR 말고도 많이 있음 resize()함수에 대해서 검색해보면 나옴
#interpolation은 사진을 확대하면 중간 부분이 픽셀이 없어지는데 이 값들을 linear하게 선형으로 
# 메꾸는 방법이다

cv2.imshow('Original', source)
cv2.imshow('Scaled Down', scaleDown)


scaleX = 1.8
scaleY = 1.8

scaleUp = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

cv2.imshow('ScleUP', scaleUp)

# 내가 원하는 부분의 이미지를 가져오기
# numpy array이므로 슬라이싱으로 가져올 수 있다
crop_img = source [ 100 : 200, 150: 250]
# 아래처럼 하면 안된다
crop_img2 = source [ 10 : 200, 150: 250]
# 행은 y축이 되는 것에 주의

cv2.imshow('Cropped Img', crop_img)
cv2.imshow('Cropped Img2', crop_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


