##############################
# Tests pour la classe Duree #
##############################
# Kim Mens, 06-11-2020, Ã  complÃ©ter par les Ã©tudiants

# Pour le moment, pour tester notre programme orientÃ© objet on va encore utiliser les instructions
# "assert" comme vu dans l'introduction de la mission 5.
# Dans une mission futur nous introduirons le mÃ©canisme des tests unitaires qui est encore mieux
# appropriÃ© pour tester du code orientÃ© objets.

# D'abord on doit importer la classe Ã  tester
from mission8 import Duree, Chanson, Album

# CREATION DE DEUX OBJET DE LA CLASSE Duree
temps1 = Duree(15,10,52)
temps2 = Duree(0,15,32)
temps3 = Duree(3,7,1)
temps4 = Duree(127,64,87)

# TEST DE LA METHODE __str__ DE LA CLASSE Duree
def test_Duree_str():
    assert temps1.__str__() == "15:10:52", "Test 1 Duree __str__"
    assert temps2.__str__() == "00:15:32", "Test 2 Duree __str__"
    assert temps3.__str__() == "03:07:01", "Test 3 Duree __str__"
    assert temps4.__str__() == "128:05:27", "Test 4 Duree __str__"



# TEST DE LA METHODE toSecondes DE LA CLASSE Duree
def test_Duree_to_secondes():
    assert temps1.to_secondes() == 54652, "Test 1 Duree toSecondes"
    assert temps2.to_secondes() == 932, "Test 2 Duree toSecondes"
    assert temps3.to_secondes() == 11221, "Test 3 Duree toSecondes"
    assert temps4.to_secondes() == 461127, "Test 4 Duree toSecondes"


# TEST DE LA METHODE delta DE LA CLASSE Duree
def test_Duree_delta():
    assert temps1.delta(temps2) == -53720, "Test 1 Duree delta"
    assert temps2.delta(temps1) == 53720, "Test 2 Duree delta"
    assert temps3.delta(temps4) == 449906, "Test 3 Duree delta"
    assert temps4.delta(temps1) == -406475, "Test 4 Duree delta"


# TEST DE LA METHODE apres DE LA CLASSE Duree
def test_Duree_apres():
    assert temps1.apres(temps2), "Test 1 Duree apres"
    assert not temps2.apres(temps1), "Test 2 Duree apres"
    assert not temps3.apres(temps4), "Test 3 Duree apres"
    assert temps4.apres(temps1), "Test 4 Duree apres"


# TEST DE LA METHODE ajouter DE LA CLASSE Duree
def test_Duree_ajouter():
    temps1.ajouter(temps2)
    assert temps1.__str__() == "15:26:24", "Test 1"
    temps2.ajouter(temps1)
    assert temps2.__str__() == "15:41:56", "Test 2"
    temps1.hour, temps1.minute, temps1.sec = 15, 10, 52
    temps2.hour, temps2.minute, temps2.sec = 0, 15, 32
    temps3.ajouter(temps4)
    assert temps3.__str__() == "131:12:28", "Test 3"
    temps3.hour, temps3.minute, temps3.sec = 3, 7, 1
    temps4.ajouter(temps1)
    assert temps4.__str__() == "143:16:19", "Test 4"
    temps4.hour, temps4.minute, temps4.sec = 127, 64, 87

################################
# Tests pour la classe Chanson #
################################

# TEST DE LA METHODE __str__ DE LA CLASSE Chanson
d1 = Duree(0, 3, 20)
d2 = Duree(0, 0, 28)
d3 = Duree(0, 0, 40)
d4 = Duree(0, 4, 10)

def test_Chanson_str():
    chanson1 = Chanson ("Confinés","Joyca",d1)
    chanson2 = Chanson ("Chamrousse","Joyca",d2)
    chanson3 = Chanson ("Les glaces","Joyca",d3)
    chanson4 = Chanson ("Jacquadi","POLO & PAN",d4)
    assert chanson1.__str__() == "Confinés - Joyca - 00:03:20"
    assert chanson2.__str__() == "Chamrousse - Joyca - 00:00:28"
    assert chanson3.__str__() == "Les glaces - Joyca - 00:00:40"
    assert chanson4.__str__() == "Jacquadi - POLO & PAN - 00:04:10"


##############################
# Tests pour la classe Album #
##############################

# TEST DE LA METHODE __str__ DE LA CLASSE Album
def test_Album_str():
    album = Album("test")
    album.ajouter(Chanson("Confinés", "Joyca", Duree(0, 3, 20)))
    album.ajouter(Chanson("Chamrousse", "Joyca", Duree(0, 0, 28)))
    album.ajouter(Chanson("Les glaces", "Joyca", Duree(0, 0, 40)))
    album.ajouter(Chanson("Jacquadi", "POLO & PAN", Duree(0, 4, 10)))

    assert album.__str__() == ("Album test (4 chansons, 00:08:38)\n"
                               "1: Confinés - Joyca - 00:03:20\n"
                               "2: Chamrousse - Joyca - 00:00:28\n"
                               "3: Les glaces - Joyca - 00:00:40\n"
                               "4: Jacquadi - POLO & PAN - 00:04:10\n")

#APPEL DES DIFFERENTES METHODES TEST
def all_tests():
    test_Duree_str()
    test_Duree_to_secondes()
    test_Duree_delta()
    test_Duree_apres()
    test_Duree_ajouter()
    test_Chanson_str()
    test_Album_str()

#####################################
# Test du comportement du programme #
#####################################

all_tests()

# QUELQUES TESTS ICI POUR TESTER QUE LES 3 CLASSES COLLABORENT CORRECTEMENT
# ET PEUVENT ETRE UTILISE POUR CREER DES ALBUMS DE CHANSONS SELON LES CONSIGNES
# DE LA MISSION
# (A COMPLETER PAR LES ETUDIANTS)
#c'est fai dans mission 8.py