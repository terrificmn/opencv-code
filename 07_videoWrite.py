import cv2
import numpy as np

#캠으로부터 데이터 가져오기 , 인덱스로 0, 캠이 더 있다면 1, 2, 3....
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("unable to read camera feed")

else:
    # 프레임의 정보 가져오기 : 화면크기 (width, height)
    frame_width = int(cap.get(3)) #3번이 width
    frame_height = int(cap.get(4)) #4번이 height

    # 캠으로 들어온 영상을 저장함
    out = cv2.VideoWriter('data/videos/output.avi',
                    cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                    10,
                    (frame_width, frame_height) )
    
    # 캠으로부터 사진을 계속 입력을 받는다
    while True : #무한 루프
        ret, frame = cap.read()

        if ret == True:
            #저장
            out.write(frame)
            #화면에 보여주기
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == 27:  #27번 ESC면 break
                break
        else:
            print('저장에 실패했습니다.')
            break
    # 자원 회수 
    cap.release()
    out.release()

    cv2.destroyAllWindows()