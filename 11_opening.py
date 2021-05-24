import cv2

imageName = 'data/images/opening.png'

image = cv2.imread(imageName, 0)

cv2.imshow('original', image)

#Opening이란 
openingSize = 3

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                    (2*openingSize+1, 2*openingSize+1) )

#iterations= 파라미터로 반복되는 것 지정해줌
imageOpened = cv2.morphologyEx(image, cv2.MORPH_OPEN, element, iterations=2)

cv2.imshow('Opened Image', imageOpened)

cv2.waitKey()
cv2.destroyAllWindows()