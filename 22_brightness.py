import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg', 1)

# 루마 채널만 변경하기 때문에 (밝기만 조절이 된다)
#beta = -100
beta = 150

# 컬러 스페이스 변경
ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# 가공을 위해서 uinit8을 float으로 변경

ycbImage = np.float32(ycbImage)

# 채널분리 Ychannel 밝기 조절부분 luma
Ychannel, Cr, Cb = cv2.split(ycbImage)

# Ychanel + beta를 더해주는데 숫자가 넘어가는것을 자동으로 255로 바꿔주는 clip메소드를 사용
# 밝기조절
Ychannel = np.clip(Ychannel + beta, 0, 255)

# 다시 채널 합친다
ycbImage = cv2.merge([Ychannel, Cr, Cb])

# int로 바꾸기
ycbImage = np.uint8(ycbImage)

# 화면에 표시하기 위해서는 컬러스페이스 BGR로 변경
ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

# 이미지를 각각의 윈도우에 표시
# cv2.imshow('src', img)
# cv2.imshow('dst', ycbImage)

# 하나의 윈도우에 2개의 이미지를 옆으로 (수평으로 ) 붙여서 표시
# 이미지가 행렬이므로 옆으로 붙이면 된다 
imgCombined = np.hstack( [img, ycbImage]) 
cv2.imshow('combined', imgCombined)


cv2.waitKey()
cv2.destroyAllWindows()



