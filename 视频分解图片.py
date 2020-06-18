# 视频分解图片
# 1 load 2 info 3 parse 4 imshow imwrite
import cv2
import os

cap = cv2.VideoCapture("C:\\Users\\ljf\\Desktop\\code\\PY\\2.mp4")# 获取一个视频打开cap 1 file name
isOpened = cap.isOpened# 判断是否打开‘
print(isOpened)
fps = cap.get(cv2.CAP_PROP_FPS)#帧率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#w h
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fps,width,height)
if not os.path.exists('img'):
    os.makedirs('img')
i = 0
while(isOpened):
    if i == 10:
        break
    else:
        i = i+1
    (flag,frame) = cap.read()# 读取每一张 flag frame

    fileName = 'img/image'+str(i)+'.jpg'
    print(fileName)
    if flag == True:
        cv2.imwrite(fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])
print('end!')
