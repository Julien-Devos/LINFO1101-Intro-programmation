def count(events, i, j):
    count = 0
    for k in events:
        if k == (i,j):
            count += 1
    return count