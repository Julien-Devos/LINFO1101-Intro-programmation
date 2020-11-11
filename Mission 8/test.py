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


# TEST DE LA METHODE __str__ DE LA CLASSE Duree

def test_Duree_str(duree1, duree2):
    assert duree1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert duree2.__str__() == "08:41:25", "Test 2 Duree __str__"
    # A COMPLETER EVENTUELLEMENT PAR LES ETUDIANTS


# TEST DE LA METHODE toSecondes DE LA CLASSE Duree

def test_Duree_to_secondes(duree1, duree2):
    assert duree1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert duree2.to_secondes() == 31285, "Test 2 Duree toSecondes"
    # A COMPLETER EVENTUELLEMENT PAR LES ETUDIANTS


# TEST DE LA METHODE delta DE LA CLASSE Duree

def test_Duree_delta(duree1, duree2):
    # A COMPLETER PAR LES ETUDIANTS
    pass


# TEST DE LA METHODE apres DE LA CLASSE Duree

def test_Duree_apres(duree1, duree2):
    duree0 = Duree(0, 0, 0)
    assert duree1.apres(duree2), "Test 1 Duree apres"
    assert not duree0.apres(duree1), "Test 2 Duree apres"
    # A COMPLETER PAR LES ETUDIANTS


# TEST DE LA METHODE ajouter DE LA CLASSE Duree

def test_Duree_ajouter(duree1, duree2):
    # A COMPLETER PAR LES ETUDIANTS
    pass


# CREATION DE DEUX OBJET DE LA CLASSE Duree ET APPEL DES DIFFERENTES METHODES TEST

d1 = Duree(10, 20, 59)
d2 = Duree(8, 41, 25)
test_Duree_str(d1, d2)
test_Duree_to_secondes(d1, d2)
test_Duree_delta(d1, d2)
test_Duree_apres(d1, d2)
test_Duree_ajouter(d1, d2)


################################
# Tests pour la classe Chanson #
################################

# TEST DE LA METHODE __str__ DE LA CLASSE Chanson

def test_Chanson_str(chanson):
    # A COMPLETER PAR LES ETUDIANTS
    pass


# CREATION D'UN OBJET DE LA CLASSE Chanson ET APPEL DES DIFFERENTES METHODES TEST

c = Chanson("Let's Dance", "David Bowie", Duree(0, 4, 5))
test_Chanson_str(c)

##############################
# Tests pour la classe Album #
##############################

# TEST DE LA METHODE __str__ DE LA CLASSE Album
# (A COMPLETER PAR LES ETUDIANTS)

# TEST DE LA METHODE add DE LA CLASSE Album
# (A COMPLETER PAR LES ETUDIANTS)

# CREATION D'UN OBJET DE LA CLASSE Album ET APPEL DES DIFFERENTES METHODES TEST
# (A COMPLETER PAR LES ETUDIANTS)

#####################################
# Test du comportement du programme #
#####################################

# QUELQUES TESTS ICI POUR TESTER QUE LES 3 CLASSES COLLABORENT CORRECTEMENT
# ET PEUVENT ETRE UTILISE POUR CREER DES ALBUMS DE CHANSONS SELON LES CONSIGNES
# DE LA MISSION
# (A COMPLETER PAR LES ETUDIANTS)