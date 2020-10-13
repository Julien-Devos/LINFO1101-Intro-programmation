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

print (distance_h("ABCDE", "ABCEB"))