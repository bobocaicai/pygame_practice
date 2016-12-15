# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:52:14 2016

@author: student
"""

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)

background=pygame.image.load('D:/2/sushiplate.jpg').convert()
sprite=pygame.image.load('D:/2/fugu.png')

x=0.
y=100.
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        screen.blit(background,(0,0))
        screen.blit(sprite,(x,y))
        x+=10
        y+=1
        
        if x>640.:
            x=0
        if y>480.:
            y=100
        pygame.display.update()