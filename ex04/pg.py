from turtle import filling
import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("ex04/fig/6.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    kkimg_sfc = pg.image.load("ex04/fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery +=1
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -=1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx +=1
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit
    sys.exit