import math
import turtle as tr
spiral_step = 2
number_of_spiral_turns = 3
angle = 0
tr.shape('turtle')
tr.speed(10)
x = 1
while True:
    tr.forward(10 + x)
    tr.left(360 - x/2*math.pi)
    x += 1