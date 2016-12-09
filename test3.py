# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 17:01:18 2016

@author: student
"""
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
Screen_size=(640,480)
screen=pygame.display.set_mode(Screen_size,0,32)

font=pygame.font.SysFont("arial",16)
font_height=font.get_linesize()
event_text=[]

while True:
    event=pygame.event.wait()
    event_text.append(str(event))
    event_text=event_text[-Screen_size[1]/font_height:]
    
    if event.type==QUIT:
        exit()
    screen.fill((0,0,0))
    y=Screen_size[1]-font_height
    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,255,0)),(0,y))
        y-=font_height
    pygame.display.update()
