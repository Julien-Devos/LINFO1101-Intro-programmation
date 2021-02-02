def treatment(data):
    l = data.strip().split(" ")
    previous = l[0]
    count = -1
    final = ""
    for i in l:
        count += 1
        if i != previous:
            final = final + previous + "*" + str(count)+" "
            count = 0
        previous = i
    count += 1
    final = final + previous + "*" + str(count)
    return final