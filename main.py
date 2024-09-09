import turtle as turtl
painter = turtl.Turtle()
screen = turtl.Screen()
painter = turtl.Turtle()



screen.setup(width = 800, height = 800)
painter.speed(0)
painter.penup()
painter.goto(-15, 15)

painter.pendown()

square_amount = int(input("How many squares do you want?  "))

for i in range(square_amount):
    for i in range(4):
        painter.forward(30)
        painter.right(90)
    painter.penup()
    painter.forward(10)
    painter.right(90)


wn = turtl.Screen()
wn.mainloop()
