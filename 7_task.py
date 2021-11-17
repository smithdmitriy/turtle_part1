import turtle as tr
import numpy as np

tr.shape('turtle')
k = 0.1
fi_rad = 0.1
fi_degr = fi_rad * (180 / np.pi)
for i in range(0, 1000):
    ro = k * fi_rad
    tr.forward(ro)
    tr.left(fi_degr)
    fi_rad += 0.1
    ro += ro
