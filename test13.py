# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:21:47 2016

@author: student
"""

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)

background=pygame.image.load('D:/2/sushiplate.jpg').convert()
sprite=pygame.image.load('D:/2/fugu.png')

clock=pygame.time.Clock()

x=0.
y=0.

speed_x=250.
speed_y=150.

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    screen.blit(background,(0,0))
    screen.blit(sprite,(x,y))
    
    time_passed=clock.tick(30)
    time_passed_seconds=time_passed/1000.0
    
    distance_moved_x=time_passed_seconds*speed_x
    distance_moved_y=time_passed_seconds*speed_y
    x+=distance_moved_x
    y+=distance_moved_y
    
    if x>640.:
        x=0.
    if y>480.:
        y=0.
    pygame.display.update()