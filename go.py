import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 700))
DISPLAYSURF.fill((255, 255, 255))
pygame.display.set_caption('go!')

#set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BLOCK_SIZE = 35

def init_board():
    dot_loc = [3, 9, 15]
    for i in range(18):
        for j in range(18):
            pygame.draw.rect(DISPLAYSURF, BLACK, (10 + i * BLOCK_SIZE, 10 + j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
            if (i in dot_loc and j in dot_loc):
                pygame.draw.circle(DISPLAYSURF, BLACK, (10 + i * BLOCK_SIZE, 10 + j * BLOCK_SIZE), 4, 0)
    return 0


if (__name__ == '__main__'):
    init_board()
    while (True):
        mouseClicked = False
        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                sys.exit()
            elif (event.type == MOUSEBUTTONUP):
                 (mousex, mousey) = event.pos
                 mouseClicked = True
        pygame.display.update()
