import pygame
from math import sqrt,pi,cos,sin

def draw_blue(surface,pos):
    x = pos[0]
    y = pos[1]
    pygame.draw.polygon(surface=surface
                        , color=(0,0,255)
                        , points=[(120+(x+y-2)*80+50*cos(pi*i/3),500+(x-y)*46+50*sin(pi*i/3)) for i in range(6)])