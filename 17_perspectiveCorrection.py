import cv2
import numpy as np
from utils import get_four_points

img_src = cv2.imread('data/images/my_test.jpg')

#행 y축, 열은 x축 헛깔림
dst_size = (400, 300, 3)

# 빈 이미지를 행렬로 만들기 zero로 (0으로 행렬만들기) 만들어준다 (검정색)
img_dst = np.zeros(dst_size, np.uint8)

cv2.imshow('dst', img_dst)

# 우리가 원본 이미지로부터는 마우스 클릭으로 4개의 가지고 옵니다.
cv2.imshow('Image', img_src)
points_src = get_four_points(img_src)

# 새로 만들 이미지에서는, 위의 원본 이미지 4개의 점과 매핑할 점을 잡아줘야한다

points_dex = np.array( [
                        0, 0,
                        dst_size[1], 0,
                        dst_size[1], dst_size[0],
                        0, dst_size[0] ], dtype=float )

points_dst = points_dex.reshape(4, 2)

h, stauts = cv2.findHomography(points_src, points_dst)

# dst_size[1]  x축   dst_size[0]  y축   #행렬을 머리속에 그려보자, 그러면 x y축이 이해가 감
img_dst = cv2.warpPerspective(img_src, h, (dst_size[1], dst_size[0]) ) 

cv2.imshow('warp', img_dst)

cv2.waitKey()
cv2.destroyAllWindows()
