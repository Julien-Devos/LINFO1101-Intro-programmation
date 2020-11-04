#Devos Bryan et Devos Julien
import search

def test_readfile():
    assert search.readfile("text_exemple_2.txt") == ["Bonjour moi\n","m'appelle cafe.\n","test c'est le test\n","pour le programme tester.??!!\n","parler france?! moi je :.\n","    pas tres"], "test n°1"
    assert search.readfile("lefichierexistepas") == "File not found!", "test n°2"
    assert search.readfile("ct_pas_un_bon_fichier_non_plus") == "File not found!", "test n°3"

def test_get_words():
    assert search.get_words("pour le programme tester.??!!\n") == ["pour","le","programme","tester"], "test n°1"
    assert search.get_words("\tbonjour c'est le test.\n") == ["bonjour","cest","le","test"], 'test n°2'
    assert search.get_words(" Ceci est une phrase de test, je ne sais pas trop quoi ecrire !!!  ") == ["ceci","est","une","phrase","de","test","je","ne","sais","pas","trop","quoi","ecrire"], "test n°3"
    assert search.get_words("Ct un prank, je c sais tro marrent! ") == ["ct","un","prank","je","c","sais","tro","marrent"], 'test n°4'

def test_create_index():
    assert search.create_index("text_exemple_2.txt") == {"bonjour": {0:1},"moi": {0:1, 4:1},"mappelle": {1:1},"cafe": {1:1},"test": {2:2},"cest": {2:1},"le": {2:1, 3:1},"pour": {3:1},"programme": {3:1},"tester": {3:1},"parler": {4:1},"france": {4:1},"je": {4:1},"pas": {5:1},"tres": {5:1}}, 'test n°1'

def test_get_lines():
    assert search.get_lines(["musique","hans","zimmer"] ,search.create_index("text_exemple_1.txt")) == [9], 'test n°1'
    assert search.get_lines(["vous","etes"] ,search.create_index("text_exemple_1.txt"))  == [0], 'test n°2'
    assert search.get_lines(["de","hans"],search.create_index("text_exemple_1.txt"))  == [2,9], 'test n°3'
    assert search.get_lines(["souvenez","programme","cependant","bout"], search.create_index("text_exemple_1.txt")) == [], 'test n°4'

def all_test():
    test_readfile()
    test_get_words()
    test_create_index()
    test_get_lines()

all_test()