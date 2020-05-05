#毕业设计：基于opencv和python来实现口罩检测


import cv2
import time
import numpy as np
import pygame
import threading


yspeech=r'music/dai.mp3'
nspeech=r'music/meidai.mp3'
pygame.mixer.init()

# 尝试pygame播放mp3
# track = pygame.mixer.music.load(yspeech)
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer.music.stop()



def nothing(x):  # 滑动条的回调函数
    pass


def music_yes():
    timeplay = 5
    global playflag_yes
    playflag_yes = 0
    while True:
        if playflag_yes == 1:
            track = pygame.mixer.music.load(yspeech)
            print("-----戴口罩才是靓仔-----")
            pygame.mixer.music.play()
            time.sleep(timeplay)
            playflag_yes = 0
        time.sleep(0)


def music_no():
    timeplay = 6
    global playflag_no
    playflag_no = 0
    while True:
        if playflag_no == 1:
            track = pygame.mixer.music.load(nspeech)
            print("------戴口罩好吗-------")
            pygame.mixer.music.play()
            time.sleep(timeplay)
            playflag_no = 0
        time.sleep(0)



