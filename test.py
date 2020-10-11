#triangle ingnious
def triangle(n):
    liste = []
    for i in range(1, n+2):
        l = []
        for j in range(i):
            l.append(j)
        liste.append(l)
    return liste