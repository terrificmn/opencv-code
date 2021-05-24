import cv2
import numpy as np

# # 이미지 가져오기
# originImg = cv2.imread('data3/test_image.jpg', 1)

# # 그레이 스케일, np copy() 를 이용해서 복사해서 사용
# lanelinesImg = originImg.copy()
# grayImg = cv2.cvtColor(lanelinesImg, cv2.COLOR_BGR2GRAY)
# cv2.imshow('GRAY SCALED', grayImg)

# # smoothing 하기 # 노이즈를 제거하기 위해서 한다
# gaussianImg = cv2.GaussianBlur(grayImg, (5, 5), 1)
# cv2.imshow('GaussianBlur', gaussianImg)

# # Canny Edge Dectection
# canny_img = cv2.Canny(gaussianImg, 40, 100, apertureSize=3)
# cv2.imshow('Canny', canny_img)

# masking the Region Of Interest function
def reg_of_interest(image) :
    image_height = image.shape[0]
    # np.array()로 2차원으로 만들고 그 안에 튜플로 생성한다
    polygons = np.array( [[ (200, image_height), (1100, image_height), (550, 250) ]] )
    # 0으로 만들어 준다 (관심없는 영역)
    image_mask = np.zeros_like(image)
    # 이제 관심영역 Region of Interest 부분을 255로 채운다
    cv2.fillPoly(image_mask, polygons, 255)
    # image 들어온 파일에서 마스크된 image_mask 를 bitwise_and로 연산한다
    masking_image = cv2.bitwise_and(image, image_mask)
    return masking_image


# Canny Edge에서 처리하는 부분을 함수로 만듬
def canny_edge(image):
    gray_conversion = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_conversion = cv2.GaussianBlur(gray_conversion, (5, 5), 1)
    canny_conversion = cv2.Canny(blur_conversion, 50, 100, apertureSize=3)
    return canny_conversion


# Hough Transform 함수
def show_lines(image, lines):
    lines_image = np.zeros_like(image) #검정 배경으로 만들기
    if lines is not None:
        for i in range(len(lines)) :
            for x1, y1, x2, y2 in lines[i]:
                cv2.line(lines_image, (x1,y1), (x2, y2), (255, 0, 0), 10 )
    
    return lines_image


# 여러 선을, 하나의 선으로 만들어 주는 함수
# 방법은? 기울기와 y절편을 평균으로 해서 하나의 기울기와 y절편을 갖도록 만드는 방법
def make_coordinates(image, line_parameters) :
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1 * (3/7) )  # 길이에 따라 2/5 1/5 이런식으로 하면 길어진다
    x1 = int( (y1 - intercept) / slope ) 
    x2 = int( (y2 - intercept) / slope )
    return np.array( [x1, y1, x2, y2] )


def average_slope_intercept(image, lines) :
    left_fit = [] # 기울기가 0보다 작은 값들
    right_fit = [] # 기울기가 0보다 큰 값들
    # Hough트랜스폼으로 만들어진 라인을 
    for line in lines :
        # 직선의 기울기와 y절편을 구해준다
        x1, y1, x2, y2 = line.reshape(4) #4차원으로 만들어준다
        parameter = np.polyfit( (x1, x2), (y1, y2), 1)
        slope = parameter[0]
        intercept = parameter[1]
        if slope < 0 : #기울기가 0보다 작으면 오른쪽 차선이 된다 ( 이런 모양 \ )
            left_fit.append( (slope, intercept) )
        else:
            right_fit.append( (slope, intercept) )

    # axis=0 기준이므로 row로 연산하면서 컬럼별로 평균을 구한다
    left_fit_avg = np.average(left_fit, axis=0)
    right_fit_avg = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_avg)
    right_line = make_coordinates(image, right_fit_avg)

    return np.array( [[left_line, right_line ]])





image = cv2.imread('data3/test_image.jpg')
lanelinesImg = image.copy()

canny_conversion = canny_edge(lanelinesImg)
roi_conversion = reg_of_interest(canny_conversion)

# HoughLines()는 샘플링을 해서 뽑기 때문에 연산 속도가 빠르다 (확률 허프 변환)
# minLineLengh = 최소 라인이고 더 작은것은 표시 안함
lines = cv2.HoughLinesP(roi_conversion, 1, np.pi/180, 100, minLineLength=40, maxLineGap=5)

averagedLines = average_slope_intercept(lanelinesImg, lines)

houghedLines = show_lines(lanelinesImg, averagedLines)


print(averagedLines.shape)


# 가중치 추가하기해서 합치기
combinedImg = cv2.addWeighted(lanelinesImg, 0.8, houghedLines, 1, 1)


# cv2.imshow('origin', lanelinesImg)
# cv2.imshow('ROI', houghedLines)
# cv2.imshow('combined', combinedImg)

cap = cv2.VideoCapture('data3/test2.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # canny엣지를 구함
        canny_image = canny_edge(frame)
        # roi 만들기
        roi_image = reg_of_interest(canny_image)
        #선 연결 HoughLinesP()
        lines = cv2.HoughLinesP(roi_image, 1, np.pi/180, 100, minLineLength=40, maxLineGap=5)
        #기울기로 왼쪽, 오른쪽 차선 평균선 구하기
        # 원본 이미지와 연결된 선 이미지를 넘긴다
        averaged_lined = average_slope_intercept(frame, lines)
        # 라인 가져오기
        getLine_image = show_lines(frame, averaged_lined)
        combined_image = cv2.addWeighted(frame, 0.8, getLine_image, 1, 1)
        cv2.imshow('result', combined_image)
        if cv2.waitKey(1) & 0xFF == 27 :  #27은 ESC
            break

cap.release()

cv2.waitKey()
cv2.destroyAllWindows()


