#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import *
import random
GAME_MAINMENU = 1
GAME_MAINGAME = 2
GAME_MAINGAME_PAUSE = 3
GAME_MAINGAME_OVER = 4
gamemode = GAME_MAINMENU
arrow = 0
score = 0
total_game_sec = 0.0
flush_sec = 0.0
color_rgb = [0, 0, 0, 255]
danegrousguys = []
speed = 150
level = 1
flushtime = 1000
pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
background = pygame.image.load("bg.png").convert()
pygame.display.set_caption("COLOR WAR!MADE BY 42YEAH AND MOONMAGIAN")
pygame.mixer.music.load("war.ogg")
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
while True:
    time_passed = clock.tick(40)  # FPS limit for CPU protect.
    for event_check in pygame.event.get():
        if event_check.type == QUIT:
            exit(1)
        if event_check.type == KEYDOWN and gamemode == GAME_MAINMENU:
            print event_check.key
            if event_check.key == K_DOWN or event_check.key == K_UP:
                if arrow == 0:
                    arrow = 1
                elif arrow == 1:
                    arrow = 0
            elif event_check.key == K_RETURN:
                if arrow == 0:
                    gamemode = GAME_MAINGAME
                    total_game_sec = 0
                    score = 0
                    speed = 150
                    flushtime = 1500
                    level = 1
                    color_rgb = [0, 0, 0, 255]
                else:
                    exit(1)
        if event_check.type == KEYDOWN and gamemode == GAME_MAINGAME:
            if event_check.key == K_a:
                color_rgb[0] = 255
            if event_check.key == K_s:
                color_rgb[1] = 255
            if event_check.key == K_d:
                color_rgb[2] = 255
            if event_check.key == K_l:
                color_rgb[3] = 125
        if event_check.type == KEYUP and gamemode == GAME_MAINGAME:
            if event_check.key == K_a:
                color_rgb[0] = 0
            if event_check.key == K_s:
                color_rgb[1] = 0
            if event_check.key == K_d:
                color_rgb[2] = 0
            if event_check.key == K_l:
                color_rgb[3] = 255
    if(gamemode == GAME_MAINMENU):
        titlefont = pygame.font.SysFont("arial", 40)
        title_surface = titlefont.render("COLOR WAR", True, (0, 0, 0))
        screen.blit(title_surface, (0, 5))
        if arrow == 0:
            c1_surface = titlefont.render(">GAMESTART", True, (0, 0, 0))
        else:
            c1_surface = titlefont.render("  GAMESTART", True, (0, 0, 0))
        if arrow == 1:
            c2_surface = titlefont.render(">EXITGAME", True, (0, 0, 0))
        else:
            c2_surface = titlefont.render("  EXITGAME", True, (0, 0, 0))
        screen.blit(c1_surface, (0, title_surface.get_offset()[1] + title_surface.get_height() + 20))
        screen.blit(c2_surface, (0, title_surface.get_offset()[1] + title_surface.get_height() + c1_surface.get_height() + 20))
    elif(gamemode == GAME_MAINGAME):
        mainsurface = pygame.draw.rect(screen, color_rgb, pygame.Rect(0, 0, 200, 600))
        time_sec = time_passed / 1000.0
        total_game_sec = total_game_sec + time_sec
        flush_sec = flush_sec + time_sec
        if flush_sec >= random.randint(int(flushtime), int(flushtime + 500)) / 1000.0:
            random.seed()
            rgbtf = [0, 0, 0, 0]
            rgbtf[0] = random.randint(0, 1)
            random.seed()
            rgbtf[1] = random.randint(0, 1)
            random.seed()
            rgbtf[2] = random.randint(0, 1)
            rgbtf[3] = random.randint(0, 1)
            rgb = [0, 0, 0, 255]
            if rgbtf[0] == 1:
                rgb[0] = 255
            if rgbtf[1] == 1:
                rgb[1] = 255
            if rgbtf[2] == 1:
                rgb[2] = 255
            if rgbtf[3] == 1:
                rgb[3] = 125
            danegrousguys.append([800, random.randint(0, 510), pygame.Color(rgb[0], rgb[1], rgb[2]), random.randint(0, 100)])
            flush_sec = 0.0
        if total_game_sec >= 15:
            speed += 25
            flushtime -= 50
            print "LEVEL UP!"
            total_game_sec = 0
            level += 1
        dellist = []
        for enemies in range(len(danegrousguys)):
            danegrousguys[enemies][0] -= speed * time_sec
            pygame.draw.rect(screen, danegrousguys[enemies][2], pygame.Rect(danegrousguys[enemies][0], danegrousguys[enemies][1], 70, 70))
            if (danegrousguys[enemies][3] >= 70):
                pygame.draw.rect(screen, pygame.Color(150, 150, 150), pygame.Rect(danegrousguys[enemies][0], danegrousguys[enemies][1], 10, 10))
            if (danegrousguys[enemies][0] <= 200):
                if (danegrousguys[enemies][2] != pygame.Color(color_rgb[0], color_rgb[1], color_rgb[2]) and danegrousguys[enemies][3] <70) or (danegrousguys[enemies][3] >= 70 and danegrousguys[enemies][2] == pygame.Color(color_rgb[0], color_rgb[1], color_rgb[2])):
                    gamemode = GAME_MAINMENU
                    del danegrousguys[:]
                    break
                else:
                    dellist.append(danegrousguys[enemies])
                    score += 1
        for guys in dellist:
            del danegrousguys[danegrousguys.index(guys)]
        pygame.display.set_caption("COLOR WAR!MADE BY 42YEAH AND MOONMAGIAN    score:" + str(score) + "    level"+str(level))
    pygame.display.flip()
    screen.blit(background, (0, 0))
    #print time_passed
    #pygame.display.update()
