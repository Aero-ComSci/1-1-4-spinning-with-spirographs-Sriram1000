import turtle as turtl
import random

painter = turtl.Turtle()
screen = turtl.Screen()
screen.setup(width = 800, height = 800)

square_amount = screen.textinput("How many squares do you want?", "Input a number 1-5:")
square_amount = int(square_amount)

painter.screen.bgcolor("light blue")
painter.speed(2)
painter.penup()
painter.goto(-350, 0)
painter.pendown()
painter.pensize(5)


for i in range(square_amount):
    for i in range(4):
        painter.forward(100)
        painter.right(90)
    painter.penup()
    painter.forward(150)
    painter.pendown()


screen.mainloop()
