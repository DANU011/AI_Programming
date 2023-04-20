import pygame
import sys
from pygame.locals import *
from util import *

# 프로그램 종료 된다는게 os는 어떻게 알고 있나요?
# int main()
# {
# return -1;
# }

def check_events():
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def draw_text_center(surface, text, font, x, y):
    text_obj = font.render(text,1,RED)
    text_rect = text_obj.get_rect()
    text_rect.center = (x,y)
    surface.blit(text_obj, text_rect)
    
def draw_text_top_left(surface, text, color, font, x, y):
    text_obj = font.render(text,1,color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(text_obj, text_rect)

def draw_dividers(surface,DIVDERS):
    for x1,y1,x2,y2 in DIVDERS:
        pygame.draw.aaline(surface, WHITE, (x1,y1),(x2,y2))



def draw_??(surface, cities):