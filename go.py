import pygame, sys, os
import time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((900, 768))
DISPLAYSURF.fill((255, 255, 255))
pygame.display.set_caption('go!')

#set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (255, 222, 173)

BLOCK_SIZE = 37
BOARD_INIT = 22
EPS = 7
CHESS = [[0 for x in range(19)] for x in range(19)]

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)

    if (image == None):
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return pygame.transform.scale(image, (704, 704))

def init_board():
    dot_loc = [3, 9, 15]
    for i in range(18):
        for j in range(18):
            pygame.draw.rect(DISPLAYSURF, BLACK, (BOARD_INIT + i * BLOCK_SIZE, BOARD_INIT + j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
            if (i in dot_loc and j in dot_loc):
                pygame.draw.circle(DISPLAYSURF, BLACK, (BOARD_INIT + i * BLOCK_SIZE, BOARD_INIT + j * BLOCK_SIZE), 4, 0)
    pygame.draw.rect(DISPLAYSURF, (0, 100, 0), (750, 350, 80, 80), 0)
    pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (750, 500, 80, 80), 0)
    return 0

def update_board():
    DISPLAYSURF.fill((230, 230, 255))
    DISPLAYSURF.blit(get_image('board2.jpg'), (3, 3))
    init_board()
    for i in range(19):
        for j in range(19):
            if (CHESS[i][j] == 1):
                pygame.draw.circle(DISPLAYSURF, BLACK, (BOARD_INIT + i * BLOCK_SIZE, BOARD_INIT + j * BLOCK_SIZE), 17, 0)
            elif (CHESS[i][j] == 3):
                pygame.draw.circle(DISPLAYSURF, WHITE, (BOARD_INIT + i * BLOCK_SIZE, BOARD_INIT + j * BLOCK_SIZE), 17, 0)
            else:
                continue
            pygame.draw.circle(DISPLAYSURF, BLACK, (BOARD_INIT + i * BLOCK_SIZE, BOARD_INIT + j * BLOCK_SIZE), 18, 2)
    return

def loc_mod(x):
    mod = (x - BOARD_INIT) % BLOCK_SIZE
    if (mod > EPS and BLOCK_SIZE - mod > EPS):
        return -1
    ret = (x - BOARD_INIT) // BLOCK_SIZE
    if (mod > BLOCK_SIZE // 2):
        ret += 1
    return ret

def go(mx, my, t):
    x = loc_mod(mx)
    y = loc_mod(my)
    if (x == -1 or y == -1):
        return -1
    if (CHESS[x][y] != 0):
        return -1
    CHESS[x][y] = t
    return 0
    
def erase(mx, my):
    x = (mx - BOARD_INIT) // BLOCK_SIZE
    if ((mx - BOARD_INIT) % BLOCK_SIZE > BLOCK_SIZE // 2):
        x += 1
    y = (my - BOARD_INIT) // BLOCK_SIZE
    if ((my - BOARD_INIT) % BLOCK_SIZE > BLOCK_SIZE // 2):
        y += 1
    CHESS[x][y] = 0
    return 0

def clear():
    for i in range(19):
        for j in range(19):
            CHESS[i][j] = 0
    return 0

def is_clear(x, y):
    #TODO
    if (x > 750 and x < 750 + 80 and y > 350 and y < 350 + 80):
        return True
    return False

def is_end(x, y):
    if (x > 750 and x < 750 + 80 and y > 500 and y < 500 + 80):
        return True
    return False

if (__name__ == '__main__'):
    init_board()
    f_end = False
    while (f_end == False):
        mouseClicked = False
        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                sys.exit()
            elif (event.type == MOUSEBUTTONUP):
                 (mousex, mousey) = event.pos
                 if (event.button == 1):
                     if (is_clear(mousex, mousey) == True):
                         clear()
                         continue
                     if (is_end(mousex, mousey) == True):
                         f_end = True
                         break
                     go(mousex, mousey, 1)
                 elif (event.button == 3):
                     go(mousex, mousey, 3)
                 else:
                     erase(mousex, mousey)
        update_board()
        pygame.display.update()
        time.sleep(0.1)
