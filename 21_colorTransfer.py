import cv2
import numpy as np

src = cv2.imread('data/images/image1.jpg')
dst = cv2.imread('data/images/image2.jpg')

cv2.imshow('src', src)
cv2.imshow('dst', dst)

output = dst.copy()

#색을 LAB형태로 바꾸기
srcLab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
dstLab = cv2.cvtColor(dst, cv2.COLOR_BGR2LAB)
outputLab = cv2.cvtColor(output, cv2.COLOR_BGR2LAB)

# float으로 바꾸기
srcLab = srcLab.astype('float') # np.float32(srcLab) 이렇게 해도 됨
dstLab = dstLab.astype('float')
outputLab = output.astype('float')

print(srcLab)

# 채널 분리 
srcL, srcA, srcB = cv2.split(srcLab)
dstL, dstA, dstB = cv2.split(dstLab)
outL, outA, outB = cv2.split(outputLab)


outL = dstL - dstL.mean()
outA = dstA - dstA.mean()
outB = dstB - dstB.mean()


# 우리가 얻고자 하는 이미지 (강가 이미지)
# 표준편차를 이용
outL = outL * ( srcL.std() / dstL.std() )

outA = outL * ( srcA.std() / dstA.std() )

outB = outL * ( srcB.std() / dstB.std() )



outL = outL + srcL.mean()
outA = outA + srcA.mean()
outB = outB + srcB.mean()




# 우리가 눈으로 보기 위해서? 0~ 255 사이 값으로 셋팅
outL = np.clip(outL, 0, 255)
outA = np.clip(outA, 0, 255)
outB = np.clip(outB, 0, 255)



# 바꾼 다음에는 채널을 합친다
outputLab = cv2.merge( [outL, outA, outB] )

# 이미지는 8비트(1바이트) 정수이므로, 형 변환을 해야한다
outputLab = np.uint8(outputLab)

# imsho()는 BGR이므로 바꿔야한다
outputLab = cv2.cvtColor(outputLab, cv2.COLOR_LAB2BGR)

cv2.imshow('output', outputLab)


cv2.waitKey()
cv2.destroyAllWindows()