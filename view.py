#!/usr/bin/env python
"""
This is a sample implementation.
"""

# ==============================================================================
# -- imports -------------------------------------------------------------------
# ==============================================================================
import time
import os
import sys
import logging

import numpy as np
from PIL import Image
import pygame

# ================================================================================== Global Variables
# ================================================================================== Global Functions
def  my_key_parse(people):
    from pygame.locals import K_ESCAPE, K_q, KMOD_CTRL, KSCAN_Z

    keys = pygame.key.get_pressed()

    # print(f"{KSCAN_Z}:{keys[KSCAN_Z]}")
    if keys[KSCAN_Z]: 
        print("Z has been pressed!!")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYUP:
            user_exit = (event.key == K_ESCAPE) or (event.key == K_q and pygame.key.get_mods() & KMOD_CTRL)
            if not user_exit and hasattr(event, "key"):
                if 1073741906 == event.key or 1073741903 == event.key or 1073741905 == event.key or 1073741904 == event.key:
                    people["state"] = "停止"
            return user_exit

        if hasattr(event, "key"):
            print(f"key: {event.key}")
            # if 99 == event.key: # "c"            
            # elif 116 == event.key: # "t"
            if 32 == event.key:
                people["state"] = "停止"
            
            # up key: 1073741906
            if 1073741906 == event.key:
                # people["position"][1] = people["position"][1] - 20
                people["state"] = "跑步"
                people["direction"] = "上"
            # right key: 1073741903
            if 1073741903 == event.key:
                # people["position"][0] = people["position"][0] + 20
                people["state"] = "跑步"
                people["direction"] = "右"
            # down key: 1073741905
            if 1073741905 == event.key:
                # people["position"][1] = people["position"][1] + 20
                people["state"] = "跑步"
                people["direction"] = "下"
            # left key: 1073741904
            if 1073741904 == event.key:
                # people["position"][0] = people["position"][0] - 20
                people["state"] = "跑步"
                people["direction"] = "左"

    return False


def make_surface(file_name):
    image = Image.open(os.path.join('images',file_name))
    np_canvas = np.asarray(image).swapaxes(0, 1)
    surface = pygame.surfarray.make_surface(np_canvas)
    surface.set_colorkey((255, 255, 255))
    return surface

def my_game():
    pygame.init()
    pygame.font.init()

    width, height, channels = (1280,720,3) 
    display = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

 
    surface_people_1 = make_surface('人物1.jpg')
    
 
    surface_people_2 = make_surface('人物2.jpg')
    
  
    base_surface = make_surface('地圖.png')

    people = {
        "position": [0, 0],
        "state": "停止"
    }
    index = 0
    while True:
        time.sleep(0.033) # 30fps
        # time.sleep(0.33) # 3fps
        if my_key_parse(people): break


        # resize
        if base_surface.get_size() != display.get_size():
            base_surface = pygame.transform.scale(base_surface, display.get_size())

        # draw out   
        display.blit(base_surface, (0, 0))
        # display.blit(base_surface, (0, 100))
        if people.get("state") == "停止":
            display.blit(surface_people_1, people.get("position"))

        if people.get("state") == "跑步":
            d = people.get("direction")
            if d == "左": people["position"][0] = people["position"][0] - 10
            if d == "右": people["position"][0] = people["position"][0] + 10
            if d == "上": people["position"][1] = people["position"][1] - 10
            if d == "下": people["position"][1] = people["position"][1] + 10
            if index % 19 < 11:
                display.blit(surface_people_1, people.get("position"))
            else: 
                display.blit(surface_people_2, people.get("position"))

        pygame.display.flip()
        index = index +1  # index += 1

    pygame.quit()

# ==================================================================================

if __name__ == '__main__':
    my_game()