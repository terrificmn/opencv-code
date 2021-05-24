import cv2
import numpy as np
from numpy.lib.histograms import _histogram_bin_edges_dispatcher

source = cv2.imread('data/images/sample.jpg', 0)  #0흑백, 1칼러

scalingFactor = 1 /255.0

# Convert unsigned int (8bit) to float
# opencv에서 사진을 불러와서 학습이 필요한 경우에 변환해주기 (feature scaling이 필요한 경우)


source = np.float32(source)  # np을 이용해서 float32로 바꿔주기

source = source * scalingFactor
print(source)


# convert back to unsigned int (8bit)
source = source * (1.0 / scalingFactor)  # 다시 255를 곱한 셈
source = np.uint8(source)
print(source)

# opencv에서 처리하는 방식
# BGR

