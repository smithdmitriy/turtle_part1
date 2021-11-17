import turtle as tr
import numpy as np

tr.shape('turtle')
tr.speed(10)
k = 0.1
fi_rad = 0.15
fi_degr = np.round(fi_rad * (180 / np.pi), decimals=2)
print(fi_degr)
for i in range(0, 1000):
    tr.forward(1)
    tr.left(fi_degr / (k * fi_rad))
    print(fi_degr / (k * fi_rad))
    fi_rad += 0.1/(k * fi_rad)
