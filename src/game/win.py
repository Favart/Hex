import numpy as np

def win(state:np.ndarray,pos:tuple,turn:int):
    r, state[pos] = 0, 0
    row = pos[0]
    column = pos[1]
    if r != turn and row > 0 and state[row-1,column] == turn:
        r = turn if pos[1] == len(state)-1 else win(state, (row-1,column), turn)   
    if r != turn and row > 0 and len(state) > column+1 and state[row-1,column+1] == 1:
        r = turn if pos[1] == len(state)-1 else win(state, (row-1,column+1), turn)                  
    if r != turn and column > 0 and state[row,column-1] == turn:
        r = turn if pos[1] == len(state)-1 else win(state, (row,column-1), turn)        
    if r != turn and len(state) > column+1 and state[row,column+1] == turn:
        r = turn if pos[1] == len(state)-1 else win(state, (row,column+1), turn)      
    if r != turn and len(state) > row+1 and column > 0 and state[row+1,column-1] == turn:
        r = turn if pos[1] == len(state)-1 else win(state, (row+1,column-1), turn)     
    if r != turn and len(state) > row+1 and state[row+1,column] == turn:
        r = turn if pos[1] == len(state)-1 else win(state, (row+1,column), turn)
    return r