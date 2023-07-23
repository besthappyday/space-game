import time
import os
import sys
import logging
import numpy as np
import pygame
from PIL import Image

#from utilities.tool2 import *
from tool2 import *

# ================================================================================== Global Variables
LOGGER: logging.Logger = logging.getLogger(__name__)

SCREEN = None
RESOURCE_PATH = os.path.join(os.getcwd(), 'resources')



# ================================================================================== Global Function
def key_parse_exit(on_event=lambda x: None):
    from pygame.locals import K_ESCAPE, K_q, KMOD_CTRL, KSCAN_Z
    keys = pygame.key.get_pressed()
    if keys[KSCAN_Z]: print("Z has been pressed!!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            on_event(event, True)
        elif event.type == pygame.KEYUP:
            go_exit = (event.key == K_ESCAPE) or (event.key == K_q and pygame.key.get_mods() & KMOD_CTRL)
            if go_exit: return go_exit
            on_event(event, False)
        # handle MOUSEBUTTONUP
        elif event.type == pygame.MOUSEBUTTONUP:
            # print(event.button)
            # event.button can equal several integer values:
            # 1 - left click
            # 2 - middle click
            # 3 - right click
            # 4 - scroll up
            # 5 - scroll down
            on_event(event, False)

def create_Screen(**kwargs):
    global SCREEN
    if SCREEN is not None:
        del SCREEN
        SCREEN = None
    SCREEN = CScreen(**kwargs)
    return SCREEN

def get_Screen():
    return SCREEN


def make_snd(fn):
    if not os.path.exists(fn):
        fn = os.path.join(RESOURCE_PATH, fn)
    return pygame.mixer.Sound(fn)


def get_music(fn):
    # bgm = BG_MUSIC.get(fn)
    # if bgm is None:
    #     if not os.path.exists(fn):
    #         fn = os.path.join(RESOURCE_PATH, fn)
    #     pygame.mixer.music.load(fn)
    #     bgm = pygame.mixer.music
    #     BG_MUSIC[fn]=bgm

    if not os.path.exists(fn):
        fn = os.path.join(RESOURCE_PATH, fn)
    pygame.mixer.music.load(fn)
    bgm = pygame.mixer.music
    return bgm


def load_canvas(fn="icon.jpg"):
    if not os.path.exists(fn):
        fn = os.path.join(RESOURCE_PATH, fn)
    pic = Image.open(fn)
    # np.rot90(, 0)
    return np.array(pic).swapaxes(0, 1)

def make_surface(fn="icon.jpg", **kwargs):
    surface = None
    surface = pygame.surfarray.make_surface(load_canvas(fn))
    no_colorkey = kwargs.get('no_colorkey')
    if not no_colorkey:
        colorkey = kwargs.get('colorkey', (0, 0, 0))
        surface.set_colorkey(colorkey)
    return surface

def sameColor(clr_standard, clr2, **kwargs):
    expandValue = kwargs.get('expand', 1)*255
    the_same = True
    # value:  0~255
    for i, value in enumerate(clr_standard):
        if clr2[i] > value + expandValue or clr2[i] < value - expandValue: 
            the_same = False
    return the_same

def findColorCenter(canvas, color):
    # canvas: np.array
    positionCenter = [ -1, -1]
    h_matches = []; w_matches = []
    height, width, channel = canvas.shape
    # v = len(canvas) == height
    for i in range(height):
        for j in range(width):
            if sameColor(color, canvas[i, j], expand=0.35):
                h_matches.append(i)
                w_matches.append(j)
            # if not sameColor((255,255,255), canvas[i, j]):
            #     print([i, j])
            
    if w_matches and h_matches:
        positionCenter = [(max(w_matches) + min(w_matches))//2, (max(h_matches) + min(h_matches))//2]
    return [positionCenter[1],positionCenter[0]]


# ================================================================================== Global classes
class CScreen(object):
    def __init__(self, **kwargs):
        pygame.init()
        pygame.font.init()

        icon_fn = kwargs.get('icon_fn')
        if icon_fn:
            programIcon = pygame.image.load(icon_fn)
            pygame.display.set_icon(programIcon)

        screen_width = kwargs.get('width', 800)
        screen_height = kwargs.get('height', 600)
        self.display = pygame.display.set_mode((screen_width, screen_height),
            pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

    def render(self, surface=None, pos=(0, 0)):
        if surface:
            self.display.blit(surface, pos)

        # if base_surface.get_size() != display.get_size():
        #     base_surface = pygame.transform.scale(base_surface, display.get_size())
        # display.blit(base_surface, (0, 0))

        return pygame.display.flip()
    
    def __del__(self):
        pygame.quit()
    
class CSound():
    def __init__(self, **kwargs):
        self.sound_fn = kwargs.pop('filename')
        self.sound = make_snd(self.sound_fn)
        self.timeGap = kwargs.pop('timeGap', 1)
        self.last_playtime = time.time()

    def play(self):
        now = time.time()
        if now - self.last_playtime > self.timeGap:
            self.last_playtime = now
            self.sound.play()


class effectDecorate1(countdownTimer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text=kwargs.get("text")
        self.text=text.split("\n") if text is not None else text
        self.lineGap = kwargs.get("lineGap", 30)
        self.text_relative_pos = kwargs.get("text_relative_pos", [0, 0])
        # self.moveStep = kwargs.get("moveStep", 1)

        self.effect = kwargs.get("effect", "move_in")
        self.start_position = kwargs.get("start_position", [600, 0])
        # self.stop_point = kwargs.get("stop_point", [600, 600])
        # self.start_scale = kwargs.get("start_scale", 0.05)
        # self.stop_scale = kwargs.get("stop_scale", 2)
        self.current_pos = self.start_position
        self._distance_calc()

        self.surface = None
        self.sound = None
        self.playing = False
        fn=kwargs.get("image_filename")
        if fn is not None:
            self.surface = make_surface(fn)
        fn=kwargs.get("sound_filename")
        if fn is not None:
            self.sound = make_snd(fn)
        
    def _distance_calc(self):
        x_step = (self.start_position[0] - self.position[0]) // self.maxTime
        y_step = (self.start_position[1] - self.position[1]) // self.maxTime
        
        self.moveStep = max(abs(x_step), abs(y_step))
        if self.moveStep <=0: self.moveStep = 1
        self.x_step = -self.moveStep if x_step >= 0 else self.moveStep
        self.y_step = -self.moveStep if y_step >= 0 else self.moveStep

    def show(self):
        self.current_pos[0] = self.current_pos[0] + self.x_step if (
            (self.x_step > 0 and self.current_pos[0] < self.position[0]) or
            (self.x_step < 0 and self.current_pos[0] > self.position[0]) 
            ) else self.position[0]
        self.current_pos[1] = self.current_pos[1] + self.y_step if (
            (self.y_step > 0 and self.current_pos[1] < self.position[1]) or
            (self.y_step < 0 and self.current_pos[1] > self.position[1]) 
            ) else self.position[1]
        
        if self.sound is not None and not self.playing and self.current_pos[0] == self.position[0] and self.current_pos[1] == self.position[1] : 
            self.sound.play()
            self.playing = True
        if self.surface is not None:
            self.display.blit(self.surface, self.current_pos)
        if self.text is not None:
            for ind, text in enumerate(self.text):
                r_pos = self.text_relative_pos
                position = [self.current_pos[0] + r_pos[0], self.current_pos[1] + r_pos[1] + self.lineGap *ind]
                draw_text(display=self.display,
                        font_color=self.font_color,
                        font_size=self.font_size,
                        font_name=self.font_name,
                        position=position,
                        text=text
                    )
        return

# ================================================================================== Global execute/Main

if __name__ == '__main__':
    # filename="123.hxe"
    # fn, ext = filename.split(".")
    # print(f"fn:{fn}, ext:{ext}")
    # exit(0)
    SCENE_MAP_FN = "scene_1_map2.jpg"
    map_canvas = load_canvas(SCENE_MAP_FN)
    entrypoint_color = (0, 255, 0) # G
    entrypoint = findColorCenter(map_canvas, entrypoint_color)
    exitpoint_color = (255, 0, 0) # R
    exitpoint = findColorCenter(map_canvas, exitpoint_color)
    print(f"Map fn:{SCENE_MAP_FN}, entrypoint= {entrypoint}; exitpoint= {exitpoint}")
    # Map fn: scene_1_map.bmp, entrypoint= [319, 862], exitpoint= [319, 862]
    pass