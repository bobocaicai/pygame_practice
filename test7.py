# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 20:26:08 2016

@author: student
"""
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
background=pygame.image.load('d:/2/sushiplate.jpg').convert()
font_all=pygame.font.get_fonts()
font=pygame.font.SysFont(font_all[55],40)
text_surface=font.render(u'你好',True,(0,0,255))

x=0
y=(480-text_surface.get_height())/2

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    screen.blit(background,(0,0))
    x-=0.05
    if x<-text_surface.get_width():
        x=640-text_surface.get_width()
        
    screen.blit(text_surface,(x,y))
    pygame.display.update()
