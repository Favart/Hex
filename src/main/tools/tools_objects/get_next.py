def get_next(current):
    """ Arguments:
            current set: positions des pions dans une colonne
        
        Return:
            next set: positions des pions qui peuvent être liés dans la colonne suivante
    """
    next = set([])
    for pos in current:
        if pos > 0:
            next.add(pos-1)
        next.add(pos)
    return next