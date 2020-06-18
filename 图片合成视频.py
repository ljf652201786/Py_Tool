import cv2

#找一张图片查看图片尺寸
img = cv2.imread('image1.jpg')
imgInfo = img.shape
size = (imgInfo[1],imgInfo[0])
print(size)
videoWrite = cv2.VideoWriter('2.mp4',-1,5,size)# 写入对象 1 file name  2 编码器 3 帧率 4 size要和图片尺寸保持一致
# 2 编码器 3 帧率 4 size
for i in range(1,11):
    fileName = 'img/image'+str(i)+'.jpg'
    img = cv2.imread(fileName)
    videoWrite.write(img)# 写入方法 1 jpg data
#记得释放空间，要不然直接打开生成的 2.mp4 会打不开   或者 暂停下运行的服务
videoWrite.release()
print('end!')
