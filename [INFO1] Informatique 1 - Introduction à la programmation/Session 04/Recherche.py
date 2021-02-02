def recherche(m, v):
    for i in m:
        for e in i:
            if e == v:
                return True
    return False