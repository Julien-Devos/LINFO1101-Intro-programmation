def write_coordinates(filename, l): #Ecriture de coordonnées
    with open(filename, 'w') as file:
        for x,y in l:
            file.write(str(x) + ',' + str(y) + '\n')

def read_coordinates(filename): #Lecture de coordonnées
    with open(filename, 'r') as file:
        l = []
        for i in file.readlines():
            l.append(i.strip().split(','))
        l2 = []
        for j in l:
            l2.append((float(j[0]),float(j[1])))
    return l2