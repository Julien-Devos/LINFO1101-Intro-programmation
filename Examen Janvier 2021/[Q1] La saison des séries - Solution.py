def serie(n) : # NE PAS EFFACER CETTE LIGNE
    """
    @pre: n >= 0 est un entier
    @post: retourne 0 si n est 0, sinon
    retourne la somme des n premiers termes de la série
    1 - 1/2 + 1/3 - 1/4 + 1/5 - ... + (-1)**(i-1)/i + ...
    """
    serie = 0
    for i in range(1,n+1):
        serie += (-1)**(i-1)/i
    return serie


def trouve(val) : # NE PAS EFFACER CETTE LIGNE
    """
    pre: val est un nombre réel
    post: retourne la plus petite valeur de l'entier n telle que serie(n)
    est presque égale à la valeur val.
    """
    i = 0
    while True:
        if presque_egal(val,serie(i)):
            return i
        i += 1

#Note: 100%