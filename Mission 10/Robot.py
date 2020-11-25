from graphics import *
import math
import turtle

class Robot():

    def __init__(self,n):
        # nom du robot
        self.__nom__ = n
        # position du robot
        self.__x = 0  # position x du robot
        self.__y = 0  # position y du robot
        # angle en degres radius
        self.__angle = 0
        self.__history = []

    def __str__(self):
        """Imprime un string du type "R2-D2@(100,100) angle: 0.0" reprÃ©sentant les coordonnÃ©es du robot."""
        return str(self.getnom()) + "@(" + str(round(self.getx())) + "," + str(round(self.gety())) + ") angle: " + str(
            self.getangle())

    def getnom(self):
        return self.__nom__

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def getanglerad(self):
        """returns the angle in radials"""
        return self.__angle

    def getangle(self):
        """returns the angle in degrees"""
        return (self.__angle * 180 / math.pi) % 360

    def getHistory(self):
        return self.__history

    def clearHistory(self):
        self.__history = []

    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    def position(self):
        return (self.getx(), self.gety())

    def unplay(self):
        hist = []
        for i in self.getHistory():
            hist.append(i)
        hist.reverse()
        for event, value in hist:
            if event == "forward":
                self.movebackward(value)

            elif event == "backward":
                self.moveforward(value)

            elif event == "right":
                self.turnleft()

            elif event == "left":
                self.turnright()
        self.clearHistory()

    def __move(self, distance, sense):
        """ mÃ©thode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            si sense = 1  il avance de distance pixels
            si sense = -1 il recule de distance pixels
        """
        oldx = self.getx()
        oldy = self.gety()
        orientationx = math.cos(self.getanglerad())
        orientationy = math.sin(self.getanglerad())
        self.setx(oldx + orientationx * distance * sense)
        self.sety(oldy + orientationy * distance * sense)

    def moveforward(self, distance):
        """ fait avancer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.__move(distance, 1)
        self.__history.append(("forward", distance))

    def movebackward(self, distance):
        """ fait reculer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.__move(distance, -1)
        self.__history.append(("backward", distance))

    def __turn(self, direction):
        """ mÃ©thode auxiliaire pour les mÃ©thodes turnright() et turnleft()
            si direction = 1 elle change l'angle du robot de 90 degrÃ©s vers la droite (dans le sens des aiguilles d'une montre)
            si direction = -1 elle change l'angle du robot de 90 degrÃ©s vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.__angle = self.__angle + direction * math.pi / 2

    def turnright(self):
        """ fait tourner le robot de 90 degrÃ©s vers la droite (dans le sens des aiguilles d'une montre)
        """
        self.__turn(1)
        self.__history.append(("right",90))

    def turnleft(self):
        """ fait tourner le robot de 90 degrÃ©s vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.__turn(-1)
        self.__history.append(("left", 90))

class XYRobot(Robot):

    def __init__(self,n):
        super().__init__(n)
        self.__win = GraphWin()

    def __drawFrom(self, oldx, oldy):
        line = Line(Point(oldx, oldy), Point(self.getx(), self.gety()))
        line.draw(self.__win)

    def __move(self,distance, sense):
        oldx = self.getx()
        oldy = self.gety()
        if sense == 1:
            super().moveforward(distance)
        else:
            super().movebackward(distance)
        self.__drawFrom(oldx, oldy)

    def moveforward(self, distance):
        """ fait avancer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.__move(distance, 1)

    def movebackward(self, distance):
        """ fait reculer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.__move(distance, -1)


class TurtleBot(Robot):

    def __init__(self, n):
        super().__init__(n)
        self.__t = turtle.Turtle()
        self.__t.speed("fastest")

    def moveforward(self, d):
        self.__t.forward(d)
        super().moveforward(d)

    def movebackward(self, d):
        self.__t.forward(-d)
        super().movebackward(d)

    def turnright(self):
        self.__t.right(90)
        super().turnright()

    def turnleft(self):
        self.__t.left(90)
        super().turnleft()

if __name__ == "__main__":
    t = TurtleBot("Spot")
    t.moveforward(100)
    t.turnright()
    t.moveforward(100)
    t.turnright()
    t.moveforward(150)
    t.turnleft()
    t.moveforward(200)
    t.unplay()
    while True:
        input("press enter to close")
        break