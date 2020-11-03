def run_program(filename):
    """ Demande au user le nom du fichier dans lequel il veut travailler et lui demande de donner une liste de mots.

        Appelle la fonction print_lines(filename, l).
    """
    words = input("\nEntrez une liste de mots: ")
    l = words.lower().split(' ')
    print_lines(filename, l)

def print_lines(filename, l):
    get_lines(l,create_index(filename))

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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    list_line = line.replace("\t"," ").strip().lower().split(' ')
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
    """ Retourne les identifiants des lignes qui contiennent tous les mots de la liste words en utilisant le dictionnaire
    contenant l'index.

    Args:
        words: lst: plusieurs mots
        index: dictionnaire contenant des index

        Returns:
            une liste des identifiants des lignes qui contiennent tous les mots de la liste words.

    """
    #TODO execpt Key error  quand le mot donné n'est pas dans le fichier
    l = []
    for word in words:
        l.append([word, list(index[word])])
    print(l)
    final_list = []
    for i in l[0][1]:
        count = 0
        for j in range(1,len(l)):
            for k in l[j][1]:
                if k == i:
                    count += 1
                    break
        if count == len(l)-1:
            final_list.append(i)
    return final_list

#get_lines(["musique","hans","zimmer"] ,create_index("text_exemple_1.txt")) == 9
#get_lines(["vous","etes"] ,create_index("text_exemple_1.txt"))  == 0

if __name__ == "__main__":
    filename = input("\nDans quel fichier souhaitez-vous travailler? ")
    while True:
        run_program(filename)