# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 16:21:44 2016

@author: student
"""
import pygame
from pygame.locals import *
from sys import exit
backgound_image_filename='d:/2/sushiplate.jpg'
mouse_image_filename='d:/2/fugu.png'
pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Hello, World!")
background=pygame.image.load(backgound_image_filename)
mouse_cursor=pygame.image.load(mouse_image_filename)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
    screen.blit(background,(0,0))
    x,y=pygame.mouse.get_pos()
    x-=mouse_cursor.get_width()/2
    y-=mouse_cursor.get_height()/2
    screen.blit(mouse_cursor,(x,y))
    pygame.display.update()
