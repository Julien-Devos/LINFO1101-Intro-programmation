def is_adn(s):
    if s == "":
        return False

    for i in s:
        if i == "a" or i == "A" or i == "t" or i == "T" or i == "c" or i == "C" or i == "g" or i == "G":
            pass
        else:
            return False

    return True

def positions(s, p):
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
    matrix = []
    for i in l:
        line = []
        for j in l:
            line.append(distance_h(i, j))
        matrix.append(line)
    return matrix