list = []
for i in lst:
    if not i in list:
        list.append(i)
return len(list)