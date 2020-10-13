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


