import turtle as tr
import numpy as np

def circle(r: float):
    accuracy = 18
    tr.shape('turtle')
    tr.speed(10)
    an = 2 * r * np.sin(np.pi / accuracy)
    angle_n = 180 - 360 / accuracy
    tr.left(180 - angle_n / 2)
    for side_counter in range(accuracy):
        tr.forward(an)
        tr.left(360 / accuracy)
    tr.right(180 - angle_n / 2)

    return


r = 40
step = 5
number_of_circles_pair = 10
for i in range(number_of_circles_pair):
    circle(r)
    circle(-r)
    r += step


