import cv2

for n in range(100000, 100012):
    path = 'F:\\bishe\\data\\gary2\\' + str(n) + '.jpg'
    # 读取图片
    img = cv2.imread(path)
    img = cv2.resize(img, (20, 20))
    cv2.imwrite('F:\\bishe\\data\\gary2\\' + str(n) + '.jpg', img)
    n += 1
