def house_designation(student_qualities):
    l, house = [["Gryffindor", 0], ["Ravenclaw", 0], ["Hufflepuff", 0], ["Slytherin", 0]], []
    for i in student_qualities:
        for j in range(len(knowledge)):
            if i in knowledge[j][1]:
                l[j][1] +=1
    for i in range(len(l)):
        max, index = l[0][1], 0
        for j in range(len(l)):
             if l[j][1] > max:
                max, index = l[j][1], j
        house.append(l[index][0])
        l.remove(l[index])
    return house