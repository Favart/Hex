import numpy as np

from main.tools.tools_objects.transform import transform
from main.tools.tools_objects.get_next import get_next
from main.tools.tools_objects.explore import explore

class Player():

    def __init__(self,n,turn):
        self.squares = np.zeros(shape=(n,n))
        if turn == 1:
            self.turn = 1
        else:
            self.turn = 2

    def play(self,square):
        row = square[0]
        column = square[1]
        self.squares[row,column] = 1

    def win(self):
        if self.turn == 1:
            squares = self.squares.transpose()
        else:
            squares = self.squares
        
        winner = False
        current = transform(squares[0])
        for pos in current:
            if explore(squares.copy(), (0,pos)):
                winner = True
        return winner
    
        
        
            
        