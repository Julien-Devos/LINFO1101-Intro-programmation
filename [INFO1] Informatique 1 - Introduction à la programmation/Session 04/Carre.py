def carre(n):
    matrix = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(n * i + j)
        matrix.append(l)
    return matrix