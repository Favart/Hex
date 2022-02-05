import numpy as np

def initialise_Q_table(n):
    Q_table = {}
    template = {}
    for i in range(n):
        for j in range(n):
            template[(i,j)] = 0
    Q_table[str(np.zeros(shape=(n,n)))] = template
    return Q_table