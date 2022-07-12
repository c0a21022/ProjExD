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
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr):
        self.rct.move_ip(self.vx, self.vy)

        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko *1.001
        self.vy *= tate *1.001

        self.blit(scr)          

def main():
    clock = pg.time.Clock()

    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/3.png", 2.0, (900, 400))
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kkt.update(scr)
        bkd.update(scr)

        if kkt.rct.colliderect(bkd.rct):
            root=tk.Tk()
            root.withdraw()
            tkm.showerror("残念！", "GameOver")  #爆弾に接触するとメッセージを表示
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    yoko, tate = +1, +1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()