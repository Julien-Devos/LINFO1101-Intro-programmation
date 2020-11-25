import XYRobot as r
import turtle

class TurtleBot(r.XYRobot):

    def __init__(self,n):
        super().__init__(n)
        self.__t = turtle.Turtle()
        self.__t.speed("fastest")

    def moveforward(self,d):
        self.__t.forward(d)
        super().moveforward(d)

    def movebackward(self,d):
        self.__t.forward(-d)
        super().movebackward(d)

    def turnright(self):
        self.__t.right(90)
        super().turnright()

    def turnleft(self):
        self.__t.left(90)
        super().turnleft()

    def unplay(self):
        hist = []
        for i in self.getHistory():
            hist.append(i)
        hist.reverse()
        for event,value in hist:
            if event == "forward":
                self.movebackward(value)

            elif event == "backward":
                self.moveforward(value)

            elif event == "right":
                self.turnleft()

            elif event == "left":
                self.turnright()
        self.clearHistory()

if __name__ == "__main__":
    t = TurtleBot("Spot")
    t.moveforward(100)
    t.turnright()
    t.moveforward(100)
    t.turnright()
    t.moveforward(150)
    t.turnleft()
    t.moveforward(200)
    print(t.getHistory())
    t.unplay()
    print(t.getHistory())
    while True:
        input("press enter to close")
        break