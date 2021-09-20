import sys
import math
import time
import numpy as np
from numpy.random import choice
#def
def ms(start_time):
    return (time.perf_counter() - start_time) * 1000
def stack(board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            k = i
            while board[k][j] == 0:
                if k == len(board) - 1:
                    break
                k += 1
            if k != i:
                board[i][j], board[k][j] = board[k][j], 0
def sum_up(board):
    for i in range(0, len(board) - 1):
        for j in range(0, len(board)):
            if board[i][j] != 0 and board[i][j] == board[i + 1][j]:
                board[i][j] += board[i + 1][j]
                board[i + 1][j] = 0

#Class
class Board:
    def __init__(self, size):
        self.__board = np.zeros((size, size), int)
        self.__seed = 0
    
    def debug_print(self, c):
        print(c, self.__board, file=err, end="\n\n", sep="\n")
        
    def load_input(self):
        for i in range(4):
            self.__board[i] = np.array([int(x) for x in input().split()])
 
    def load_seed(self):
        self.__seed = int(input())
        #print("load seed ",self.__seed, file=err)

    def move(self, action):
        rotated_board = np.rot90(self.__board, action).copy()
        stack(rotated_board)
        sum_up(rotated_board)
        stack(rotated_board)
        rotated_board = np.rot90(rotated_board, -action)
        #print(np.max(np.power(rotated_board, .5)),file=err)
        #print(rotated_board,file=err)
        return np.max(rotated_board) - np.count_nonzero(rotated_board) if not np.array_equal(self.__board, rotated_board) else -1

    def apply_move(self, action):
        rotated_board = np.rot90(self.__board, action)
        stack(rotated_board)
        sum_up(rotated_board)
        stack(rotated_board)
        self.__board = np.rot90(rotated_board, len(self.__board) - action)

    def drop_elem(self):
        value = 2 if (self.__seed & 0x10) == 0 else 4
        z = np.where(self.__board == 0)
        z_idx = np.lexsort((z[0], z[1]))#[(x, y) for x, y in zip(z[0], z[1])],
        #print(z_idx, file=err, sep="\n")
        if not len(z_idx):
            #print("Zeroes indices null", file=err)
            return True
        r_nbr = self.__seed % len(z_idx)
        r_idx = (z[0][z_idx[r_nbr]], z[1][z_idx[r_nbr]])
        #print(r_nbr, self.__seed, file=err)
        self.__board[r_idx] = value
        self.__seed = (self.__seed*self.__seed) % 50515093
        return False
        #print(z, file=err, sep="\n")
        

#Vars
err = sys.stderr
board = Board(4)
start = True
d = {}
m = {'U':0, 'R':1, 'D':2, 'L':3}
# game loop
while True:
    o=""
    #board.debug_print()
    if (start == True):
        start = True
        board.load_seed()
        score = int(input())
        board.load_input()
    start_time = time.perf_counter()
    while(ms(start_time) < 48):
        d["U"] = board.move(0)
        d["R"] = board.move(1)
        d["D"] = board.move(2)
        d["L"] = board.move(3)
        c = max(d, key=d.get)
        #if c == "D" and d["D"] == d["L"]:
        #    c = "L"
        o += c
        board.apply_move(m[c])
        if (board.drop_elem()):
            continue
        #board.debug_print(c)
    print(o, flush=True)
