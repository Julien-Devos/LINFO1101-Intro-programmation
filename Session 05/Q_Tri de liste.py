sorted_list = []
while len(a_list) > 0:
    min, index = a_list[0], 0
    for i in range(1, len(a_list)):
        if a_list[i] < min:
            min, index = a_list[i], i
    sorted_list.append(min)
    a_list.remove(a_list[index])