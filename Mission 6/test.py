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
    assert assist.search

def test_sum():
    assert assist.sum([4, 6, 5, 3, 9, 2]) == "La somme vaut : 29", 'test 1'

def test_avg():
    assert assist.avg([4, 6, 5, 3, 9, 2]) == ""

def test_help():


def test_exit():


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


