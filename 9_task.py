import turtle as tr
import numpy as np


def polygon(n: int, r:float):
    tr.shape('turtle')
    tr.speed(1)
    an = 2*r*np.sin(np.pi/n)
    tr.left(180 - 180 / n)
    for i in range(n):
        tr.forward(an)
        print(an)
        tr.left(360 / n)
    tr.right(180/n)
    return


r = 30
step = 30

for i in range(3, 10):
    polygon(i,r)
    tr.penup()
    tr.forward(step)
    tr.pendown()
    r += 40


