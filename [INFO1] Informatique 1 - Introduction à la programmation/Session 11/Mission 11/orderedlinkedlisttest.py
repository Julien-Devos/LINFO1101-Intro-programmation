import unittest
from orderedlinkedlist import OrderedLinkedList
from coureur import Coureur
from resultat import Resultat
from temps import Temps

class OrderedLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.l = OrderedLinkedList()
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
        self.assertEqual(self.l.first(), None)
        self.l.add(self.a_result)
        self.assertEqual(self.l.first().value()[0], self.a.nom())
        self.assertEqual(self.l.first().value()[1], self.a_result)
        self.l.add(self.b_result)
        self.assertEqual(self.l.first().value()[0], self.a.nom())
        self.assertEqual(self.l.first().value()[1], self.a_result)
        self.assertEqual(self.l.first().next().value()[0], self.b.nom())
        self.assertEqual(self.l.first().next().value()[1], self.b_result)
        self.l.add(self.c_result)
        self.assertEqual(self.l.first().value()[0], self.a.nom())
        self.assertEqual(self.l.first().value()[1], self.a_result)
        self.assertEqual(self.l.first().next().value()[0], self.c.nom())
        self.assertEqual(self.l.first().next().value()[1], self.c_result)
        self.assertEqual(self.l.first().next().next().value()[0], self.b.nom())
        self.assertEqual(self.l.first().next().next().value()[1], self.b_result)

    def test_get(self):
        self.l.add(self.a_result)
        self.l.add(self.b_result)
        self.l.add(self.c_result)
        self.assertEqual(self.l.get(self.a), self.a_result)
        self.assertEqual(self.l.get(self.b), self.b_result)
        self.assertEqual(self.l.get(self.c), self.c_result)

    def test_get_position(self):
        self.l.add(self.a_result)
        self.l.add(self.b_result)
        self.l.add(self.c_result)
        self.assertEqual(self.l.get_position(self.a), 1)
        self.assertEqual(self.l.get_position(self.b), 3)
        self.assertEqual(self.l.get_position(self.c), 2)

    def test_remove(self):
        self.l.add(self.a_result)
        self.l.add(self.b_result)
        self.l.add(self.c_result)
        self.assertEqual(self.l.first().value()[0], self.a.nom())
        self.assertEqual(self.l.first().value()[1], self.a_result)
        self.assertEqual(self.l.first().next().value()[0], self.c.nom())
        self.assertEqual(self.l.first().next().value()[1], self.c_result)
        self.assertEqual(self.l.first().next().next().value()[0], self.b.nom())
        self.assertEqual(self.l.first().next().next().value()[1], self.b_result)
        self.l.remove(self.c)
        self.assertEqual(self.l.first().value()[0], self.a.nom())
        self.assertEqual(self.l.first().value()[1], self.a_result)
        self.assertEqual(self.l.first().next().value()[0], self.b.nom())
        self.assertEqual(self.l.first().next().value()[1], self.b_result)


if __name__ == '__main__':
    unittest.main()