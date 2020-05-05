#添加音频的尝试----失败
import cv2
import time
import numpy as np
import pygame
import threading


yspeech =r'music/dai.mp3'
nspeech =r'music/meidai.mp3'
pygame.mixer.init()

# 尝试pygame播放mp3
# track = pygame.mixer.music.load(yspeech)
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer.music.stop()


def music_yes():
    timeplay = 8
    while True:
        pygame.mixer.music.load(yspeech)
        print("-----戴口罩才是靓仔-----")
        pygame.mixer.music.play()
        time.sleep(timeplay)


def music_no():
    timeplay = 6
    global playflag_no
    playflag_no = 0
    while True:
        if playflag_no == 1:
            pygame.mixer.music.load(nspeech)
            print("------戴口罩好吗-------")
            pygame.mixer.music.play()
            time.sleep(timeplay)
            playflag_no = 0
        time.sleep(0)


def music_init():
    global thread_music_yes
    global thread_music_no
    image =cv2.imread("images\\background.jpg")
    cv2.imshow('skin' ,image)
    cv2.waitKey()
    cv2.destroyAllWindows()


music_init()
threading.Thread(target=music_yes()).start()

