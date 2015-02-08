#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import *
GAME_MAINMENU = 1
GAME_MAINGAME = 2
GAME_MAINGAME_PAUSE = 3
GAME_MAINGAME_OVER = 4
gamemode = GAME_MAINMENU
arrow = 0
color_rgb = [0, 0, 0]
pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("MoonWorld")
while True:
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
                else:
                    exit(1)
        if event_check.type == KEYDOWN and gamemode == GAME_MAINGAME:
            if event_check.key == K_a:
                color_rgb[0] = 255
            if event_check.key == K_s:
                color_rgb[1] = 255
            if event_check.key == K_d:
                color_rgb[2] = 255
        if event_check.type == KEYUP and gamemode == GAME_MAINGAME:
            if event_check.key == K_a:
                color_rgb[0] = 0
            if event_check.key == K_s:
                color_rgb[1] = 0
            if event_check.key == K_d:
                color_rgb[2] = 0
    if(gamemode == GAME_MAINMENU):
        titlefont = pygame.font.SysFont("arial", 40)
        title_surface = titlefont.render("COLOR WARRIOR", True, (0, 0, 0))
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
    pygame.display.flip()
    screen.fill(pygame.Color(255, 255, 255))
    #pygame.display.update()
