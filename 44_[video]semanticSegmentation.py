import cv2 
import numpy as np
import imutils
import time

DEFAULT_FRAME = 1
SET_WIDTH = int(600)
normalize_image = 1 / 255.0
resize_image_shape = (1024, 512)

#sv = cv2.VideoCapture('data4/video/video.mp4')
#sv = cv2.VideoCapture('data4/video/dashcam2.mp4')
sv = cv2.VideoCapture(0)
sample_video_writer = None

# Enet 모델 가져오기 # 예측
cv_enet_model = cv2.dnn.readNet('data4/enet-cityscapes/enet-model.net')


label_values = open('data4/enet-cityscapes/enet-classes.txt').read().split('\n')
## 마지막 ''제거
label_values = label_values[: -1]

# 색 관련 파일 가져와서 레이블 색으로 만들어주기
CV_ENET_SHAPE_IMG_COLORS = open('data4/enet-cityscapes/enet-colors.txt').read().split('\n')
# 맨 마지막 따옴표 없애기 slicing
CV_ENET_SHAPE_IMG_COLORS = CV_ENET_SHAPE_IMG_COLORS[: -2+1]
temp_list = np.array( [ np.array(color.split(',')).astype('int') for color in CV_ENET_SHAPE_IMG_COLORS ] )
CV_ENET_SHAPE_IMG_COLORS = np.array(temp_list)


# # legend표시해주기 위해서 zeros로 만들기
# my_legend = np.zeros( ( len(label_values) * 25 , 300, 3), dtype='uint8' )
# # zip()는 2개의 리스트를 묶어서 처리할 수 있게함 (row를 묶어서 처리(튜플로))
# ## for 루프를 돌릴 때  enumerate는 i에 0번째로 인덱스 값을 주게 된다
# for ( i, (class_name, img_color)) in enumerate( zip(label_values, CV_ENET_SHAPE_IMG_COLORS)) :
#     color_info = [ int(color) for color in img_color ] #리스트 컴프리핸션으로 int로 바꿈
#     cv2.putText(my_legend, class_name, (5, (i * 25)+17), cv2.FONT_HERSHEY_COMPLEX , 0.5, (0, 255, 0),2)
#     cv2.rectangle(my_legend, (100, (i*25)), (300, (i*25) + 25) , tuple(color_info), -1)

# cv2.imshow('legend', my_legend)


try:
    prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() else cv2.CAP_PROP_FRAME_COUNT
    total = sv.get(prop)
    print("[INFO] {} total frames in video.".format(total))
except:
    print('{INFO] could not determine number of frames in video')
    total = -1


while True:
    grabbed, frame = sv.read()

    if grabbed == False:
        break
    
    video_frame = imutils.resize(frame, width=SET_WIDTH)
    blob_img = cv2.dnn.blobFromImage(frame, normalize_image, resize_image_shape, 0, swapRB=True, crop=False)
    cv_enet_model.setInput(blob_img)
    start_time = time.time() #첫 시간 재기 (실행할 코드 사이에 넣어준다) 예측하는 시간을 구함
    cv_enet_model_output = cv_enet_model.forward()
    end_time = time.time() #끝나는 시간 재기
        
    (classes_num, height, width) = cv_enet_model_output.shape[1:4] # 0번째는 뺌
    class_map = np.argmax(cv_enet_model_output[0], axis=0)

    mask_class_map = CV_ENET_SHAPE_IMG_COLORS[class_map] #레이블을 3차원 이미지로 
    # 리사이즈
    mask_class_map = cv2.resize(mask_class_map, (video_frame.shape[1], video_frame.shape[0]), interpolation=cv2.INTER_NEAREST)
    # 모델 합치기
    cv_enet_model_output = ((0.3 * video_frame) + (0.6 * mask_class_map)).astype('uint8')

    #print(cv_enet_model_output)
    print(end_time - start_time)
    cv2.imshow('result video', cv_enet_model_output)
    if cv2.waitKey(25) & 0xFF == 27 :
        break
    
sv.release()

#cv2.waitKey()
cv2.destroyAllWindows()