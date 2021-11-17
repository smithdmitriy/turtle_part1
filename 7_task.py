import numpy as np
import turtle as tr
spiral_step = 2
number_of_spiral_turns = 3
angle = 5
tr.shape('turtle')
tr.speed(10000)
i = 0
k = 20
#for i in np.arange(0, 2*np.pi, np.pi/64):
while True:
    tr.goto(np.sin(i)*k, np.cos(i)*k)
    i +=0.01
    k *= 1.001
   # tr.left(np.cos(x))
  #  tr.forward(np.cos(i)*10)
