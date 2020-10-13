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

print(distances_matrice(["AG", "AT", "GT", "ACG", "ACT" ]))

