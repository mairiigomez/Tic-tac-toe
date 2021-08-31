"""Next, to make a branch to work on playing against the machine 
post it on github 
Figure out how to move MASTER to master on github 
Maybe show on the screen for a couple of seconds what is the start over key """


import pygame, sys
import numpy as np

pygame.init()

WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
CIRCLE_RADIOUS = SQUARE_SIZE//2 - SQUARE_SIZE//6
CIRCLE_WIDTH = 15
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE//4
# RGB colors, Red Green Blue
RED = (255,0,0)
BG_COLOR = (28,170,156)
LINE_COLOR = (23,145,135)
CROSS_COLOR = (66, 66, 66)
CIRCLE_COLOR = (250,250,250)
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )

board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0,SQUARE_SIZE),(WIDTH,SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0,2*SQUARE_SIZE),(WIDTH,2*SQUARE_SIZE), LINE_WIDTH)
    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE,0),(SQUARE_SIZE,HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (2*SQUARE_SIZE,0),(2*SQUARE_SIZE,HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                # SQUARE_SIZE and 100 values it is the value of the screen (x,y) divide it by 3 and by 6
                pygame.draw.circle( screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIOUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

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

def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col,player)
            return True

    # Horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    
    return False

def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    if player == 2:
        color = CROSS_COLOR 
    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    if player == 2:
        color = CROSS_COLOR 
    pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), 15)

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    if player == 2:
        color = CROSS_COLOR 
    pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    if player == 2:
        color = CROSS_COLOR 
    pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
    screen.fill( BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

draw_lines()

player = 1 
game_over = False

# Main loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x coordinate
            mouseY = event.pos[1] # y coordinate 

            click_row = int(mouseY//SQUARE_SIZE)
            click_col = int(mouseX//SQUARE_SIZE)

            if available_square( click_row, click_col ):
                mark_square( click_row, click_col, player)
                if check_win(player):
                    game_over = True
                
                # Change to the other player
                player = player % 2 + 1

                draw_figures()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1 
    
    # Update the display always
    pygame.display.update()

 