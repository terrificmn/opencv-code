import cv2
import numpy as np
from utils import get_four_points

img_src = cv2.imread('data/images/first-image.jpg', 1)
img_dst = cv2.imread('data/images/times-square.jpg', 1)

#des_size를 변형할 이미지의 크기로 가져온다
dst_size = img_dst.shape


# 우리가 원본 이미지로부터는 이미지 포인트를 바로 가져올 수 있다. 
# get_four_points 포인트를 가져오는 사용자 함수를 사용할 필요가 없다
cv2.imshow('Source Image', img_src)

# 시계 방향으로 점을 가져온다, 정사각형이므로 좌표를 찍을 수 있다
points_src = np.array( [ 0, 0, 
                        img_src.shape[1], 0,
                        img_src.shape[1], img_src.shape[0],
                        0, img_src.shape[0]
])
points_src = points_src.reshape(4, 2)

# 새로 만들 이미지에서는, 위의 원본 이미지 4개의 점과 매핑할 점을 잡아줘야한다
# 좌표를 알 수 없으므로 마우스를 눌러서 찍어야함
points_dst = get_four_points(img_dst)

# h가 3행 X 3열 행렬임
h, stauts = cv2.findHomography(points_src, points_dst)

# dst_size[1]  x축   dst_size[0]  y축   #행렬을 머리속에 그려보자, 그러면 x y축이 이해가 감
img_warp_temp = cv2.warpPerspective(img_src, h, (dst_size[1], dst_size[0]) ) 

cv2.imshow('warpPerspective', img_warp_temp)

# 이제 점이 찍은 다음이므로 타임스퀘어 이미지를 간판을 검정색으로 바꾼다 0
# fillConvexRoly() 에서 2번째 파라미터 포인트는 int로 바꿔서 넣어줘야한다. points_dst는 float
blackedImg = cv2.fillConvexPoly(img_dst, points_dst.astype(int), 0)

# 이렇게 하면 간판만 검은색 화면으로 볼 수 있다
cv2.imshow('Img to 0', blackedImg)

img_result = img_dst + img_warp_temp

cv2.imshow('image complete', img_result)

cv2.waitKey()
cv2.destroyAllWindows()
