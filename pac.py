from tools import *
def scene_run1(display, value=None):
    surface_start= make_surface('start.jpg')
    
 
    surface_框框 = make_surface('框框.jpg')
    surface_文字 = make_surface('文字.png')

    c=True
    while c==True:
        time.sleep(0.033)
        
        #surface_start.get_size =
        #surface_start = pygame.transform.scale(surface_start)
        display.blit(surface_start, (530, 500))
        display.blit(surface_框框, (400,100))
        display.blit(surface_文字, (400,100))
        pygame.display.flip()  
    return 2 if value is None else value