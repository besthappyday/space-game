from tools import *



def scene_run2(display,value=2):
    print("I am scene2")
    base_surface = make_surface('簡單迷宮.jpg', True)
    surface_人物 = make_surface('小人物1.jpg')
    
    
    
    
    people = {
        "position": [0, 0],
        "state": "停止"
    }
    c=True
    while c==True:
        time.sleep(0.033)
        #if base_surface.get_size() != display.get_size():
        # base_surface = pygame.transform.scale(base_surface, display.get_size())
        display.blit(base_surface, (-10, -1100))
        display.blit(surface_人物, (200, 350))
        pygame.display.flip()
        


    return 3 if value is 2 else 4