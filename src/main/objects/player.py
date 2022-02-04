import numpy as np

from main.tools.tools_objects.transform import transform
from main.tools.tools_objects.get_next import get_next

class Player():

    def __init__(self,n):
        self.squares = np.zeros(shape=(n,n))

    def play(self,square):
        row = square[0]
        column = square[1]
        self.squares[row,column] = 1

    def win(self):
        squares = self.squares.transpose()
        current = transform(squares[0])
        for i in range(1,len(squares)):
            next = get_next(current)
            current = next.intersection(transform(squares[i]))
        if current:
            return True
        else:
            return False