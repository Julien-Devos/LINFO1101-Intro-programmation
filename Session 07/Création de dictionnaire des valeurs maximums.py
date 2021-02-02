def create_dict_max(l):
    d = {}
    for x,y in l:
        if x not in d:
            d[x] = y
        else:
            if d[x] < y:
                d[x] = y
    return d