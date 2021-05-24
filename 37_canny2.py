import cv2
import numpy as np

highThreshold = 100
lowThreshold = 50

maxThreshold = 1000

apertureSizes = [3, 5, 7]
maxapertureIndex = 2 #위의 배열에서 가장 큰 인덱스
apertureIndex = 0 #위의 배열에서 처음 인덱스

blurAmount = 0
maxBlurAmount = 20

# 트랙바용 함수
# canny edge 적용하는 함수
def applyCanny() :
    if blurAmount >= 0 :
        # 가우시안 블러를 적용해준다
        blurredSrc = cv2.GaussianBlur(src, (2*blurAmount +1, 2*blurAmount+1), 0 )
    else:
        blurredSrc = src.copy()

    apertureSize = apertureSizes[apertureIndex]

    edges = cv2.Canny(blurredSrc, lowThreshold, highThreshold, apertureSize = apertureSize)

    cv2.imshow('Edges', edges)

# 로우 쓰레숄드 적용하는 함수
def updateLowThreshold(*args) :
    global lowThreshold
    lowThreshold = args[0]
    applyCanny()

# 하이 쓰레숄드 적용하는 함수
def updateHighThreshold(*args) :
    global highThreshold
    highThreshold = args[0]
    applyCanny()

# 블러 적용하는 함수
def updateBlurAmount(*args) :
    global blurAmount
    blurAmount = args[0]
    applyCanny()

# aperture 적용하는 함수
def updateApertureIndex(*args):
    global apertureIndex
    apertureIndex = args[0]
    applyCanny()

src = cv2.imread('data/images/sample.jpg', 0)

edges = src.copy()

cv2.imshow('Edges', src)

# namedWindow()에 이름을 해주면 계속 재활용 할 수 있다. 
cv2.namedWindow('Edges', cv2.WINDOW_AUTOSIZE)

# 로우 쓰레숄드에 대한 컨트롤러를 트랙바를 붙인다.
cv2.createTrackbar('Low Threshold', 'Edges', lowThreshold, maxThreshold, updateLowThreshold )

# 하이 쓰레숄드에 대한 컨트롤러를 트랙바에 붙인다
cv2.createTrackbar('High Threshold', 'Edges', highThreshold, maxThreshold, updateHighThreshold)

# aperture를 트랙바에 붙인다
cv2.createTrackbar('Aperture Size', 'Edges', apertureIndex, maxapertureIndex, updateApertureIndex)

# 블러 컨트롤러를 트랙바에 붙인다
cv2.createTrackbar('Blur', 'Edges', blurAmount, maxBlurAmount, updateBlurAmount)


cv2.waitKey()
cv2.destroyAllWindows()


