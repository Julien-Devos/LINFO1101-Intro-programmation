final_list1, final_list2 = [], []
if first_list == []:
    return second_list
elif second_list == []:
    return first_list
for i in range(len(first_list)):
    final_list1.append(first_list[i])
    final_list1.append(second_list[i])
for j in range(len(final_list1)):
    min = final_list1[0][1]
    index = 0
    for i in range(1, len(final_list1)):
        if final_list1[i][1] < min:
            min = final_list1[i][1]
            index = i
    final_list2.append(final_list1[index])
    final_list1.remove(final_list1[index])
return final_list2