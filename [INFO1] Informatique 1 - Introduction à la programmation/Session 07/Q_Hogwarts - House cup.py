def winning_house(scroll):
    with open(scroll, 'r') as file:
        d = {'gryffindor':0,'ravenclaw':0,'hufflepuff':0,'slytherin':0}
        for line in file:
            houses = ['gryffindor','ravenclaw','hufflepuff','slytherin']
            l = line.strip().split(" ")
            for house in houses:
                if l[0] in students[house]:
                    d[house] += int(l[1])
        max = 0
        max_house = ''
        for house in d:
            if d[house] > max:
                max = d[house]
                max_house = house
        for house2 in d:
            if d[house2] == max and max_house != house2:
                return [max_house,house2]
    return max_house