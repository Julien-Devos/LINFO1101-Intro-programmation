def is_adn(s):
    """pre: s est un string
       post: retourne True si s contient seulement les caractères [a, t, c, g] en
             minuscule ou en majuscule. Si le string est vide il retourne False
    """
    if s == "":
        return False

    for i in s:
        if i == "a" or i == "A" or i == "t" or i == "T" or i == "c" or i == "C" or i == "g" or i == "G":
            pass
        else:
            return False

    return True

def positions(s, p):
    """pre: s et p sont des strings et len(p) <= len(s)
       post: retourne les positions des occurences de p dans s
    """
    pos = []
    l = []
    occur = 0
    current = 0
    for i in s.lower():
        if i == p[occur].lower():
            occur += 1
            l.append(current)
        elif i == p[0].lower():
            l = []
            l.append(current)
            occur = 1
        else:
            l = []
            occur = 0
        if occur == len(p):
            pos.append(l[0])
            l = []
            occur = 0
        current += 1
    return pos

def distance_h(s, p):
    """pre: s et p sont des strings de tailles égales
       post: retourne le nombre de caractéres différents entre s et p
    """
    if len(s) != len(p):
        return None
    count = 0
    current = 0
    for e in s:
        if e != p[current]:
            count += 1
        current += 1
    return count

def distances_matrice(l):
    """pre: l est une liste contenant des strings
       post: retourne une matrice des distances de hamming entre tous les caractères de la liste l
    """
    matrix = []
    for i in l:
        line = []
        for j in l:
            line.append(distance_h(i, j))
        matrix.append(line)
    return matrix
