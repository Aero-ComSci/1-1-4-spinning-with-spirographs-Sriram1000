import turtle as turtl
import random

painter = turtl.Turtle()
screen = turtl.Screen()


square_amount = screen.textinput("How many squares do you want?", "Enter a number:")
square_amount = int(square_amount)

painter.screen.bgcolor("light blue")
painter.speed(0)
painter.penup()
painter.goto(-15, 15)
painter.pendown()
painter.pensize(5)

SquareSideLength=30

for i in range(square_amount):
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    PaintColor=random.choice(colors)
    painter.color(PaintColor)
    for i in range(4):
        painter.forward(SquareSideLength)
        painter.right(90)
    painter.penup()
    painter.left(90)
    painter.forward(30)
    painter.left(90)
    painter.forward(30)
    painter.right(180)
    painter.pendown()
    SquareSideLength += 60


screen.mainloop()
