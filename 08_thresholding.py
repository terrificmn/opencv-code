import cv2

src = cv2.imread('data/images/threshold.png', 0)

# 구분하기 위한 값 설정
thresh = 0
#배경이 검은색일때 검은색에 가까운것들을 잘 안보이게 되므로 

# 위에서 설정한 값보다 큰 것들은, 모두 255로 색으로 변경하겠다는 것
maxValue = 255

cv2.imshow('Original', src)

# 2번째 파라미터는 구분하기 위한 색(배경색)을 설정
# 두번째 리턴값이 dst변수에 들어가는 것이 적용된 이미지(numpy)
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY )

cv2.imshow('Thresholded Image', dst)


cv2.waitKey()
cv2.destroyAllWindows()