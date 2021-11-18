import turtle
import turtle as tr
import numpy as np

def arc(r: float, arc_length:float):
    accuracy = 32
    tr.shape('turtle')
    tr.speed(10)
    tr.penup()
    tr.forward(r)
    tr.pendown()
    an = 2 * r * np.sin(np.pi / accuracy)
    angle_n = 180 - 360 / accuracy
    tr.left(180 - angle_n / 2)
    for side_counter in range(round(accuracy/(360 / arc_length))):
        tr.forward(an)
        tr.left(360 / accuracy)
    tr.right(180 - angle_n / 2)

    return

#face
tr.color('black','yellow')
tr.begin_fill()
arc(150, 360)
tr.end_fill()

#eyes color
tr.color('black', 'white')

#to left eye
tr.penup()
tr.goto(-50, 75)

# left eye
tr.pendown()
tr.begin_fill()
arc(30, 360)
tr.end_fill()

# to right eye
tr.penup()
tr.goto(50, 75)

# right eye
tr.pendown()
tr.begin_fill()
arc(30, 360)
tr.end_fill()

# pupils color
tr.color('black', 'black')

tr.penup()
tr.goto(-50, 75)

tr.pendown()
tr.begin_fill()
arc(20, 360)
tr.end_fill()
tr.penup()

tr.goto(50, 75)
tr.pendown()
tr.begin_fill()
arc(20, 360)
tr.end_fill()

tr.penup()
tr.goto(0, 5)
tr.pendown()
tr.width(10)
tr.goto(0,-50)

tr.penup()
tr.color('red', 'black')
tr.goto(0,0)
tr.left(180)
arc(100, 180)