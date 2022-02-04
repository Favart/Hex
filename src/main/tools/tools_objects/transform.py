def transform(column):
    """ Arguments:
            column list: valeur différente de 0 s'il y a un pion
        
        Return:
            r set: toutes les postitions dans la colonne où les valeurs sont différentes de 0
    """
    r = set([])
    for i in range(len(column)):
        if column[i] != 0:
            r.add(i)
    return r