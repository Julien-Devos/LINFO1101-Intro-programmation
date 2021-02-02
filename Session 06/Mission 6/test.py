import assistant as assist

def test_file():
    assert assist.file("all_words.dat") == "Vous travaillez avec le ficher: all_words.dat", 'test 1'

def test_info():
    assert assist.info() == "Nombre de lignes: 113004\nNombre de caractères: 1330217", 'test 1'

def test_dictionary():
    assert assist.dictionary() == "Read all_words.dat as a Dictionary", 'test 1'

def test_search():
    assert assist.search("this") == "'this' is in the Dictionary", 'test 1'
    assert assist.search("bitch") == "'bitch' is in the Dictionary", 'test 2'
    assert assist.search("cunt") == "'cunt' is in the Dictionary", 'test 3'
    assert assist.search("bryan") == "'bryan' is not in the Dictionary", 'test 4'
    assert assist.search("aubergine") == "'aubergine' is not in the Dictionary", 'test 5'

def test_sum():
    assert assist.sum([4, 6, 5, 3, 9, 2]) == 29, 'test 1'
    assert assist.sum([2, 5, 7, 1]) == 15, 'test 2'
    assert assist.sum([2, 3, 9, 6, 1]) == 21, 'test 3'

def test_avg():
    assert assist.avg([4, 6, 5, 3, 9, 2]) == "La moyenne est de: 4.833333333333333", 'test 1'
    assert assist.avg([3, 2, 7, 4]) == "La moyenne est de: 4.0", 'test 2'
    assert assist.avg([10, 24, 78, 17]) == "La moyenne est de: 32.25", 'test 3'

def test_help():
    assert assist.help() == ("- file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment\n"
                            "- info: montre le nombre de lignes et de caractères du fichier \n"
                            "- dictionary: utilise le fichier comme dictionnaire à partir de maintenant\n"
                            "- search <word>: détermine si le mot est dans le dictionnaire\n"
                            "- sum <number1> ... <numbern>: calcule la somme des nombres spécifiés\n"
                            "- avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés\n"
                            "- help: montre des instructions à l'utilisateur\n"
                            "- exit: arrête l'outil\n")

def test_exit():
    assert assist.exit() == "Stopping program", 'test 1'

def all_tests():
    test_file()
    test_info()
    test_dictionary()
    test_search()
    test_sum()
    test_avg()
    test_help()
    test_exit()

all_tests()


