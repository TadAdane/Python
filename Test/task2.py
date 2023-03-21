import requests
import numpy as np
import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []

A1 = 1
A2 = 5
B1 = 2
B2 = 5

for n in np.arange(0, 2.02, 0.02):
    x.append(n)
    y1.append(A1 * n ** 3 + B1 * n)
    y2.append(A2 * n ** 3 + B2 * n)

plt.figure()
plt.plot(x, y1)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y2)
plt.title('Y(x) = Ax^3 + Bx')
plt.legend()
plt.show()

