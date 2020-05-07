# 毕业设计：基于opencv和python来实现口罩检测

import cv2
import numpy as np
import math
import pygame
import time
import threading

pspeech =r'music/pass.mp3'
yspeech = r'music/dai.mp3'
nspeech = r'music/meidai.mp3'
pygame.mixer.init()


# 尝试pygame播放mp3
# track = pygame.mixer.music.load(yspeech)
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer.music.stop()

def music_yes():
    timeplay = 4
    global maskOn, lock
    while True:
        if maskOn == 1:
            pygame.mixer.music.load(pspeech)
            print("-----通过口罩检测-----")
            pygame.mixer.music.play()
            time.sleep(timeplay)
            maskOn == 0
        time.sleep(0)


def music_no():
    timeplay = 6
    while True:
        pygame.mixer.music.load(nspeech)
        print("-----请您戴口罩-----")
        pygame.mixer.music.play()
        time.sleep(timeplay)


#
#
# def music_no():
#     timeplay = 6
#     global playflag_no
#     playflag_no = 0
#     while True:
#         if playflag_no == 1:
#             track = pygame.mixer.music.load(nspeech)
#             print("------戴口罩好吗-------")
#             pygame.mixer.music.play()
#             time.sleep(timeplay)
#             playflag_no = 0
#         time.sleep(0)


detector = cv2.CascadeClassifier('data\\haarcascades\\haarcascade_frontalface_default.xml')
eyes_detector = cv2.CascadeClassifier('data\\haarcascades\\haarcascade_eye_tree_eyeglasses.xml')
mask_detector = cv2.CascadeClassifier('data\\cascade.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
flag=True
# event_obj = threading.Event()  # 创建一个事件
thread_yes=threading.Thread(target=music_yes)
thread_yes.setDaemon(True)




def gamma_trans(img, gamma):  # gamma函数处理
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]  # 建立映射表
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
    return cv2.LUT(img, gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。


while True:
    ret, img = cap.read()
    if ret == False:
        print("无法打开摄像头")
        break
    # 高斯模糊
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    mean = np.mean(gray)
    gamma_val = math.log10(0.5) / math.log10(mean / 255)  # 公式计算gamma
    image_gamma_correct = gamma_trans(img, gamma_val)  # gamma变换

    faces = detector.detectMultiScale(image_gamma_correct, 1.1, 6)
    mask_face = mask_detector.detectMultiScale(image_gamma_correct, 1.1, 4)
    # 参数分别为 图片、左上角坐标，右下角坐标，颜色，厚度
    # face = img[y:y + h, x:x + w]  # 裁剪坐标为[y0:y1, x0:x1]
    if len(mask_face) <= 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, 'NO MASK', (x - 25, y - 25), font, 1.2, (255, 0, 0), 2)
    if len(mask_face) and flag:
        flag=False
        global maskOn
        maskOn = 1
        print("------------戴口罩")
        thread_yes.start()


    for (x2, y2, w2, h2) in mask_face:
        cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)
        cv2.putText(img, 'HAVE MASK', (x2 - 25, y2 - 25), font, 1.2, (0, 0, 255), 2)

    eyes = eyes_detector.detectMultiScale(image_gamma_correct, 1.1, 5)
    for (x3, y3, w3, h3) in eyes:
        cv2.rectangle(img, (x3, y3), (x3 + w3, y3 + h3), (0, 255, 0), 2)

    cv2.imshow('mask', img)
    c = cv2.waitKey(30) & 0xff
    if c == 27:
        cap.release()
        break
    # if maskOn == 0:
    #     print("------------无口罩")
    #     threading.Thread(target=music_no).start()
    #     maskOn = 3
    # elif maskOn == 1:
    #     print("戴口罩------------")
    #     threading.Thread(target=music_yes).start()
    #     time.sleep(5)
    #     maskOn = 3

cap.release()
cv2.destroyAllWindows()
