import cv2
import numpy as np

# FPS: Frame Per Second

cap = cv2.VideoCapture('data/videos/chaplin.mp4')
#cap = cv2.VideoCapture('data/videos/output.avi')

if cap.isOpened() == False :
    print('Error opening video stream or file')

else:
    # 반복문이 필요한 이유? 비디오는 여러 사진을 구성되어 있으므로
    # 여러장의 사진이 동영상이 된다
    while cap.isOpened() :
        # 사진을 1장씩 가져와서, frame변수에 넘파이로 넣어준다
        ret, frame = cap.read()

        # 사진이 있다면, 화면에 표시
        if ret == True:
            cv2.imshow('Frame', frame)

            # 키보드에서 ESC키를 누르면 exit 함
            if cv2.waitKey(25) & 0xFF == 27 :
                break
        else :
            break
    
    # 
    cap.release()
    

    cv2.destroyAllWindows()