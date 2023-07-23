"""
"""

import os
import time
import sys
# import numpy as np
import math
import logging

import pygame

# ================================================================================== The Customize module
class CParameters():
    def __init__(self, **kwargs): [setattr(self, k, v) for k, v in kwargs.items()]
    

def draw_text(**kwargs):
    # display = pygame.display
    display = kwargs["display"]

    defaultFontName = "Times New Roman"
    defaultColor = (255, 255, 255)
    defaultSize = 22
    defaultText = "(no text)"
    defaultPos = (0, 0)

    new_font = pygame.font.SysFont(
        kwargs.get("font_name", defaultFontName), 
        kwargs.get("font_size", defaultSize)
        )
    new_font.set_bold(False)
    new_font.set_italic(False)

    surface = new_font.render(
        kwargs.get("text", defaultText), 
        True, 
        kwargs.get("font_color", defaultColor)
        )
    display.blit(surface, kwargs.get("position", defaultPos))


class countdownTimer():
    def __init__(self, **kwargs):

        self.display = kwargs.get("display")

        self.font_color = kwargs.get("font_color", [200, 250, 200])
        self.font_size = kwargs.get("font_size", 12)
        self.font_name = kwargs.get("font_name","Mongolian Baiti")
        self.position = kwargs.get("position", [200, 200])
        self.timeup_cbf = kwargs.get("timeup")

        import time
        self.currentTime = time.time()
        self.maxTime = kwargs.get("maxTime", 30)
        self.timeGap = kwargs.get("timeGap", 1)
        self.remainTime = self.maxTime

    def update(self):
        if self.remainTime > 0:
            now = time.time()
            if now - self.currentTime >= self.timeGap:
                self.remainTime -= self.timeGap
                self.currentTime = now
            if self.remainTime <= 0: 
                self.remainTime = 0
                if callable(self.timeup_cbf): 
                    self.timeup_cbf()
        self.show()

    def show(self):
        draw_text(display=self.display,
                font_color=self.font_color,
                font_size=self.font_size,
                font_name=self.font_name,
                position=self.position,
                text=f"Remain {self.remainTime:02d} sec"
                # text=f"{self.remainTime:02d}"
            )

class endCredits(countdownTimer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text=kwargs.get("text", "片尾名單")
        self.text=text.split("\n")
        self.lineGap=kwargs.get("lineGap", 30)
        self.moveStep = kwargs.get("moveStep", 1)


    def show(self):
        self.position[1] -= self.moveStep

        for ind, text in enumerate(self.text):
            position = [self.position[0], self.position[1] + self.lineGap *ind]
            draw_text(display=self.display,
                    font_color=self.font_color,
                    font_size=self.font_size,
                    font_name=self.font_name,
                    position=position,
                    text=text
                )


# ================================================================================== The Customize Functions
def on_event(event):
    global Record_Coordinates, YAW_Degree, Apply_Transform
    if hasattr(event, "button"):
        # 1 - left click
        # 2 - middle click
        # 3 - right click
        if 1 == event.button: pass
        elif 3 == event.button: pass

    elif hasattr(event, "key"):
        print(event.key)
        # if 112 == event.key:      # "p"
        # if 99 == event.key:       # "c"
        # elif 116 == event.key:    # "t"
        # elif 118 == event.key:    # "v"
        # elif 120 == event.key:    # "x"
        # elif 121 == event.key:    # "y"
        # elif 104 == event.key:    # "h"

CT = None
EndCredits = None

def customization(more_info):
    result = {}
    display = more_info.get('display')

    pygame.mixer.music.load('500.mp3')
    pygame.mixer.music.play()

    sound = pygame.mixer.Sound('button-7.wav')
    
    def timeup(): 
        sound.play(loops=1)
        # playSound()

    global CT, EndCredits
    CT = countdownTimer(display=display,
                font_color=[200, 250, 200],
                font_size=48,
                # font_name="Mongolian Baiti",
                position=[200, 200],
                maxTime = 10,
                timeup=timeup
            )
    text = "片尾名單"
    with open("name_list.txt", "r", encoding='utf-8') as f:
        text = f.read()
    EndCredits = endCredits(display=display,
                font_color=[200, 250, 200],
                font_size=48,
                font_name="Microsoft JhengHei",
                position=[200, 200],
                text=text,
                lineGap=80,
                moveStep=1,
                maxTime = 8,
                timeGap=0.3,
                timeup=timeup,
            )

    # pygame.mixer.init(channels=2) #frequency=44100, size=16, channels=1
    # ch = pygame.mixer.get_num_channels()

    # from moviepy.editor import VideoFileClip
    # clip = VideoFileClip('starting.mp4').subclip(10, 20)
    # # .set_start(5).crossfadeout(3)
    # clip = clip.without_audio()
    # clip.preview()

    # movie = pygame.movie.Movie('starting.mp4')
    # screen = pygame.display.set_mode((movie.get_size()))
    # movie.set_display(screen)
    # movie.play()
    # while movie.get_busy():
    #     pygame.time.Clock().tick(60)

    # import cv2
    # cap = cv2.VideoCapture('starting.mp4')
    # while True:
    #     ret, frame = cap.read()
    #     if not ret:
    #         break
    #     cv2.imshow('frame', frame)
    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #         break
    # cap.release()
    # cv2.destroyAllWindows()
    return result

def customize_render(pygame, display, base_dimention):
    
    CT.update()
    EndCredits.update()
    return 

def customize_release(id_list=[]):
    return

# ================================================================================== Global execute/Main

if __name__ == '__main__':
    # exit(0)
    pass