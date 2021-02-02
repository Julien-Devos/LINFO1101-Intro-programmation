def compare(p,x):
    count = 0
    for i in range(len(p)):
        if p[i].lower() == x[i].lower() or p[i] == '?':
            count += 1
    if count == len(p):
        return True
    return False

def positions(p,s):
    pos = []
    for i in range(len(s) - len(p) + 1):
        if compare(p,s[i:len(p)+i]):
            pos.append(i)
    return pos