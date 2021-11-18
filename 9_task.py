import turtle as tr
import numpy as np


def polygon(n: int, r: float):
    tr.shape('turtle')
    tr.speed(10)
    tr.penup()
    tr.forward(r)
    tr.pendown()
    an = 2 * r * np.sin(np.pi / n)
    angle_n = 180 - 360 / n
    tr.left(180 - angle_n / 2)
    for side_counter in range(n):
        tr.forward(an)
        tr.left(360 / n)
    tr.right(180 - angle_n / 2)
    tr.penup()
    tr.backward(r)

    return


radius_circumscribed_circle = 10
step = 15
for polygons_counter in range(3, 13):
    polygon(polygons_counter, radius_circumscribed_circle)
    radius_circumscribed_circle += step
