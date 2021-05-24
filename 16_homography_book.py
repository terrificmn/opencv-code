import cv2
import numpy as np

image_src = cv2.imread('data/images/book2.jpg', 1)

# 4개의 점을 어레이로 만든다 (단, dtype=float 으로 만들어준다) (또는 np.float도 가능) 
# 1차원으로 만든 후에 reshape 한다
point_src = np.array( [ 141, 131, 480, 159, 493, 630, 64, 601], dtype=float )

point_src = point_src.reshape(4, 2)

print(point_src)

image_dst = cv2.imread('data/images/book1.jpg')

# 위의 point_src 와 매칭시킨다
point_dst = np.array( [ 318, 256, 534, 372, 316, 670, 73, 473], dtype=float)

point_dst = point_dst.reshape(4,2)

print(point_dst)

# 위의 point_src 와 변경시킬 point_dst를 매칭시킨 것을 findHomography() 메소드를 사용해서
# 변환에 사용할 행렬을 만들어 준다
# h가 바로, 변환에 사용된 3X3 행렬이다
h, status = cv2.findHomography(point_src, point_dst)

# warpPerspective()에는 소스이미지,
# 정확하지 않음 알아봐야함;; 정확히 이해 못함 ; ㅠ변환시킬이미지의 해상도 [1]번째가 x축, [0]번째가 y축이된다
image_out = cv2.warpPerspective(image_src, h, (image_dst.shape[1], image_dst.shape[0]))

cv2.imshow('Source', image_src)
cv2.imshow('Destination', image_dst)
cv2.imshow('Warp', image_out)

cv2.waitKey()
cv2.destroyAllWindows()