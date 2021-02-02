def fact(n):
    """pre: n >= 0
       post: retourne la factorielle de n"""
    factoriel = n
    if n == 0:
        factoriel = 1
    else:
        for i in range(1, n):
            factoriel *= n - i
    return factoriel