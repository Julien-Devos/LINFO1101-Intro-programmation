# Devos Bryan / Devos Julien
# Création du drapeau européen et autres
import turtle

t = turtle.Turtle()
t.speed("fastest")


def european_flag(width):
    """pre: width > 0
       post: create the european flag with the turtle
    """
    t.begin_fill()
    rectangle(width, (width / 3) * 2, "#1E448A")
    t.forward(width / 2)
    t.left(90)
    t.forward(((width / 3) * 2) / 2)
    t.right(90)
    for i in range(1, 13):
        t.left(i * 30)
        t.forward((width) / 4)
        t.right(i * 30)
        star(width / 25)
        t.left(180 + (i * 30))
        t.forward((width) / 4)
        t.right(180 + (i * 30))
    t.right(90)
    t.forward(((width / 3) * 2) / 2)
    t.right(90)
    t.forward(width / 2)
    t.right(180)


def star(width):
    """pre: width > 0
       post: create a star with the turtle
    """
    t.penup()
    t.left(90)
    t.forward(width / 2)
    t.right(18)
    t.color("#FDCB0B")
    t.begin_fill()
    t.pendown()
    for i in range(5):
        t.right(144)
        t.forward(width)
    t.end_fill()
    t.penup()
    t.right(162)
    t.forward(width / 2)
    t.left(90)


def rectangle(width, height, color):
    """pre: width > 0, height > 0, color = ["black", "blue", "green", "red", "magenta", "cyan", "yellow", "white"]
       post: create a rectangle with the turtle
    """
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def three_color_flag(width, color1, color2, color3):
    """pre: width > 0, colorx = ["black", "blue", "green", "red", "magenta", "cyan", "yellow", "white"]
       post: create a three color vertical flag with the turtle
    """
    colors = [color1, color2, color3]
    for i in range(3):
        rectangle(width / 3, (width / 3) * 2, colors[i])
        t.forward(width / 3)


def three_color_flag_h(width, color1, color2, color3):
    """pre: width > 0, colorx = ["black", "blue", "green", "red", "magenta", "cyan", "yellow", "white"]
       post: create a three color horizontal flag with the turtle
    """
    colors = [color1, color2, color3]
    t.penup()
    t.forward(width)
    t.left(90)
    for i in range(3):
        rectangle(width / 3 * 2 / 3, width, colors[i])
        t.forward(width / 3 * 2 / 3)
    t.penup()
    t.left(180)
    t.forward(width / 3 * 2)
    t.left(90)


def lgbt_flag(width):
    colors = ["purple", "blue", "green", "yellow", "orange", "red"]
    t.penup()
    t.forward(width)
    t.left(90)
    for i in range(6):
        rectangle(width / 3 * 2 / 6, width, colors[i])
        t.forward(width / 3 * 2 / 6)
    t.penup()
    t.left(180)
    t.forward(width / 3 * 2)
    t.left(90)


def belgian_flag(width):
    """pre: width > 0
       post: create the belgian flag with the turtle
    """
    three_color_flag(width, "#000000", "#FDDA24", "#EF3340")


def french_flag(width):
    """pre: width > 0
       post: create the french flag with the turtle
    """
    three_color_flag(width, "#0055A4", "#FFFFFF", "#EF4135")


def dutch_flag(width):
    """pre: width > 0
       post: create the dutch flag with the turtle
    """
    three_color_flag_h(width, "#21468B", "#FFFFFF", "#AE1C28")


def german_flag(width):
    """pre: width > 0
       post: create the german flag with the turtle
    """
    three_color_flag_h(width, "#FFCC00", "#FF0000", "#000000")


def luxemburg_flag(width):
    """pre: width > 0
       post: create the luxemburg flag with the turtle
    """
    three_color_flag_h(width, "#00A3E0", "#FFFFFF", "#EF3340")


def presentation():
    """pre: \
       post: shows the personalized presentations of all the flags
    """
    t.penup()
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.right(180)
    european_flag(150)
    t.forward(250)
    european_flag(150)
    t.goto(0.00, -100.00)
    t.right(180)
    t.forward(388)
    t.left(180)
    belgian_flag(100)
    t.right(35)
    t.forward(30)
    dutch_flag(100)
    t.forward(70)
    t.left(35)
    german_flag(100)
    t.forward(50)
    french_flag(100)
    t.left(35)
    t.forward(70)
    luxemburg_flag(100)
    t.forward(30)
    t.right(35)
    lgbt_flag(100)
    t.goto(0.00, 0.00)
    t.left(90)
    for i in range(1, 1000):
        for j in range(0, 8):
            t.right(15)
            colors = ["black", "blue", "green", "red", "magenta", "cyan", "yellow", "white"]
            t.color(colors[j])

presentation()