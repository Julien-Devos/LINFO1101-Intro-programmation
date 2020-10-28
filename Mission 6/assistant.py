def start_assistant():
    commands = ['file', 'info', 'dictionary', 'search', 'sum', 'avg', 'help', 'exit']

    command = input("\nRentrez la commande: ").split()
    while command[0] not in commands:
        print("Command not found, type 'help' for help")
        command = input("\nRentrez la commande: ").split()

    do_command(command)

def do_command(command):
    try:
        if command[0] == 'file':
            print(file(command[1]))

        elif command[0] == 'info':
            print(info())

        elif command[0] == 'dictionary':
            print(dictionary())

        elif command[0] == 'search':
            try:
                print(search(command[1]))
            except NameError:
                print("This file is not sorted, use 'dictionary' before 'search' ")

        elif command[0] == 'sum':
            parameter = (','.join(command[1:len(command)])).split(',')
            print(sum(parameter))

        elif command[0] == 'avg':
            parameter = (','.join(command[1:len(command)])).split(',')
            print(avg(parameter))

        elif command[0] == 'help':
            print(help())

        elif command[0] == 'exit':
            exit()

    except IndexError:
        print("Too much arguments in the command, type 'help' for help")


def file(name):
    """ Change le fichier sur lequel l'utilisateur travaille et le lui confirme en affichant le nom de ce dernier.

        Args:
            name: un string   le nom du fichier
        Returns:
            Assigne le nom du fichier à la variable global filename
    """
    global filename
    filename = name
    return "Vous travaillez avec le ficher: " + filename

def info():
    """

    """
    with open(filename, "r") as file:
        lines = 0
        caract = 0
        for line in file:
            lines += 1
            caract += len(line)
    return "Nombre de lignes: " + str(lines) + "\nNombre de caractères: " + str(caract)

def dictionary():
    """ Il ordonne le fichier filename et le stock dans une variable

    """
    with open(filename, "r") as file:
        global sorted_file
        sorted_file = []
        for line in file:
            sorted_file.append(tuple(line.strip().split(',')))
        sorted_file = sorted(sorted_file)
        return "Read " + filename + " as a Dictionary"

def search(name):
    """

    """
    first = 0
    last = len(sorted_file) - 1

    while first <= last:
        middle = (first + last) // 2
        if sorted_file[middle][0] == name:
            return "'" + name + "'" + " is in the Dictionary"
        else:
            if name < sorted_file[middle][0]:
                last = middle - 1
            else:
                first = middle + 1
    return "'" + name + "'" + " is not in the Dictionary"

def sum(numbers):
    """ Retourne la somme des nombres donnés par l'utilisateur.

        Par exemple: sum 1 2 3 4 5 == 15

        Args:
            numbers: Une liste de nombres.
        Returns:
            Retourne la sommes des nombres dans numbers.
    """
    somme = 0
    for i in numbers:
        somme += int(i)
    return "La somme vaut : " + str(somme)

def avg(numbers):
    """ Affiche la moyenne des nombres donnés par l'utilisateur.

        Par exemple: avg 1 2 3 4 5 == 3

        Args:
            numbers: Une liste de nombres.
        Returns:
            Print "La moyenne est de: " suivi de la moyenne calculée.
    """
    return "La moyenne est de: " + str(sum(numbers) / len(numbers))

def help():
    """ Affiche les commandes possibles et comment les utiliser.

        Returns:
            Print la liste des commandes possibles et comment les utiliser.
    """
    return ("- file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment\n"
            "- info: montre le nombre de lignes et de caractères du fichier \n"
            "- dictionary: utilise le fichier comme dictionnaire à partir de maintenant\n"
            "- search <word>: détermine si le mot est dans le dictionnaire\n"
            "- sum <number1> ... <numbern>: calcule la somme des nombres spécifiés\n"
            "- avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés\n"
            "- help: montre des instructions à l'utilisateur\n"
            "- exit: arrête l'outil\n")

def exit():
    """ Termine le programme assistant.

        Returns:
             Print "Stop program" et termine le programme.
    """
    print("Stopping program")
    raise SystemExit

while True:
    start_assistant()