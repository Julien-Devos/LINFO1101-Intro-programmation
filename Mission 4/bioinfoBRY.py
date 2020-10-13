def distance_h(s, p):
    if len(s) != len(p):
        return None
    current = 0
    count = 0
    for e in s:
        if e == p[current]:
            current += 1
            count += 1
        else:
            pass
    return count
print (distance_h("ABCDE", "AEEE"))