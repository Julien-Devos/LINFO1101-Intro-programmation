freq = []
all = []
for i in l:
    if i not in all:
        all.append(i)
        freq.append([i,1])
    else:
        for car in freq:
            if car[0] == i:
                car[1] += 1
max_freq = freq[0][1]
max_car = freq[0][0]
for i in freq:
    if i[1] > max_freq:
        max_freq = i[1]
        max_car = i[0]
return max_car