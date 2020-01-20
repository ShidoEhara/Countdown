# -*- coding:utf-8 -*-
import pygame
import pygame.mixer
from pygame.locals import *
import time
import datetime
import math
import sys

pygame.init()
SCREEN = pygame.display.set_mode((640, 480))
CLOCK = pygame.time.Clock()


def main():
    """ main routine """
    pygame.display.set_caption("Countdown ver EVA")          # タイトルバーに表示する文字
    font_7seg = pygame.font.Font('DSEG7ModernMini-BoldItalic.ttf', 50)
    font_mincho = pygame.font.Font('ipam.ttf', 20)
    font1 = pygame.font.SysFont('arial', 50)               # フォントの設定(40px)
    font2 = pygame.font.SysFont('arial', 150)               # フォントの設定(40px)
    font3 = pygame.font.SysFont('ヒラキノ角コシックw3ttc', 20)
    cnt = 0

    """ target day """
    dt_target1 = datetime.datetime(2020, 2, 18, 9, 0, 0, 0)
    dt_target2 = datetime.datetime(2020, 1, 27, 15, 0, 0, 0)

    def get_time(sec):
        td = datetime.timedelta(seconds=sec)
        m, s = divmod(td.seconds, 60)
        h, m = divmod(m, 60)
        ms = td.microseconds / 1000
        return td.days, h, m, s, ms

# import datetime
# now = datetime.datetime.now()
# target = datetime.datetime(2020, 2, 18, 0, 0, 0, 0)
# delta = target - now
# dsec = delta.total_seconds()
# def get_time(sec):
#     td = datetime.timedelta(seconds=sec)
#     m, s = divmod(td.seconds, 60)
#     h, m = divmod(m, 60)
#     ms = td.microseconds / 1000
#     return td.days, h, m, s, ms
# print(delta)
# # print("{0} {1:3.0f}".format(delta.days, delta.hour, delta.mindelta.microseconds/1000))
# print(get_time(dsec))
# print("{0[0]:02d}d {0[1]:02d}h {0[2]:02d}m {0[3]:02d}s {0[4]:03.0f}ms".format(get_time(dsec)))

    while (1):
        CLOCK.tick(30) # 画面の更新頻度(fps)
        SCREEN.fill((0,0,0)) # 画面を黒色に塗りつぶし
        dt_now = datetime.datetime.now() # 現在時刻を取得
        dt_delta1 = (dt_target1 - dt_now).total_seconds() # 締め切りまでの時間を秒で取得

        cnt += 1 # カウンタのカウント
        if cnt == 30:cnt = 0 # 30ごとにカウンタを初期化

        title1 = font_mincho.render("卒論提出まであと", True, (248, 169, 0))
        title2 = font1.render("ACTIVE TIME REMAINING:", True, (248, 169, 0))
        alert1 = font1.render("DANGER", True, (247, 16, 0))
        alert2 = font1.render("EMERGENCY", True, (247, 16, 0))
        countdown1 = font_7seg.render("{0[0]:02d}  {0[1]:02d}    {0[2]:02d}  {0[3]:02d}  {0[4]:03.0f}".format(get_time(dt_delta1)), True, (247,214,0))
        unit1 = font_mincho.render("         d           h         m          s            ms", True, (248, 169, 0))
        unit2 = font_mincho.render("        日        時間        分         秒            耗", True, (248, 169, 0))

        if(cnt % 2 == 1):
            SCREEN.blit(alert1, [20, 100])
            pygame.draw.rect(SCREEN, (247, 16, 0), Rect(20, 99, 152, 33), 3)
            SCREEN.blit(alert2, [180, 100])
            pygame.draw.rect(SCREEN, (247, 16, 0), Rect(180, 99, 224, 33), 3)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 50), (640, -50), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 100), (640, 0), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 150), (640, 50), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (580, 160), (640, 100), 30)

        pygame.draw.rect(SCREEN, (0, 0, 0), Rect(540, 0, 100, 155), 30)

        SCREEN.blit(title1, [20, 20])
        SCREEN.blit(title2, [20, 50])
        SCREEN.blit(countdown1, [19, 160])
        SCREEN.blit(unit1, [20, 160])
        SCREEN.blit(unit2, [20, 190])

        pygame.draw.rect(SCREEN, (248, 169, 0), Rect(10, 10, 620, 210), 3)


        dt_delta2 = (dt_target2 - dt_now).total_seconds() # 締め切りまでの時間を秒で取得

        title3 = font_mincho.render("修論提出まであと", True, (248, 169, 0))
        countdown2 = font_7seg.render("{0[0]:02d}  {0[1]:02d}    {0[2]:02d}  {0[3]:02d}  {0[4]:03.0f}".format(get_time(dt_delta2)), True, (247,214,0))
        unit1 = font_mincho.render("         d           h         m          s            ms", True, (248, 169, 0))
        unit2 = font_mincho.render("        日        時間        分         秒            耗", True, (248, 169, 0))

        if(cnt % 2 == 1):
            SCREEN.blit(alert1, [20, 340])
            pygame.draw.rect(SCREEN, (247, 16, 0), Rect(20, 339, 152, 33), 3)
            SCREEN.blit(alert2, [180, 340])
            pygame.draw.rect(SCREEN, (247, 16, 0), Rect(180, 339, 224, 33), 3)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 290), (590, 240), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 340), (640, 240), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 390), (640, 290), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (580, 400), (640, 340), 30)

        pygame.draw.rect(SCREEN, (0, 0, 0), Rect(540, 240, 100, 155), 30)

        SCREEN.blit(title3, [20, 260])
        SCREEN.blit(title2, [20, 290])
        SCREEN.blit(countdown2, [19, 400])
        SCREEN.blit(unit1, [20, 400])
        SCREEN.blit(unit2, [20, 430])

        pygame.draw.rect(SCREEN, (248, 169, 0), Rect(10, 250, 620, 210), 3)

        pygame.display.update()     # 画面を更新

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
