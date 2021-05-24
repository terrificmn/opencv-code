import cv2
import numpy as np

def mouse_handler(event, x, y, flags, data) :
    
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(data['im'], (x, y), 3, (0, 0, 255), 5, 16)
        cv2.imshow( 'Image', data['im'] )
        # 4 작을 경우에만 추가 
        if len(data['points']) < 4 :
            data['points'].append([x, y])


def get_four_points(im) :
    data = {}
    data['im'] = im.copy()
    # 마우스로 클릭을 하면 좌표가 들어갈 리스트를 만듬
    data['points'] = []

    cv2.imshow('Image', im)
    # 콜백 메소드를 사용해서 mouse_handler 함수 호출한다, 사용자 콜백함수를 
    cv2.setMouseCallback('Image', mouse_handler, data)
    cv2.waitKey(0)

    # 유저가 마우스를 찍은 점을 float으로 바꿔줘야 한다
    points = np.array( data['points'], dtype=float)
    # mouse_handler함수에서 data['points'] 에 이미 리스트로 추가했기 때문에 2차원으로 구성됨

    return points

