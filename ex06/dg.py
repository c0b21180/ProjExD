from cmath import rect
import pygame as pg
import sys
import random
import numpy as np
max_bm = 0
bg_x = 0
t = 0
#スクリーン用クラス
class Screen:
    def __init__(self, title, wh: tuple, img):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rect = self.sfc.get_rect()
        self.bg_sfc = pg.image.load(img).convert()
        self.bg_rect = self.bg_sfc.get_rect()

    def blit(self,bg_x):
        #背景を動かす
        self.sfc.blit(self.bg_sfc,[bg_x-1600,0])
        self.sfc.blit(self.bg_sfc,[bg_x,0])

#こうかとん用クラス
class Bird:
    def __init__(self, img, size: float, screen: Screen):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rect = self.sfc.get_rect()
        self.rect.center = self.rect.width, (screen.rect.height - self.rect.height) // 2
        self.gravity = 0

    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rect)

    def update(self, screen: Screen):
        key = pg.key.get_pressed()
        if self.rect.y >= 750:
            self.rect.y = 750
            if key[pg.K_SPACE]:
                self.gravity = -30
        #重力の計算
        self.gravity += 1
        if self.gravity > 15:
            self.gravity = 15
        self.rect.y += self.gravity  
        self.blit(screen)



#爆弾用クラス
class Bomb:
    def __init__(self, img, size: float, screen: Screen):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rect = self.sfc.get_rect()
        self.rect.x = screen.rect.width + self.rect.width
        self.rect.y = screen.rect.height - self.rect.height
        self.vx = -10
        self.vy = 0

    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rect)

    def update(self, screen: Screen):
        self.rect.move_ip(self.vx,self.vy)
        self.blit(screen)



def main():
    global bg_x
    global t
    #fpsのカウント開始
    clock = pg.time.Clock()
    sc = Screen("飛べ！こうかとん", (1600, 900), "ex06/fig/pg_bg.jpg")
    tori = Bird("ex06/fig/6.png", 2.0, sc)
    #ボムをリストに格納
    bomb = Bomb("ex06/fig/1.png",random.randint(3,6) , sc)
    bomlis = [bomb]
    #描画
    while True:
        t += 1
        bg_x = (bg_x-0.6)%1600
        sc.blit(bg_x)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        tori.update(sc)
        #ボムをだいたい1秒に一個作成
        if t%120 == 0:
            bomlis.append(Bomb("ex06/fig/1.png",random.randint(3,6) , sc))

        for i , bom in enumerate(bomlis):
            bom.update(sc)
            #ボムが画面外に消えたら削除
            if bom.rect.y > 1600:
                bomlis.pop(i)
            if tori.rect.colliderect(bom.rect):
                return

        pg.display.update()
        clock.tick(120)

def check_bound(rect, sc_rect):
    w, h = 1, 1
    if rect.left < sc_rect.left or rect.right > sc_rect.right:
        w = -1
    if rect.top < sc_rect.top or rect.bottom > sc_rect.bottom:
        h = -1
    return w, h


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()