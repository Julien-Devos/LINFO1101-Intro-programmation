def maximum_index(lst):
    if lst == []:
        return None
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return lst.index(max)