import numpy as np
from win import win

class Game():
    
    def __init__(self):
        self.empty = None
        self.full = None
        self.state = None
        self.turn = None
        
    def clear(self, size:int):
        self.empty = list()
        for row in range(size):
            for col in range(size):
                self.empty.append((row,col))
        self.full = list()
        self.state = np.zeros((size,size))
        self.turn = 1
    
    def play(self, move:tuple):
        self.empty.remove(move)
        self.full.append(move)
        self.state[move] = self.turn
        self.turn = 3-self.turn
        
    def check_end(self):
        state = self.state.copy()
        for i in range(len(state)):
            r = win(state, (i,0), 1) if state[(i,0)] == 1 and r == 0 else r
            r = win(state.transpose(), (i,0), 2) if state[(0,i)] == 1 and r == 0 else r
        return r
