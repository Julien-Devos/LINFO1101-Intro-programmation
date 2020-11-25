import unittest
#import XYRobot as rob    # test the XYRobot.py file
import Robot as rob   # test the Robot.py file

class XYRobotTest(unittest.TestCase):

    def setUp(self):
        self.r = rob.XYRobot("C3PO")

    def test_init(self):
        self.assertEqual(self.r.getnom(), "C3PO", "Le nom du robot ne correspond pas")
        self.assertEqual(self.r.getx(), 0, "Le robot ne se trouve pas en X = 0")
        self.assertEqual(self.r.gety(), 0, "Le robot ne se trouve pas en Y = 0")
        self.assertEqual(self.r.getanglerad(), 0, "L'angle du robot en rad n'est pas 0")
        self.assertEqual(self.r.getangle(), 0, "L'angle du robot en deg n'est pas 0")
        self.assertEqual(self.r.position(), (0,0), "La position du robot n'est pas (0,0)")

    def test_moveforward(self):
        forward = 50
        x,y = self.r.position()
        expected_position = (float(x + forward),float(y))
        expected_angle = self.r.getangle()
        self.r.moveforward(forward)
        self.assertEqual(self.r.position(), expected_position, "La position de votre robot n'est pas correcte")
        self.assertEqual(self.r.getangle(), expected_angle, "L'angle de votre robot a changé sans raison")

    def test_movebackward(self):
        backward = 50
        x,y = self.r.position()
        expected_position = (float(x - backward), float(y))
        expected_angle = self.r.getangle()
        self.r.movebackward(backward)
        self.assertEqual(self.r.position(), expected_position, "La position de votre robot n'est pas correcte")
        self.assertEqual(self.r.getangle(), expected_angle, "L'angle de votre robot a changé sans raison")


    def test_turnright(self):
        expected_position = self.r.position()
        expected_angle = (self.r.getangle() + 90) % 360
        self.r.turnright()
        self.assertEqual(self.r.position(), expected_position, "Votre robot a avancé ou reculé sans raison")
        self.assertEqual(self.r.getangle(), expected_angle, "Votre robot n'a pas le bon angle en tournant à droite")

    def test_turnleft(self):
        expected_position = self.r.position()
        expected_angle = (self.r.getangle() - 90) % 360
        self.r.turnleft()
        self.assertEqual(self.r.position(), expected_position, "Votre robot a avancé ou reculé sans raison")
        self.assertEqual(self.r.getangle(), expected_angle, "Votre robot n'a pas le bon angle en tournant à gauche")

    def test_getHistory(self):
        expected_History = [("forward",100),("left",90),("backward",152),("right",90),("forward",120),("forward",50)]
        self.r.moveforward(100)
        self.r.turnleft()
        self.r.movebackward(152)
        self.r.turnright()
        self.r.moveforward(120)
        self.r.moveforward(50)
        self.assertEqual(self.r.getHistory(), expected_History, "The History is not correct")

    def test_unplay(self):
        x,y = self.r.position()
        expected_angle = self.r.getangle()
        self.r.moveforward(50)
        self.assertEqual(self.r.position(), (x + 50, y), "¯\_(ツ)_/¯")
        self.assertEqual(self.r.getangle(), expected_angle, "¯\_(ツ)_/¯")
        self.r.unplay()
        self.assertEqual(self.r.position(), (x, y), "¯\_(ツ)_/¯")
        self.assertEqual(self.r.getangle(), expected_angle, "¯\_(ツ)_/¯")
        self.r.movebackward(50)
        self.assertEqual(self.r.position(), (x - 50, y), "¯\_(ツ)_/¯")
        self.assertEqual(self.r.getangle(), expected_angle, "¯\_(ツ)_/¯")
        self.r.unplay()
        self.assertEqual(self.r.position(), (x, y), "¯\_(ツ)_/¯")
        self.assertEqual(self.r.getangle(), expected_angle, "¯\_(ツ)_/¯")
        self.r.turnright()
        self.assertEqual(self.r.position(), (x, y), "¯\_(ツ)_/¯")
        self.assertEqual(self.r.getangle(), (expected_angle + 90) % 360, "¯\_(ツ)_/¯")
        self.r.unplay()
        self.assertEqual(self.r.position(), (x, y), "¯\_(ツ)_/¯")
        self.assertEqual(self.r.getangle(), expected_angle, "¯\_(ツ)_/¯")
        self.r.turnleft()
        self.assertEqual(self.r.position(), (x, y), "¯\_(ツ)_/¯")
        self.assertEqual(self.r.getangle(), (expected_angle - 90) % 360, "¯\_(ツ)_/¯")
        self.r.unplay()
        self.assertEqual(self.r.position(), (x, y), "¯\_(ツ)_/¯")
        self.assertEqual(self.r.getangle(), expected_angle, "¯\_(ツ)_/¯")