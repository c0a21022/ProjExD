import pygame as pg
import sys
import random


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh) 
        self.rct = self.sfc.get_rect()     
        self.bgi_sfc = pg.image.load(image)    
        self.bgi_rct = self.bgi_sfc.get_rect()
        self.bg_x = 0

    def blit(self):
        self.sfc.blit(self.bgi_sfc, [self.bg_x - self.rct.width, 0])  #背景を描画
        self.sfc.blit(self.bgi_sfc, [self.bg_x, 0])                   #ずらした分も描画
        self.bg_x = (self.bg_x - 5) % self.rct.width                       #背景を動かす

class Bird:
    def __init__(self, image: str, size: float, x, y):
        self.sfc = pg.image.load(image)    
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()     
        #self.rct.center = xy
        self.rct.x = x
        self.rct.y = y

        self.vel_y = 35                    #こうかとんの加速度を設定


    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed()

        if self.rct.y+self.vel_y >= 500:   #y座標と加速度を合わせた値が500を超えたら
            self.rct.y = 500               #y座標を500に固定する
            if key_states[pg.K_SPACE]:     #スペースキーが押されたら
                self.vel_y = -25           #加速度を-25に設定する

        self.vel_y += 1                    #加速度を毎tick1ずつ増やす

        if self.vel_y > 15:                #加速度が15を超えたら
            self.vel_y = 15                #15に固定する

        self.rct.y += self.vel_y           #y座標に加速度を足し合わせる

        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size))
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        
        self.rct.move_ip(self.vx, self.vy)
        
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        
        self.blit(scr)          


def main():
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/bg_sabaku.jpg")
    kkt = Bird("fig/6.png", 2.5, 300, 500)
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kkt.update(scr)
        bkd.update(scr)
        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(120)


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
