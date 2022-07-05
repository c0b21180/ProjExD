import random
import pygame as pg
import sys
import time
import math


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

    # 爆弾
    bmimg_sfc = pg.image.load("ex04/fig/1.png")
    bmimg_sfc = pg.transform.rotozoom(bmimg_sfc, 0, 2.0)
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(10,1590)
    bmimg_rct.centery = random.randint(10, 890)
    vx,vy = +1 , +1

    bmimg1_sfc = pg.image.load("ex04/fig/1.png")
    bmimg1_sfc = pg.transform.rotozoom(bmimg1_sfc, 0, 2.0)
    bmimg1_sfc.set_colorkey((0,0,0))
    bmimg1_rct = bmimg1_sfc.get_rect()
    bmimg1_rct.centerx = random.randint(10,1590)
    bmimg1_rct.centery = random.randint(10,890)
    vx1,vy1 = +1,+1

    font = pg.font.Font(None,100)
    s = font.render("GameOver",True,(63,255,63))
    start = time.time()
    while True:


        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]      == True:
            kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]    == True:
            kkimg_rct.centery +=1
        if key_states[pg.K_LEFT]    == True:
            kkimg_rct.centerx -=1
        if key_states[pg.K_RIGHT]   == True:
            kkimg_rct.centerx +=1
        


        if check_bound(kkimg_rct,screen_rct) != (1,1):
            if key_states[pg.K_UP]      == True: kkimg_rct.centery += 1
            if key_states[pg.K_DOWN]    == True: kkimg_rct.centery -=1
            if key_states[pg.K_LEFT]    == True: kkimg_rct.centerx +=1
            if key_states[pg.K_RIGHT]   == True: kkimg_rct.centerx -=1
        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        bmimg_rct.move_ip(vx,vy)
        bmimg1_rct.move_ip(vx1,vy1)
        screen_sfc.blit(bmimg1_sfc,bmimg1_rct)
        screen_sfc.blit(bmimg_sfc,bmimg_rct)

        yoko1, tate1 = check_bound(bmimg1_rct,screen_rct)
        vx1*=yoko1
        vy1*=tate1




        yoko, tate = check_bound(bmimg_rct,screen_rct)
        vx*=yoko
        vy*=tate

        if kkimg_rct.colliderect(bmimg_rct):
            screen_sfc.blit(s,[10,5])  
            return
        if kkimg_rct.colliderect(bmimg1_rct):
            screen_sfc.blit(s,[10,5])  
            return

        end = end = time.time()
        dif = end - start 
        dif = math.floor(dif)
        text = font.render(str(dif),True,(64,255,63))
        screen_sfc.blit(text,[10,5])

        pg.display.update()
        clock.tick(10000)





def check_bound(rct, scr_rct):
    yoko , tate = +1 , +1
    if rct.left < scr_rct.left or scr_rct.right < rct.right : yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1
    return yoko , tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit
    sys.exit