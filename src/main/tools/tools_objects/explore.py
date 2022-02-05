def explore(matrix,pos):
    if pos[0] == len(matrix)-1:
        return True
    else:
        over = False
        row = pos[0]
        column = pos[1]
        matrix[row,column] = 0
        if row > 0 and matrix[row-1,column] == 1:
            if explore(matrix, (row-1,column)):
                over = True
        if row > 0 and len(matrix) > column+1 and matrix[row-1,column+1] == 1:
            if explore(matrix, (row-1,column+1)):
                over = True  
        if column > 0 and matrix[row,column-1] == 1:
            if explore(matrix, (row,column-1)):
                over = True
        if len(matrix) > column+1 and matrix[row,column+1] == 1:
            if explore(matrix, (row,column+1)):
                over = True
        if len(matrix) > row+1 and column > 0 and matrix[row+1,column-1] == 1:
            if explore(matrix, (row+1,column-1)):
                over = True
        if len(matrix) > row+1 and matrix[row+1,column] == 1:
            if explore(matrix, (row+1,column)):
                over = True
        return over