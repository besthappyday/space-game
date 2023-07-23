
import time
import os
import sys
import logging

import numpy as np
from PIL import Image
import pygame

from scene1 import scene_run1
from scene2 import scene_run2
from scene3 import scene_run3
from tools import *





def my_game():
    # display = game_init()
    screen = create_Screen(icon_fn =os.path.join('resources', 'icon.jpg'), width =800, height =600)
    display =screen.display 

    display.fill((255,255,255))
    exit_scene = 999
    next_scene = 1
    while next_scene < exit_scene:
        if next_scene == 1:
            next_scene = scene_run1(display)
        elif next_scene == 2:
            next_scene = scene_run2(display)
        elif next_scene == 3:
            next_scene = scene_run3(999)
        else:
            next_scene = exit_scene

if __name__ == '__main__':
    my_game()
   