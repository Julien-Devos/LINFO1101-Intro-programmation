count_num = 0
count = 0
for i in l:
    if i == 9999:
        break
    elif i <= 0:
        count += 1
    elif isinstance(i, (int,float)):
        count_num += i
        count += 1
return count_num / count