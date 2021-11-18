import turtle as tr
import numpy as np

def arc(r: float):
    accuracy = 16
    tr.shape('turtle')
    tr.speed(10)
    an = 2 * r * np.sin(np.pi / accuracy)
    angle_n = 180 - 360 / accuracy
    tr.left(angle_n / 2)
    for side_counter in range(round(accuracy/2)):
        tr.forward(an)
        tr.right(360 / accuracy)
    tr.right(angle_n / 2)
    return


for i in range(10):
    arc(50)
    arc(10)
