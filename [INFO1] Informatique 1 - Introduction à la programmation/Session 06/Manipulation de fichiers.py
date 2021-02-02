def line_count(filename): #Compteur de lignes
    with open(filename, 'r') as file:
        count = 0
        for line in file.readlines():
            count += 1
        return count


def char_count(filename): #Compteur de caractères
    with open(filename, 'r') as file:
        count = 0
        for char in file.read():
            count += 1
        return count


def space(filename,n): #Création de fichiers
    with open(filename, 'w') as file:
        file.write(n*" ")


def capitalize(filename_in,filename_out): #Mise en majuscule
    with open(filename_in, 'r') as file1:
        l = file1.readlines()
    with open(filename_out, 'w') as file:
        for i in l:
            file.write(i.upper())