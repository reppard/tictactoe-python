import random
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((300,500),0,32)

blank_piece = pygame.image.load("blank.jpg").convert()
x_piece = pygame.image.load("x.jpg").convert()
o_piece = pygame.image.load("o.jpg").convert()
turn = 1

def get_empty_grid():
    return {1 : None, 2 : None, 3 : None,
            4 : None, 5 : None, 6 : None,
            7 : None, 8 : None, 9 : None}

def new_board():
    return { 1 : [blank_piece,(0,0)], 2 : [blank_piece,(100,0)], 3 : [blank_piece,(200,0)],
             4 : [blank_piece,(0,100)], 5 : [blank_piece,(100,100)], 6 : [blank_piece,(200,100)],
             7 : [blank_piece,(0,200)], 8 : [blank_piece,(100,200)], 9 : [blank_piece,(200,200)] }

def winner():
    if grid[1] == grid[2] and grid[3]:
        print "WINNER!"

grid = get_empty_grid()
pieces = new_board()

def setup_board(pieces):
    for key,value in pieces.iteritems():
        screen.blit(value[0],value[1])

def player_one_move(pos):
    for key,value in pieces.iteritems():
        for x in range(value[1][0], value[1][0] + 100):
            for y in range(value[1][1], value[1][1] + 100):
                if pos[0] == x and pos[1] == y:
                    return key

def player_two_move(pos):
    for key,value in pieces.iteritems():
        for x in range(value[1][0], value[1][0] + 100):
            for y in range(value[1][1], value[1][1] + 100):
                if pos[0] == x and pos[1] == y:
                    return key

def comp_move(pieces):
    free_spaces = []
    for key,value in pieces.iteritems():
        if value[0] == blank_piece:
            free_spaces.append(key)
        if len(free_spaces) > 0:
            return random.choice(free_spaces)

setup_board(pieces)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if turn == 1:
                play = player_one_move(pygame.mouse.get_pos())
                grid[play] = "X"
                pieces[play][0] = x_piece
                screen.blit(pieces[play][0],pieces[play][1])
                turn = 2
                print grid
            elif turn == 2:
                play = player_two_move(pygame.mouse.get_pos())
                grid[play] = "O"
                pieces[play][0] = o_piece
                screen.blit(pieces[play][0],pieces[play][1])
                turn = 1
                print grid
          # comp = comp_move(pieces)
          # pieces[comp][0] = o_piece
          # screen.blit(pieces[comp][0],pieces[comp][1])
        if event.type == KEYDOWN:
            if event.key == K_c:
                setup_board(new_board())
    pygame.display.update()

