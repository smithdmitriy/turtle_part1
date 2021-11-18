import turtle as tr
import numpy as np

def circle(r: float):
    tr.shape('turtle')
    tr.speed(10)
    tr.penup()
    tr.forward(r)
    tr.pendown()
    an = 2 * r * np.sin(np.pi / 360)
    angle_n = 180 - 360 / 360
    tr.left(180 - angle_n / 2)
    for side_counter in range(360):
        tr.forward(an)
        tr.left(360 / 360)
    tr.right(180 - angle_n / 2)
    tr.penup()
    tr.backward(r)
    return


r = 20
step = 15
number_of_circles_pair = 5
for i in range(number_of_circles_pair):
    circle(r)
    r += step


