import cv2
import numpy as np

# Region of interest masking
# ROI (관심 영역)
image_color = cv2.imread('data2/test5.jpg')

image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

#cv2.imshow('GRAY', image_gray)

print(image_gray.shape)

# np.zeros 함수는 파라미터로, 몇행 몇열로 만들지 넣어줘야한다. 
# 0 인 검정색 화면을 만들어 준다음에 포인트 4개를 찍어서 흰색으로 바꿔주기위한 작업
#blank = np.zeros( (image_gray.shape[0], image_gray.shape[1]) )

# np 에서 더 쉬운 함수를 제공하는데 shape속성을 사용할 필요없이 이미지 사이즈로 똑같이 만들어 준다
blank = np.zeros_like(image_gray)

print(blank.shape)

# 2차원으로 만들어 준다
ROI = np.array( [ [ (0, 400), (300, 250), (450, 300), (700, 426) ] ], dtype= np.int32)

mask = cv2.fillPoly(blank, ROI, 255)

print(mask)
cv2.imshow('mask', mask)

# 비트 와이즈 앤드 연산을 한다 (비트 단위로 연산)
masked_image = cv2.bitwise_and(image_gray, mask)
cv2.imshow('img', masked_image)
#cv2.imshow('masked_image', masked_image)

#cv2.imshow('BLANK', blank)


# hough transform (canny 엣지로 선을 찾은 것을 라인을 이어준다)
image_c = cv2.imread('data2/calendar.jpg')
image_g = cv2.cvtColor(image_c, cv2.COLOR_BGR2GRAY)

image_canny = cv2.Canny(image_g, 50, 200, apertureSize=3)  # apertureSize=대개 3, 5, 7 한다고 함

lines = cv2.HoughLines(image_canny, 1, np.pi / 180, 250)

cv2.imshow('Canny', image_canny)

for i in range(len(lines)) :
    for rho,theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(image_c, (x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('canny', image_c)

cv2.waitKey()
cv2.destroyAllWindows()