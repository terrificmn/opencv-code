import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')

cv2.imshow('img', image)

# 선 그리기 
# 카피해서 사용하자. 
imageLine = image.copy()

#cv2.line()메소드
# 1st param: numpy이미지, 
# 2nd param: 시작점 (행렬)
# 3 param: 끝점 (행렬))
# 4th param: B G R 로 처리한다 
# 기타 파라미터들은 thickness=, lineType= 등 
cv2.line(imageLine, (322, 179), (400, 183), (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow('image line', imageLine)

# 원 그리기
imageCicle = image.copy()
# 원의 중심을 행렬로 표시하고, 150만큼 원을 그림
cv2.circle(imageCicle, (350, 200), 150, (255, 0, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow('image circle', imageCicle)

# 타원 그리기
imageEllipse = image.copy()

cv2.ellipse(imageEllipse, (360, 200), (100, 170), 45, 0, 360, (0, 255, 0), thickness=2)
cv2.ellipse(imageEllipse, (360, 200), (100, 170), 135, 0, 360, (0, 0, 255), thickness=2)
cv2.imshow('image ellipse', imageEllipse)


# 사각형 그리기
# 파라미터는 시작점, 끝점, 색(BGR)
imageRectangle = image.copy()
cv2.rectangle(imageRectangle, (208,55), (450,355), (255, 0, 0), thickness=3)
cv2.imshow('rectangle', imageRectangle)


# 글자 넣기
imageText = image.copy()
cv2.putText(imageText, 'Mark Zuckerberg', (205, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('text', imageText)


imageTextRectangle = image.copy()
cv2.rectangle(imageTextRectangle, (208,55), (450,355), (255, 0, 0), thickness=3)
cv2.putText(imageTextRectangle, 'Mark Zuckerberg', (205, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('complex', imageTextRectangle)



cv2.waitKey()
cv2.destroyAllWindows()
