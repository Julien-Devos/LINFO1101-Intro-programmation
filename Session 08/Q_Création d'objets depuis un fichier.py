def marks_from_file(filename):
    l = []
    with open(filename, 'r') as file:
        for lines in file:
            line = lines.strip().split(" ")
            l.append(Student(line[0],line[1],int(line[2])))
    return l