from tools import *


canvas_黑線 = None


def  my_key_parse(map_move):
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
                    map_move["state"] = "停止"
            return user_exit
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 - left click, # 2 - middle click, # 3 - right click
            if 1 == event.button: 
                mos_x, mos_y = pygame.mouse.get_pos() # relative to left, top window pos
                pos_bg = map_move["position"]
                pos_map = [mos_x - pos_bg[0], mos_y - pos_bg[1]]
                clr = canvas_黑線[pos_map[0],pos_map[1]]
                print(f"mos_x:{mos_x}, mos_y:{mos_y}, pos_bg:{pos_bg}, map:{pos_map}, clr:{clr}")


        if hasattr(event, "key"):
            print(f"key: {event.key}")
            # if 99 == event.key: # "c"            
            # elif 116 == event.key: # "t"
            if 32 == event.key:
                map_move["state"] = "停止"
            
            # up key: 1073741906
            if 1073741906 == event.key:
                # people["position"][1] = people["position"][1] - 20
                map_move["state"] = "跑步"
                map_move["direction"] = "上"
            # right key: 1073741903
            if 1073741903 == event.key:
                # people["position"][0] = people["position"][0] + 20
                map_move["state"] = "跑步"
                map_move["direction"] = "右"
            # down key: 1073741905
            if 1073741905 == event.key:
                # people["position"][1] = people["position"][1] + 20
                map_move["state"] = "跑步"
                map_move["direction"] = "下"
            # left key: 1073741904
            if 1073741904 == event.key:
                # people["position"][0] = people["position"][0] - 20
                map_move["state"] = "跑步"
                map_move["direction"] = "左"

    return False





def scene_run2(display,value=2):
    global canvas_黑線
    canvas_黑線 = load_canvas('完整黑框線2.jpg')
    base_surface = make_surface('完整黑框線2.jpg') #, True)
    # base_surface = make_surface('太空地圖.jpg', True)
    # surface_人物1 = make_surface('小人物1.jpg')
    # surface_人物2 = make_surface('小人物2.jpg')
    surface_人物1 = make_surface('飛船.jpg')
    surface_人物2 = make_surface('飛船.jpg')
    surface_起點 = make_surface('太空站.jpg')
    surface_終點 = make_surface('地球.jpg')
    entrypoint = [328, 357]
    exitpoint = [1559, 840]

    def enter_exit(x, y):
        done = x >exitpoint[0] and y <exitpoint[1]
        # self.done = False
        return done
    
    map_move = {
        "position": [-500,-600],
        "state": "停止"
    }
    起點_pos = {
        "position": [40, 150],
        "state": "停止"
    }
    終點_pos = {
        "position": [3140, 1200],
        "state": "停止"
    }
    actor_pos = [300, 300]
    #起點_pos = [300, 300]
    # canvas_黑線_pos= [actor_pos[0]-entrypoint[0], actor_pos[1]-entrypoint[1]]
    # actorx, actory = [actor_pos[0]-canvas_黑線_pos[0], actor_pos[1]-canvas_黑線_pos[1]]
    actorx, actory = actor_pos
    startx, starty = 起點_pos
    index = 0
    while True:
        time.sleep(0.033) # 30fps
        display.fill([ 45, 0, 103])
        # time.sleep(0.33) # 3fps
        if my_key_parse(map_move): break
        

        # if map_move.get("state") == "停止":
        #     display.blit(base_surface, map_move.get("position"))
        
        
        steppixel =10
        
        
        
        if map_move.get("state") == "跑步" and not enter_exit(actorx, actory):
            d = map_move.get("direction")
            pos = [actorx - map_move["position"][0], actory - map_move["position"][1]]
           
            if d == "左": 
                pos=[pos[0] -steppixel, pos[1]]
                print(f"pos:{pos}, color:{canvas_黑線[pos[0],pos[1]]}")
                if all([255 == rgb for rgb in canvas_黑線[pos[0],pos[1]]]):
                # if all([255 == rgb for rgb in canvas_黑線[actorx -steppixel, actory]]):
                   map_move["position"][0] = map_move["position"][0] + steppixel
                   起點_pos["position"][0] = 起點_pos["position"][0] + steppixel
                   終點_pos["position"][0] = 終點_pos["position"][0] + steppixel
                   
            if d == "右":  
                pos=[pos[0] +steppixel, pos[1]]
                print(f"pos:{pos}, color:{canvas_黑線[pos[0],pos[1]]}")
                if all([255 == rgb for rgb in canvas_黑線[pos[0],pos[1]]]):
                # if all([255 == rgb for rgb in canvas_黑線[actorx +steppixel, actory]]):
                  
                   map_move["position"][0] = map_move["position"][0] - steppixel
                   起點_pos["position"][0] = 起點_pos["position"][0] - steppixel
                   終點_pos["position"][0] = 終點_pos["position"][0] - steppixel
            
            if d == "上": 
                pos=[pos[0], pos[1] -steppixel]
                print(f"pos:{pos}, color:{canvas_黑線[pos[0],pos[1]]}")
                if all([255 == rgb for rgb in canvas_黑線[pos[0],pos[1]]]):
                # if all([255 == rgb for rgb in canvas_黑線[actorx, actory -steppixel]]):
                    
                   map_move["position"][1] = map_move["position"][1] + steppixel
                   起點_pos["position"][1] = 起點_pos["position"][1] + steppixel
                   終點_pos["position"][1] = 終點_pos["position"][1] + steppixel
                
            if d == "下": 
                pos=[pos[0], pos[1] +steppixel]
                print(f"pos:{pos}, color:{canvas_黑線[pos[0],pos[1]]}")
                if all([255 == rgb for rgb in canvas_黑線[pos[0],pos[1]]]):
                # if all([255 == rgb for rgb in canvas_黑線[actorx, actory +steppixel]]):
                    
                   map_move["position"][1] = map_move["position"][1] - steppixel
                   起點_pos["position"][1] = 起點_pos["position"][1] - steppixel
                   終點_pos["position"][1] = 終點_pos["position"][1] - steppixel


            # display.blit(base_surface, map_move.get("position"))
            display.blit(base_surface, map_move.get("position"))
            display.blit(surface_起點 ,  起點_pos.get("position"))
            display.blit(surface_終點 ,  終點_pos.get("position"))
            if index % 19 < 11:
                # display.blit(surface_人物1, (517, 576))
                display.blit(surface_人物1, actor_pos)
            else: 
                display.blit(surface_人物2, actor_pos)
                # display.blit(surface_人物2, (517, 576))

        else:
            # display.blit(base_surface, map_move.get("position"))
            display.blit(base_surface, map_move.get("position"))
            display.blit(surface_起點 , 起點_pos.get("position"))
            display.blit(surface_終點 ,  終點_pos.get("position"))
            display.blit(surface_人物1, actor_pos)

    
        
        pygame.display.flip()
        index = index +1  # index += 1

    pygame.quit()
    return 3 if value is 2 else 4  