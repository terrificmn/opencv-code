import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg')

# intensity Scaling
# scaleFactor를 조절해서 밝기를 조절할 수 있음
scaleFactor = 2.5

ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

ycbImage = ycbImage.astype('float')

ychannel, Cr, Cb = cv2.split(ycbImage)

ychannel = np.clip( ychannel * scaleFactor, 0, 255)

ycbImage = cv2.merge([ychannel, Cr, Cb])

ycbImage = np.uint8(ycbImage) #unsigned int 8bit로 다시 변환

ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

combinedImg = np.hstack( [img, ycbImage])

cv2.imshow('combined', combinedImg)

cv2.waitKey()
cv2.destroyAllWindows()



