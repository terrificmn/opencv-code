import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg')

ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

Ychannel, Cr, Cb = cv2.split(ycbImage)

print(Ychannel)

# equalizeHist()메소드가 자동으로 만들어 줌
Ychannel = cv2.equalizeHist(Ychannel)

# 전 후 비교
print(Ychannel)

ycbImage = cv2.merge( [Ychannel, Cr, Cb ])

ycbImage = cv2.cvtColor (ycbImage, cv2.COLOR_YCrCb2BGR)

combinedImg = np.hstack( [img, ycbImage] )

cv2.imshow("combined", combinedImg )

cv2.waitKey()
cv2.destroyAllWindows()
