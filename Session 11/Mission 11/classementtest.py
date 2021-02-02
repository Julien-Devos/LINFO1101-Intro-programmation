import unittest
from orderedlinkedlist import OrderedLinkedList
from coureur import Coureur
from resultat import Resultat
from temps import Temps
from classement import Classement

class OrderedLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.cl = Classement()
        self.a = Coureur("A", 10)
        self.b = Coureur("B", 10)
        self.c = Coureur("C", 10)
        self.d = Coureur("d", 10)
        self.a_temps = Temps(0, 1, 0)
        self.b_temps = Temps(0, 3, 0)
        self.c_temps = Temps(0, 2, 0)
        self.d_temps = Temps(0, 1, 0)
        self.a_result = Resultat(self.a, self.a_temps)
        self.b_result = Resultat(self.b, self.b_temps)
        self.c_result = Resultat(self.c, self.c_temps)

    def test_add(self):
        self.assertEqual(self.cl.size(), 0)
        self.cl.add(self.a_result)
        self.assertEqual(self.cl.size(), 1)
        self.cl.add(self.b_result)
        self.assertEqual(self.cl.size(), 2)
        self.cl.add(self.c_result)
        self.assertEqual(self.cl.size(), 3)

    def test_get(self):
        self.cl.add(self.a_result)
        self.assertEqual(self.cl.get(self.a),self.a_result)
        self.cl.add(self.b_result)
        self.assertEqual(self.cl.get(self.a), self.a_result)
        self.assertEqual(self.cl.get(self.b), self.b_result)
        self.cl.add(self.c_result)
        self.assertEqual(self.cl.get(self.a), self.a_result)
        self.assertEqual(self.cl.get(self.b), self.b_result)
        self.assertEqual(self.cl.get(self.c), self.c_result)
        self.assertEqual(self.cl.get(self.d), None)

    def test_get_position(self):
        self.cl.add(self.a_result)
        self.assertEqual(self.cl.get_position(self.a), 1)
        self.cl.add(self.b_result)
        self.assertEqual(self.cl.get_position(self.a), 1)
        self.assertEqual(self.cl.get_position(self.b), 2)
        self.cl.add(self.c_result)
        self.assertEqual(self.cl.get_position(self.a), 1)
        self.assertEqual(self.cl.get_position(self.b), 3)
        self.assertEqual(self.cl.get_position(self.c), 2)
        self.assertEqual(self.cl.get_position(self.d), -1)

    def test_remove(self):
        self.cl.add(self.a_result)
        self.cl.add(self.b_result)
        self.cl.add(self.c_result)
        self.assertEqual(self.cl.size(), 3)
        self.assertEqual(self.cl.get_position(self.b), 3)
        self.cl.remove(self.c)
        self.assertEqual(self.cl.size(), 2)
        self.assertEqual(self.cl.get_position(self.b), 2)
        self.assertEqual(self.cl.get_position(self.c), -1)
        self.assertEqual(self.cl.get(self.c), None)
        self.cl.remove(self.b)
        self.assertEqual(self.cl.size(), 1)
        self.assertEqual(self.cl.get_position(self.a), 1)
        self.assertEqual(self.cl.get_position(self.b), -1)
        self.assertEqual(self.cl.get(self.b), None)
        self.cl.remove(self.a)
        self.assertEqual(self.cl.size(), 0)
        self.assertEqual(self.cl.get_position(self.a), -1)
        self.assertEqual(self.cl.get(self.a), None)



if __name__ == '__main__':
    unittest.main()