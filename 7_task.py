import turtle as tr
import numpy as np

tr.shape('turtle')
tr.speed(10)
k = 0.1
fi_rad = 0.1
fi_degr = fi_rad * (180 / np.pi)
for i in range(0, 1000):
    tr.forward(k * fi_rad)
    print(k * fi_rad)
    tr.left(fi_degr)
    fi_rad += 0.1

