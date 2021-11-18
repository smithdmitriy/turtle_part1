import turtle as tr
import numpy as np

def arc(r: float):
    accuracy = 16
    tr.shape('turtle')
    tr.speed(10)
    an = 2 * r * np.sin(np.pi / accuracy)
    angle_n = 180 - 360 / accuracy
    tr.left(180 - angle_n / 2)
    for side_counter in range(round(accuracy/2)):
        tr.forward(an)
        tr.left(360 / accuracy)
    tr.right(180 - angle_n / 2)

    return


while True:
    arc(50)
    arc(15)
