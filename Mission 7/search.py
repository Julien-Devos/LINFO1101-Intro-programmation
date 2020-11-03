def run_program():
    """ Demande au user le nom du fichier dans lequel il veut travailler et lui demande de donner une liste de mots.

        Appelle la fonction print_lines(filename, l).
    """
    filename = input("\nDans quel fichier souhaitez-vous travailler? ")
    words = input("\n Entrez une liste de mots: ")
    l = words.lower.split(' ')
    print_lines(filename, l)

def print_lines(filename, l):
    pass

def readfile(filename):
    """ Retourne une liste qui contient les lignes du fichier.

        Args:
            filename: str: le nom d'un fichier

        Returns:
            une liste contenant les lignes du fichier
    """
    with open(filename, 'r') as file:
        return file.readlines()

def get_words(line):
    """ Retourne une liste contenant les mots sans la ponctuation de la ligne rentrée en paramètre.

        Args:
            line: str: une phrase

        Returns:
            une liste contenant les mots de la phrase sans la ponctuation
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzéèàç'
    list_line = line.strip().lower().split(' ')
    l = []
    for i in list_line:
        word = ''
        for j in i:
            if j in alphabet:
                word = word + j
        if word != '':
            l.append(word)
    return l

def create_index(filename):
    """ Retourne un dictionnaire qui contient tous les mots différents du fichier et pour chaque mot, donne les index de chaque ligne
    où ils se trouvent et pour chaque index, donne sa récurrence sur cet index.

        Args:
            filename: str: le nom du fichier

        Returns:
            un dictionnaire d'index
    """
    dictionary = {}
    lines = readfile(filename)
    for i in range(len(lines)):
        words = get_words(lines[i])
        for word in words:
            if word not in dictionary:
                dictionary[word] = {i:1}
            else:
                try:
                    dictionary[word][i] += 1
                except:
                    dictionary[word][i] = 1
    return dictionary

def get_lines(words,index):
    l = []
    for word in words:
        l.append([word, list(index[word])])

    for indexs in range(len(l[0][1])):
        for i in range(len(l)):
            try:
                if l[i][1][indexs] != indexs:
                    break
            except:
                pass
        l.append(indexs)
    print(l)
    return l


if __name__ == "__main__":
    """while True:
        run_program()"""
    get_lines(['guacamole','bon'] ,create_index("README.txt"))