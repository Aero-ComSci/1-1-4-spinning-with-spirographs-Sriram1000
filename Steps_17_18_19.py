import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()
painter.speed(0)

x = -200
y = 0
move_x = 1
move_y = 1

#Step 19
while True:
    while (x < 0):

        while (y < 100):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = -1
    
        while (y > 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = 1

    #Step 17
    while (x < 200):

        while (y < 100):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = -1
    
        while (y > 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = 1

    #Step 18
    painter.penup()
    painter.goto(-200, 0)
    painter.pendown()
    painter.speed(0)
    x = -200
    y = 0
    move_x = 1
    move_y = -1

    while (x < 0):

        while (y > -100):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = 1
    
        while (y < 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = -1

    while (x < 200):

        while (y > -100):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = 1
    
        while (y < 0):
            x = x + move_x
            y = y + move_y
            painter.goto(x,y)
        move_y = -1




wn = trtl.Screen()
wn.mainloop()
