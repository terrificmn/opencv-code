import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg', 1)

gamma = 2.5

fullRange = np.arange(0, 256) #마지막포함안함 255까지

# 감마 보정에 의한 공식 대입
lookupTable = np.uint8( 255 * np.power( (fullRange / 255.0), gamma ))

output = cv2.LUT(img, lookupTable)

combinedImg = np.hstack( [img, output])

# 실제로는 우리눈은 리니어하게 보지 않기 때문에 오른쪽 화면에 가깝게 보이게 된다고 함
# 디지털 카메라는 linear하게 구분을 하기때문에 검은색과 밝은 부분을 구별한다
cv2.imshow('combined', combinedImg)

cv2.waitKey()
cv2.destroyAllWindows()