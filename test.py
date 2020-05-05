import cv2
import numpy as np
import math

detector = cv2.CascadeClassifier('data\\haarcascades\\haarcascade_frontalface_default.xml')
mask_detector = cv2.CascadeClassifier('data\\cascade.xml')
cap = cv2.VideoCapture(0)

def gamma_trans(img, gamma):  # gamma函数处理
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]  # 建立映射表
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
    return cv2.LUT(img, gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。


# def nothing(x):
#     pass

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mean=np.mean(gray)
    gamma_val = math.log10(0.5) / math.log10(mean / 255)  # 公式计算gamma
    image_gamma_correct = gamma_trans(img, gamma_val)  # gamma变换
    faces = detector.detectMultiScale(image_gamma_correct, 1.1, 3)
    for (x, y, w, h) in faces:
        # 参数分别为 图片、左上角坐标，右下角坐标，颜色，厚度
        # face = img[y:y + h, x:x + w]  # 裁剪坐标为[y0:y1, x0:x1]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    mask_face = mask_detector.detectMultiScale(image_gamma_correct, 1.1, 5)
    for (x2, y2, w2, h2) in mask_face:
        cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)

    cv2.imshow('mask', img)
    cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()