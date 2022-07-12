import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)      #Surface
        self.rct = self.sfc.get_rect()          #Rect
        self.bgi_sfc = pg.image.load(image)     #Surface
        self.bgi_rct = self.bgi_sfc.get_rect()  #Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)             #Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size) #Surface
        self.rct = self.sfc.get_rect()              #Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        #screen_sfc.blit(kkimg_sfc, kkimg_rct)
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_LSHIFT] == True:     #LSHIFTを押している間移動速度を上げる
            move_speed = 4
        else:
            move_speed = 2

        if key_states[pg.K_UP]:
            self.rct.centery -= move_speed
        if key_states[pg.K_DOWN]:
            self.rct.centery += move_speed
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= move_speed
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += move_speed

        if check_bound(self.rct, scr.rct) != (1,1) :
            if key_states[pg.K_UP]:
                self.rct.centery += move_speed
            if key_states[pg.K_DOWN]:
                self.rct.centery -= move_speed
            if key_states[pg.K_LEFT]:
                self.rct.centerx += move_speed
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= move_speed
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko *1.001
        self.vy *= tate *1.001
        # 練習5
        self.blit(scr)          

def main():
    clock = pg.time.Clock()

    # pg.display.set_caption("逃げろ！こうかとん")
    # screen_sfc = pg.display.set_mode((1600, 900))
    # screen_rct = screen_sfc.get_rect()
    # bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    # bgimg_rct = bgimg_sfc.get_rect()
    # screen_sfc.blit(bgimg_sfc, bgimg_rct)
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")


    # kkimg_sfc = pg.image.load("fig/3.png")
    # kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    # kkimg_rct = kkimg_sfc.get_rect()
    # kkimg_rct.center = 900, 400
    kkt = Bird("fig/3.png", 2.0, (900, 400))

    # bmimg_sfc = pg.Surface((60, 60))
    # bmimg_sfc.set_colorkey((0, 0, 0))
    # pg.draw.circle(bmimg_sfc, (255, 0, 0), (30, 30), 30)
    # bmimg_rct = bmimg_sfc.get_rect()
    # bmimg_rct.centerx = random.randint(0, screen_rct.width)
    # bmimg_rct.centery = random.randint(0, screen_rct.height)
    # vx, vy = +1, +1
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)

    while True:
        #screen_sfc.blit(bgimg_sfc, bgimg_rct)
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # key_states = pg.key.get_pressed()
        # if key_states[pg.K_LSHIFT] == True:       #LSHIFTを押している間移動速度を上げる
        #     move_speed = 4
        # else:
        #     move_speed = 2

        # if key_states[pg.K_UP]    == True: kkimg_rct.centery -= move_speed
        # if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += move_speed
        # if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= move_speed
        # if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += move_speed
        # if check_bound(kkimg_rct, screen_rct) != (1,1) :
        #     if key_states[pg.K_UP]    == True: kkimg_rct.centery += move_speed
        #     if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -= move_speed
        #     if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx += move_speed
        #     if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= move_speed
        # screen_sfc.blit(kkimg_sfc, kkimg_rct)
        kkt.update(scr)

        # bmimg_rct.move_ip(vx, vy)

        # screen_sfc.blit(bmimg_sfc, bmimg_rct)

        # yoko, tate = check_bound(bmimg_rct, screen_rct)
        # vx *= yoko *1.0001                      #壁に反射する度に僅かに加速
        # vy *= tate *1.0001
        bkd.update(scr)

        # if kkimg_rct.colliderect(bmimg_rct):
        #     root=tk.Tk()
        #     root.withdraw()
        #     tkm.showerror("残念！", "GameOver")  #爆弾に接触するとメッセージを表示
        #     return
        if kkt.rct.colliderect(bkd.rct):
            root=tk.Tk()
            root.withdraw()
            tkm.showerror("残念！", "GameOver")  #爆弾に接触するとメッセージを表示
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    yoko, tate = +1, +1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()