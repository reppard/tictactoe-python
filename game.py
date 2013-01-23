import random
import pygame, sys
from pygame.locals import *

pygame.init()
box_color = (255,255,255)
box_border = (80,153,105)
screen = pygame.display.set_mode((300,500),0,32)
blank_piece = pygame.image.load("blank.jpg").convert()
x_piece = pygame.image.load("x.jpg").convert()
o_piece = pygame.image.load("o.jpg").convert()
triplets = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
# Game Setup

def get_empty_grid():
    return { 1 : None, 2 : None, 3 : None,
             4 : None, 5 : None, 6 : None,
             7 : None, 8 : None, 9 : None }

def new_board():
    return { 1 : [blank_piece,(0,0)], 2 : [blank_piece,(100,0)], 3 : [blank_piece,(200,0)],
             4 : [blank_piece,(0,100)], 5 : [blank_piece,(100,100)], 6 : [blank_piece,(200,100)],
             7 : [blank_piece,(0,200)], 8 : [blank_piece,(100,200)], 9 : [blank_piece,(200,200)] }

def setup_board(pieces):
    for key,value in pieces.iteritems():
        screen.blit(value[0],value[1])

def new_game():
    global grid, pieces
    grid = get_empty_grid()
    pieces = new_board()
    setup_board(pieces)

grid = get_empty_grid()
pieces = new_board()
setup_board(pieces)
player_one_score = 0
player_two_score = 0
turn = 1

#Player and Move logic

def winner():
    for a, b, c in triplets:
        if grid[a] == grid[b] == grid[c] and grid[a] is not None:
            return True

def whos_turn():
    if turn == 1:
        return "Player X's turn"
    else:
        return "Player O's turn"

def player_move(pos):
    for key,value in pieces.iteritems():
        for x in range(value[1][0], value[1][0] + 100):
            for y in range(value[1][1], value[1][1] + 100):
                if pos[0] == x and pos[1] == y:
                    if grid[key] == None:
                        return key
                    else:
                        return False

while True: #Main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if turn == 1:
                play = player_move(pygame.mouse.get_pos())
                if not (play == False):
                    grid[play] = "X"
                    pieces[play][0] = x_piece
                    screen.blit(pieces[play][0],pieces[play][1])
                    if not (winner() == True):
                        turn = 2
                        print grid
                    else:
                        player_one_score += 1
                        new_game()
            elif turn == 2:
                play = player_move(pygame.mouse.get_pos())
                if not (play == False):
                    grid[play] = "O"
                    pieces[play][0] = o_piece
                    screen.blit(pieces[play][0],pieces[play][1])
                    if not (winner() == True):
                        turn = 1
                        print grid
                    else:
                        player_two_score += 1
                        new_game()
        if event.type == KEYDOWN:
            if event.key == K_c:
                new_game()
    font = pygame.font.Font(None, 24)
    info = font.render("X-Score: " + str(player_one_score) + "    O-Score: " + str(player_two_score),1,box_border)
    go  = font.render(whos_turn(),1,box_border)
    pygame.draw.rect(screen, box_border, (0, 300, 300, 200))
    pygame.draw.rect(screen, box_border, (0, 300, 300, 200))
    pygame.draw.rect(screen, box_color, (25, 325, 250, 150))
    screen.blit(info, (55,350))
    screen.blit(go, (145,450))
    pygame.display.update()

