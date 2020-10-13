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
    occur = 0
    for i in range(len(s)):
        if s[i].lower() == p[0].lower():
            for k in range(1, len(p)+1):
                if s[i+k].lower() == p[k].lower():
                    occur += 1
                    if occur == len(p)-1:
                        occur = 0
                        pos.append(i)
                        break
                else:
                    break
            else:
                break
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
        if e.lower() != p[current].lower():
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
