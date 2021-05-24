import cv2

imageName = 'data/images/sample.jpg'

image = cv2.imread(imageName, cv2.IMREAD_COLOR) # color로 읽음
#grayImage = cv2.imread(imageName, 0) # cv2.IMREAD_COLOR는 const임
# 숫자들이 정의 되어 있는 거라서 0은 gray, 1은 color == IMREAD_COLOR

if image is None:
    print('Could not open or find the image')

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 창에 이름과 성질을 설정
cv2.namedWindow('gray image', cv2.WINDOW_AUTOSIZE)

# 위에서 설정한 창 gray image 에다 , numpy인 grayImage를 표현
cv2.imshow('gray image', grayImage)

# imshow()는 쥬피터 노트북에서 에러가 난다. (plt.imshow()를 사용해야한다 )
# 코랩에서도 충돌이 난다

# 작업한 이미지를 파일로 저장하는 코드
#cv2.imwrite('data/result_gray.jpg', grayImage)

cv2.waitKey(0) # 0은 아무키나 입력받음
cv2.destroyAllWindows()

