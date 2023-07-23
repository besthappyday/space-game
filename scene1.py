
from tools import *

def scene_run1(display, value=None):
    print("I am scene1")
    bgm = get_music('starting_bgm.mp3')
    bgm.play(-1)

    # surface_start= make_surface('start.png')
    surface_start= make_surface('start.jpg')
    surface_back= make_surface('宇宙背景.jpg')
 
    
    surface_文字 = make_surface('文字.jpg')
  
    result:dict = {
       "width": 100,
       "name": "PIG"
    }

    def on_event(event):
      x,y=pygame.mouse.get_pos() 
      w,h=surface_start.get_size()
      if 530<x<530+w and 500<y<500+h:
        if hasattr(event,"button"):
           if 1==event.button:
             return 2
    


    
   
    # display = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

    c=True
    while c==True:
        time.sleep(0.033)
        
        #surface_start.get_size =
        #surface_start = pygame.transform.scale(surface_start)
        display.blit(surface_back, (0,0))
        display.blit(surface_start, (530, 500))
        
        display.blit(surface_文字, (400,100))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
            elif event.type ==pygame.MOUSEBUTTONUP:  
                value=on_event(event)
                if value==2:
                   c=False
                   

              
    return 2 if value is None else value
        
