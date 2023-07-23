from tools import *
def __init__(self, **kwargs):

        # load background
        self.s_background = make_surface('ending.jpg')
        # load button
        self.s_btn_start = make_surface('btn.bmp')
        self.size_btn_start = self.s_btn_start.get_size()
        self.pos_btn_start = (200, 200)

        self.s_btn_exit = make_surface('exit.png')
        self.size_btn_exit = self.s_btn_exit.get_size()
        self.pos_btn_exit = (200, 400)
        
        self.mos_x, self.mos_y = 0, 0
        self.phase = 1

def click_check(self):
        result = ""
        def point_in(x, y, st, range):
            value = x >= st[0] and x<= st[0]+range[0] and y >= st[1] and y<= st[1]+range[1]
            return value
        if self.mos_x > 0 and self.mos_y >0:
            if point_in(self.mos_x, self.mos_y, self.pos_btn_start, self.size_btn_start): result = "btn_start"
            elif point_in(self.mos_x, self.mos_y, self.pos_btn_exit, self.size_btn_exit): result = "btn_exit"
        return result
    
def on_event(self, event, pressed):
        if hasattr(event, "button"):
            # 1 - left click, # 2 - middle click, # 3 - right click
            if 1 == event.button: 
                self.mos_x, self.mos_y = pygame.mouse.get_pos() # relative to left, top window pos
                
            # elif 3 == event.button: pass
        # elif hasattr(event, "key"):
        #     if 112 == event.key: # "p"
        #         pass
        return

def on_EndCreditsDone(self):
        self.phase =2

def start(self):
    exit_step =-1
    next_step =1
    step = 0 
    try:
        screen = get_Screen()
        text = "片尾名單"

        fn = "name_list.txt"
        if not os.path.exists(fn):
            fn = os.path.join(RESOURCE_PATH, fn)
        with open(fn, "r", encoding='utf-8') as f:
            text = f.read()
        
        EndCredits = endCredits(display=screen.display,
                    font_color=[200, 250, 200],
                    font_size=48,
                    font_name="Microsoft JhengHei",
                    position=[200, 200],
                    text=text,
                    lineGap=80,
                    moveStep=1,
                    maxTime = 150,
                    timeGap=0.3,
                    timeup=self.on_EndCreditsDone,
                )

        self.bgm = get_music('500.mp3')
        self.bgm.play()

        self.phase = 1
        # flow loop
        while step == 0:
            self.mos_x, self.mos_y = 0, 0
            if key_parse_exit(self.on_event): step = exit_step

            screen.display.blit(self.s_background, (0, 0))

            # phase: show name list
            if self.phase == 1:
                EndCredits.update()

            # phase2: next
            if self.phase == 2:
                state_str = self.click_check()
                if state_str == "btn_exit": step = exit_step
                elif state_str == "btn_start": step = next_step

                screen.display.blit(self.s_btn_start, self.pos_btn_start)
                draw_text(display=screen.display,
                    # font_color=self.font_color,
                    # font_size=self.font_size,
                    font_name="Microsoft JhengHei",
                    position=[240,205],
                    text="返回"
                    )
                screen.display.blit(self.s_btn_exit, self.pos_btn_exit)

            screen.render()
            time.sleep(0.066)
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        LOGGER.error(f"ERROR [main] error\n\tType: {exc_type}\n\tObject: {exc_obj}\n\tLine: {exc_tb.tb_lineno}\n(or world may crashed?)")
    finally:
        self.bgm.stop() 
        return step
def scene_run3(value=3):
    print("I am scene3")
    surface_人物1 = make_surface('飛船.jpg')
    return 1 if value is 3 else 5