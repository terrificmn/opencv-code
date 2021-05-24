import cv2 

imageName = "data/images/truth.png"

image = cv2.imread(imageName, cv2.IMREAD_COLOR)

cv2.imshow('original', image)

# 이미지 확장 dilation
dilationSize = 6
# getStructuringElement() 메소드는 2번째 파라미터는 ()튜플로 넣는다
element = cv2.getStructuringElement(cv2.MORPH_RECT, 
                            (2*dilationSize +1, 2*dilationSize+1)
                            )

imageDilate = cv2.dilate(image, element)


cv2.imshow('Dilation', imageDilate)

cv2.waitKey()
cv2.destroyAllWindows()