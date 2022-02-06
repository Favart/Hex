import pygame
from math import sqrt,pi,cos,sin

def draw_red(surface,pos):
    x = pos[0]
    y = pos[1]
    pygame.draw.polygon(surface=surface
                        , color=(255,0,0)
                        , points=[(120+(x+y-2)*80+50*cos(pi*i/3),500+(x-y)*46+50*sin(pi*i/3)) for i in range(6)])