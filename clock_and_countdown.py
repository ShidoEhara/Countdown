# -*- coding:utf-8 -*-
import pygame
import pygame.mixer
from pygame.locals import *
import time
from datetime import datetime, timedelta, timezone
import sys

""" parameter """
WIDTH = 640 # 画面幅を設定
HEIGHT = 480 # 画面高さを設定
dt_target1 = datetime(2020, 10, 16, 9, 0, 0, 0) # コアタイムを設定
YAMABUKI = (248, 169, 0)
YELLOW = (247,214,0)
RED = (247, 16, 0)


pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN) # raspi用
CLOCK = pygame.time.Clock()


def main():
    #=== 初期設定 ===#
    pygame.display.set_caption("Countdown ver EVA") # タイトルバーに表示する文字
    font_7segL = pygame.font.Font('font/DSEG7ModernMini-BoldItalic.ttf', 80) # 7セグフォントの読み込み
    font_7segM = pygame.font.Font('font/DSEG7ModernMini-BoldItalic.ttf', 55) # 7セグフォントの読み込み
    font_7segS = pygame.font.Font('font/DSEG7ModernMini-BoldItalic.ttf', 30) # 7セグフォントの読み込み
    font_minchoL = pygame.font.Font('font/AozoraMincho-bold.ttf', 60) # 明朝体フォントの読み込み
    font_minchoM = pygame.font.Font('font/AozoraMincho-bold.ttf', 40) # 明朝体フォントの読み込み
    font_minchoS = pygame.font.Font('font/AozoraMincho-bold.ttf', 20) # 明朝体フォントの読み込み
    font_L = pygame.font.SysFont('arial', 60, bold=True)
    font_M = pygame.font.SysFont('arial', 40, bold=True)
    font_S = pygame.font.SysFont('arial', 20, bold=True) # raspi用
    cnt = 0 # カウンタの初期化

    #=== 音楽の再生 ===#
    pygame.mixer.init(frequency = 44100)
    # pygame.mixer.music.load("music/yashima.mp3")
    # pygame.mixer.music.load("music/01 3EM01_EM20_Master.mp3")
    pygame.mixer.music.load("music/evangelion_OST.mp3")
    pygame.mixer.music.play(-1)

    #=== timedelta型から日数，時間，分，秒，ミリ秒を抽出 ===#
    def get_time(sec):
        td = timedelta(seconds=sec)
        m, s = divmod(td.seconds, 60)
        h, m = divmod(m, 60)
        h += td.days*24
        ms = td.microseconds / 1000
        if h <= -100 or h >= 100:
            h, m, s, ms = 88, 88, 88, 88
        return h, m, s

    while (1):
        CLOCK.tick(30) # 画面の更新頻度(fps)
        SCREEN.fill((0,0,0)) # 画面を黒色に塗りつぶし
        dt_now = datetime.now() # 現在時刻を取得
        utc_now = datetime.now(timezone.utc) # 現在時刻を標準時で取得
        dt_delta1 = (dt_target1 - dt_now).total_seconds() # 締め切りまでの時間を秒で取得

        # cnt += 1 # カウンタのカウント
        # if cnt == 3:cnt = 0 # 3ごとにカウンタを初期化

        #=== 日本標準時の描画 ===#
        title1 = font_minchoL.render("日本標準時", True, YAMABUKI)
        title2 = font_S.render("Japan Standard Time", True, YAMABUKI)
        title3 = font_M.render("Live", True, YAMABUKI)
        date = font_7segL.render(dt_now.strftime("%H  %M  %S"), True, YELLOW)
        unit1 = font_M.render(" h              m              s", True, YAMABUKI)
        unit2 = font_minchoM.render("時          分           秒", True, YAMABUKI)
        # alert1 = font_L.render("DANGER", True, (RED))
        # alert1 = font_L.render("WARNING", True, (RED))

        pygame.draw.rect(SCREEN, (0, 0, 0), Rect(540, 0, 100, 155), 30)
        SCREEN.blit(title1, [20, 20])
        SCREEN.blit(title2, [90, 80])
        SCREEN.blit(title3, [70, 115])
        SCREEN.blit(date, [105, 140])
        SCREEN.blit(unit1, [225, 135])
        SCREEN.blit(unit2, [230, 180])
        pygame.draw.line(SCREEN, YAMABUKI, (15, 20), (15, 95), 6)
        pygame.draw.line(SCREEN, YAMABUKI, (330, 20), (330, 95), 6)
        # pygame.draw.rect(SCREEN, YAMABUKI, Rect(60, 110, 560, 100), 3)

        pygame.draw.line(SCREEN, YAMABUKI, (60, 110), (60, 140), 10)
        pygame.draw.line(SCREEN, YAMABUKI, (60, 140), (70, 150), 10)
        pygame.draw.line(SCREEN, YAMABUKI, (70, 150), (70, 200), 10)
        pygame.draw.line(SCREEN, YAMABUKI, (70, 200), (100, 230), 10)
        pygame.draw.line(SCREEN, YAMABUKI, (100, 229), (620, 229), 3)
        pygame.draw.line(SCREEN, YAMABUKI, (620, 230), (620, 130), 10)
        pygame.draw.line(SCREEN, YAMABUKI, (620, 131), (200, 131), 3)
        pygame.draw.line(SCREEN, YAMABUKI, (202, 132), (180, 110), 10)
        pygame.draw.line(SCREEN, YAMABUKI, (60, 111), (180, 111), 3)

        # if(cnt == 1):
            # SCREEN.blit(alert1, [370, 20])

        #=== 作戦開始時間の描画 ===#
        mst_jp = font_minchoM.render("作戦開始時間", True, YAMABUKI)
        mst_en = font_S.render("H - hour", True, YAMABUKI)
        mst_date = font_7segM.render("{0[0]:02d}:{0[1]:02d}:{0[2]:02d}".format(get_time(dt_delta1)), True, YELLOW)

        SCREEN.blit(mst_jp, [20, 270])
        SCREEN.blit(mst_en, [105, 310])
        SCREEN.blit(mst_date, [310, 270])
        pygame.draw.line(SCREEN, YAMABUKI, (15, 270), (15, 325), 6)
        pygame.draw.line(SCREEN, YAMABUKI, (265, 270), (265, 325), 6)

        #=== 世界標準時の描画 ===#
        gmt_jp = font_minchoM.render("世界標準時", True, YAMABUKI)
        gmt_en = font_S.render("Greenwich Mean Time", True, YAMABUKI)
        gmt_date = font_7segM.render(utc_now.strftime("%H:%M:%S"), True, YELLOW)

        SCREEN.blit(gmt_jp, [60, 380])
        SCREEN.blit(gmt_en, [75, 420])
        SCREEN.blit(gmt_date, [310, 380])
        pygame.draw.line(SCREEN, YAMABUKI, (55, 380), (55, 435), 6)
        pygame.draw.line(SCREEN, YAMABUKI, (265, 380), (265, 435), 6)

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
