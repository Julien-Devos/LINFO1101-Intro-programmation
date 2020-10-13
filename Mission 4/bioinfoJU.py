def positions(s, p):
    pos = []
    for i in s.lower():
        for j in range(len(p)):
            occur = 0
            if i == p[j].lower():
                l = []
                occur += 1
                l.append(s.index(i))
        if occur == len(p):
            pos.append(l[0])

    return pos

print(positions("ACGACC", "cg"))