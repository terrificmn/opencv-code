# 이미지를 부드럽게 해주는 필터

import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png')

# GaussianBlur() 내부적으로 커널을 사용해서 컨볼루션을 알아서 해줌
# 종모양을 생각하자

# sigmaX 가 필요 표준편차
# 3x3 커널 사용할 때, ( , )
# 마지막 파라미터는 표준편차를 의미 (sigma)
# (커널사이즈는 홀수로 많이 사용)
dst1 = cv2.GaussianBlur(img, (5, 5), 1)

# 7x7 커널 사용할 때
dst2 = cv2.GaussianBlur(img, (25, 25), 10)

combined = np.hstack([img, dst1, dst2])
cv2.imshow('combined_Image', combined)

cv2.waitKey()
cv2.destroyAllWindows()