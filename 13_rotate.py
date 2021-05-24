import cv2

source = cv2.imread('data/images/sample.jpg',1)

# 회전의 중심 좌표
#center = ( source.shape[1] / 2, source.shape[0] / 2)
# 행에 2를 나누고 , 열에서 2를 나누면 중간 값이 되는데 이 행렬로 가져오면 정중앙이 됨

center = ( 200, 200)
rotationAngle = 30
#rotationAngle = 90
scaleFactor = 1

# 행렬과 백터로 되어 있는 수학공식에 의해서 만들어진 함수
rotationMatrix = cv2.getRotationMatrix2D( center, rotationAngle, scaleFactor)

print(rotationMatrix)

result = cv2.warpAffine(source, rotationMatrix, (source.shape[1], source.shape[0]) )

cv2.imshow('original Image', source)
cv2.imshow('Rotated Image', result)

cv2.waitKey()
cv2.destroyAllWindows()


