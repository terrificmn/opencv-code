import cv2 
import numpy as np

original = cv2.imread('data/images/girl.jpg')
img = original.copy()

# x 축 피봇 포인트
originalValue = np.array([0, 50, 100, 150, 200, 255])

# y축 포인트 : 빨간쪽, 파란쪽 두 부분의 포인트
rCurve = np.array([0, 80, 150, 190, 220, 255])

bCurve = np.array([0, 20, 40, 75, 150, 255])

# Lookup 테이블 만들기

fullrange = np.arange(0, 255+1)
rLUT = np.interp(fullrange, originalValue, rCurve)
bLUT = np.interp(fullrange, originalValue, bCurve)

print(rLUT)
print(rLUT.shape)

# 빨간색만 가져오기 --- B, G, R 에서 이미지가 3차원으로 되어 있기 때문에 3번째 [2]의 가져오면 red 

rChannel = img[ :, :, 2]
# B, G, rChannel = cv2.split(img)

rChannel = cv2.LUT(rChannel, rLUT)

img[ :, :, 2] = rChannel

# B G R, 순서이므로 3차원의 0번째가 Blue 채널
bChannel = img[ :, :, 0]
bChannel = cv2.LUT(bChannel, bLUT)

img[:, :, 0] = bChannel

# 화면표시

combined = np.hstack([original, img])
cv2.imshow('combined', combined)


cv2.waitKey()
cv2.destroyAllWindows()



