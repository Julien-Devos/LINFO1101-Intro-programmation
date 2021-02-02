def equal(l, d):
    test = {}
    for i in range(len(l)):
        for index, value in enumerate(l[i]):
            if value != 0:
                test[(i, index)] = value
    count = 0
    for i, j in test.items():
        if d.get(i) == j:
            count += 1
    if count == len(test):
        return True
    else:
        return False
