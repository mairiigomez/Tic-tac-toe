import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
# RGB colors, Red Green Blue
RED = (255,0,0)
BG_COLOR = (28,170,156)
LINE_COLOR = (23,145,135)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )

board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0,200),(600,200), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0,400),(600,400), LINE_WIDTH)
    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (200,0),(200,600), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (400,0),(400,600), LINE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row,col):
    return board[row][col] == 0
    # if board[row][col] == 0:
    #     return True
    # else: 
    #     return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.update()

"Verify is the new functions work"  

 