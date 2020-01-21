# -*- coding:utf-8 -*-
import pygame
import pygame.mixer
from pygame.locals import *
import time
import datetime
import math
import sys

""" parameter """
WIDTH = 640 # 画面幅を設定
HIGHT = 480 # 画面高さを設定
dt_target1 = datetime.datetime(2020, 2, 18, 9, 0, 0, 0) # 卒論提出日時を設定
dt_target2 = datetime.datetime(2020, 2, 6, 17, 0, 0, 0) # 修論提出日時を設定


pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HIGHT))
# SCREEN = pygame.display.set_mode((WIDTH, HIGHT)，FULLSCREEN) # raspi用
CLOCK = pygame.time.Clock()


def main():
    #=== 初期設定 ===#
    pygame.display.set_caption("Countdown ver EVA") # タイトルバーに表示する文字
    font_7seg = pygame.font.Font('font/DSEG7ModernMini-BoldItalic.ttf', 50) # 7セグフォントの読み込み
    font_mincho20 = pygame.font.Font('font/AozoraMincho-bold.ttf', 20) # 明朝体フォントの読み込み
    font_mincho30 = pygame.font.Font('font/AozoraMincho-bold.ttf', 35) # 明朝体フォントの読み込み
    # font1 = pygame.font.SysFont('arial', 50)
    font1 = pygame.font.SysFont('arial', 35, bold=True) # raspi用
    font2 = pygame.font.SysFont('arial', 20, bold=True) # raspi用
    cnt = 0 # カウンタの初期化

    #=== 音楽の再生 ===#
    pygame.mixer.init(frequency = 44100)
    # pygame.mixer.music.load("music/yashima.mp3")
    pygame.mixer.music.load("music/01 3EM01_EM20_Master.mp3")
    pygame.mixer.music.play(-1)

    #=== timedelta型から日数，時間，分，秒，ミリ秒を抽出 ===#
    def get_time(sec):
        td = datetime.timedelta(seconds=sec)
        m, s = divmod(td.seconds, 60)
        h, m = divmod(m, 60)
        ms = td.microseconds / 1000
        return td.days, h, m, s, ms

    while (1):
        CLOCK.tick(30) # 画面の更新頻度(fps)
        SCREEN.fill((0,0,0)) # 画面を黒色に塗りつぶし
        dt_now = datetime.datetime.now() # 現在時刻を取得
        dt_delta1 = (dt_target1 - dt_now).total_seconds() # 締め切りまでの時間を秒で取得

        cnt += 1 # カウンタのカウント
        if cnt == 6:cnt = 0 # 30ごとにカウンタを初期化

        #=== テキストの指定 ===#
        title1 = font_mincho30.render("卒論提出まであと", True, (248, 169, 0))
        title2 = font1.render("ACTIVE TIME REMAINING:", True, (248, 169, 0))
        alert1 = font1.render("DANGER", True, (247, 16, 0))
        alert2 = font1.render("EMERGENCY", True, (247, 16, 0))
        countdown1 = font_7seg.render("{0[0]:02d}  {0[1]:02d}    {0[2]:02d}  {0[3]:02d}  {0[4]:03.0f}".format(get_time(dt_delta1)), True, (247,214,0))
        unit1 = font2.render("           d                       h                 m                   s                         ms", True, (248, 169, 0))
        unit2 = font_mincho20.render("        日              時間             分              秒                    粍", True, (248, 169, 0))

        #=== 点滅部分の描画 ===#
        if(cnt == 0 or cnt == 1 or cnt == 2):
            # alertのテキストと枠描画
            SCREEN.blit(alert1, [35, 95])
            # pygame.draw.rect(SCREEN, (247, 16, 0), Rect(20, 99, 152, 33), 3)
            pygame.draw.rect(SCREEN, (247, 16, 0), Rect(20, 99, 152, 33), 3) # raspi用
            SCREEN.blit(alert2, [200, 95])
            # pygame.draw.rect(SCREEN, (247, 16, 0), Rect(180, 99, 224, 33), 3)
            pygame.draw.rect(SCREEN, (247, 16, 0), Rect(180, 99, 224, 33), 3) # raspi用
            # 斜め線の描画
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 50), (640, -50), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 100), (640, 0), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 150), (640, 50), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (580, 160), (640, 100), 30)

        #=== テキストと枠の描画 ===#
        pygame.draw.rect(SCREEN, (0, 0, 0), Rect(540, 0, 100, 155), 30)
        SCREEN.blit(title1, [20, 20])
        SCREEN.blit(title2, [20, 55])
        SCREEN.blit(countdown1, [49, 160])
        SCREEN.blit(unit1, [85, 160])
        SCREEN.blit(unit2, [85, 190])
        pygame.draw.rect(SCREEN, (248, 169, 0), Rect(10, 10, 620, 210), 3)

        dt_delta2 = (dt_target2 - dt_now).total_seconds() # 締め切りまでの時間を秒で取得

        #=== テキストの指定 ===#
        title3 = font_mincho30.render("修論提出まであと", True, (248, 169, 0))
        countdown2 = font_7seg.render("{0[0]:02d}  {0[1]:02d}    {0[2]:02d}  {0[3]:02d}  {0[4]:03.0f}".format(get_time(dt_delta2)), True, (247,214,0))
        unit1 = font2.render("           d                       h                 m                   s                         ms", True, (248, 169, 0))
        unit2 = font_mincho20.render("        日              時間             分              秒                    粍", True, (248, 169, 0))

        #=== 点滅部分の描画 ===#
        if(cnt == 0 or cnt == 1 or cnt == 2):
            # alertのテキストと枠描画
            SCREEN.blit(alert1, [35, 335])
            pygame.draw.rect(SCREEN, (247, 16, 0), Rect(20, 339, 152, 33), 3) # raspi用
            SCREEN.blit(alert2, [200, 335])
            pygame.draw.rect(SCREEN, (247, 16, 0), Rect(180, 339, 224, 33), 3) # raspi用
            # 斜め線の描画
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 290), (590, 240), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 340), (640, 240), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (540, 390), (640, 290), 30)
            pygame.draw.line(SCREEN, (247, 16, 0), (580, 400), (640, 340), 30)

        #=== テキストと枠の描画 ===#
        pygame.draw.rect(SCREEN, (0, 0, 0), Rect(540, 240, 100, 155), 30)
        SCREEN.blit(title3, [20, 260])
        SCREEN.blit(title2, [20, 295])
        SCREEN.blit(countdown2, [49, 400])
        SCREEN.blit(unit1, [85, 400])
        SCREEN.blit(unit2, [85, 430])
        pygame.draw.rect(SCREEN, (248, 169, 0), Rect(10, 250, 620, 210), 3)

        pygame.display.update() # 画面を更新

        #=== イベント処理 ===#
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
