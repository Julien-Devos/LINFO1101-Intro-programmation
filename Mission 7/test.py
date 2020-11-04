import search

def test_readfile():
    assert search.readfile("text_exemple_2.txt") == ["Bonjour moi\n","m'appelle cafe.\n","test c'est le test\n","pour le programme tester.??!!\n","parler france?! moi je :.\n","    pas tres"], "test n°1"

def test_get_words():
    assert search.get_words("pour le programme tester.??!!\n") == ["pour","le","programme","tester"], "test n°1"
    assert search.get_words("\tbonjour c'est le test.\n") == ["bonjour","cest","le","test"], "test n°2"

def test_create_index():
    pass

def test_get_lines():
    pass
    # get_lines(["musique","hans","zimmer"] ,create_index("text_exemple_1.txt")) == 9
    # get_lines(["vous","etes"] ,create_index("text_exemple_1.txt"))  == 0

def all_test():
    test_readfile()
    test_get_words()
    test_create_index()
    test_get_lines()

all_test()
