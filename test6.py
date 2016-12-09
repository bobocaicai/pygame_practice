# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 20:18:13 2016

@author: student
"""
import pygame
my_name='Hello World!'
pygame.init()
my_font=pygame.font.SysFont("youyuan",64)
#pygame.font.get_fonts()可以得到系统可用字体
name_surface=my_font.render(my_name,True,(0,0,0),(255,255,255))
pygame.image.save(name_surface,"d:/2/name1.png")