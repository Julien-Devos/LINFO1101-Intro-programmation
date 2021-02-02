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
            if i.lower() == p[0].lower():
                occur = 1
            else:
                occur = 0
        current += 1
    return pos
# abbbe bb
def positions(s, p):
    pos = []
    occur = 0
    for i in range(len(s)):
        for j in range(len(p)):
            if s[i].lower() == p[j].lower():
                for k in range(1, len(p)+1):
                    if s[i+k] == p[k]:
                        occur += 1

print(positions('CbbbF','bB'))