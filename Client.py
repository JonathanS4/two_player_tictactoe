import socket, atexit
host='localhost'
port=4445
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

def close():
    s.close()
atexit.register(close)

import pygame
import pygame, random

pygame.init()
from pygame.locals import *

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-Tac-Toe P2')
start = (0, 0)
turn = 1
a = None
cords = [[75, 75], [275, 75], [475, 75],
         [75, 275], [275, 275], [475, 275],
         [75, 475], [275, 475], [475, 475]]
TP = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def X(start):
    pygame.draw.line(screen, 'white', start, (start[0] + 50, start[1] + 50), 5)
    pygame.draw.line(screen, 'white', (start[0] + 50, start[1]), (start[0], start[1] + 50), 5)

def Circle(start):
    pygame.draw.circle(screen, 'white', (start[0] + 25, start[1] + 25), 50, 5)

def placement(x,y):
    x=int(x)
    y=int(y)
    global turn
    if (0 < x < 200 and 0 < y < 200) and TP[0]==0:
        if turn % 2 == 0:
            TP[0] = 2
        else:
            TP[0] = 1
        turn += 1
    elif (200 < x < 400 and 0 < y < 200) and TP[1]==0:
        if turn % 2 == 0:
            TP[1] = 2
        else:
            TP[1] = 1
        turn += 1
    elif (400 < x < 600 and 0 < y < 200) and TP[2]==0:
        if turn % 2 == 0:
            TP[2] = 2
        else:
            TP[2] = 1
        turn += 1
    elif (0 < x < 200 and 200 < y < 400) and TP[3]==0:
        if turn % 2 == 0:
            TP[3] = 2
        else:
            TP[3] = 1
        turn += 1
    elif (200 < x < 400 and 200 < y < 400) and TP[4]==0:
        if turn % 2 == 0:
            TP[4] = 2
        else:
            TP[4] = 1
        turn += 1
    elif (400 < x < 600 and 200 < y < 400) and TP[5]==0:
        if turn % 2 == 0:
            TP[5] = 2
        else:
            TP[5] = 1
        turn += 1
    elif (0 < x < 200 and 400 < y < 600) and TP[6]==0:
        if turn % 2 == 0:
            TP[6] = 2
        else:
            TP[6] = 1
        turn += 1
    elif (200 < x < 400 and 400 < y < 600) and TP[7]==0:
        if turn % 2 == 0:
            TP[7] = 2
        else:
            TP[7] = 1
        turn += 1
    elif (400 < x < 600 and 400 < y < 600) and TP[8]==0:
        if turn % 2 == 0:
            TP[8] = 2
        else:
            TP[8] = 1
        turn += 1

def win():
    global TP
    if TP[0] != 0 and TP[0] == TP[1] == TP[2]:
        if TP[0] == 1:
            print('X wins')
        else:
            print('Y wins')

    elif TP[3] != 0 and TP[3] == TP[4] == TP[5]:
        if TP[0] == 1:
            print('X wins')
        else:
            print('Y wins')
    elif TP[6] != 0 and TP[6] == TP[7] == TP[8]:
        if TP[0] == 1:
            print('X wins')
        else:
            print('Y wins')

    elif TP[0] != 0 and TP[0] == TP[3] == TP[6]:
        if TP[0] == 1:
            print('X wins')
        else:
            print('Y wins')

    elif TP[1] != 0 and TP[1] == TP[4] == TP[7]:
        if TP[0] == 1:
            print('X wins')
        else:
            print('Y wins')

    elif TP[2] != 0 and TP[2] == TP[5] == TP[8]:
        if TP[0] == 1:
            print('X wins')
        else:
            print('Y wins')

    elif TP[0] != 0 and TP[0] == TP[4] == TP[8]:
        if TP[0] == 1:
            print('X wins')
        else:
            print('Y wins')

    elif TP[2] != 0 and TP[2] == TP[4] == TP[6]:
        if TP[0] == 1:
            print('X wins')
        else:
            print('Y wins')
    elif turn >= 10:
        print('draw')


while True:
    pygame.draw.line(screen, 'white', (200, 0), (200, 600), 5)
    pygame.draw.line(screen, 'white', (400, 0), (400, 600), 5)
    pygame.draw.line(screen, 'white', (0, 200), (600, 200), 5)
    pygame.draw.line(screen, 'white', (0, 400), (600, 400), 5)

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                a = event.pos
                inp = str(event.pos[0]) + "," + str(event.pos[1])
                inp = inp.encode()
                s.sendall(inp)
        if event.type == QUIT:
            pygame.quit()
            exit()
    if a != None:
        x = a[0]
        y = a[1]
        placement(x,y)
        for i in range(9):
            if TP[i] == 1:
                X(cords[i])
            elif TP[i] == 2:
                Circle(cords[i])
        win()
        pygame.display.update()
    if turn%2==1:
        a=s.recv(1024)
        a=a.decode()
        a=a.split(',')
        x=int(a[0])
        y=int(a[1])
        placement(x,y)
        win()
    pygame.display.update()



