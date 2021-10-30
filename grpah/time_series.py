"""
Have new realization
"""
import matplotlib.pyplot as plt
import numpy as np

from setup import *


def g(x, b):
    return (a*x**2)/((b+x)**6)


T_range = range(1, 301)
# x_start = 1.2
x_start = 0.0001
b_range = np.arange(0, 0.6, 0.001)

x_arr = dict()

# x_0 возможно эта точка лишняя

#for b in b_range:
# b= 0.563
b = 0.56
x_arr[b] = []
x_0 = x_start
for t in T_range:
    x_t = g(x_0, b)
    x_0 = x_t
for t in T_range:
    x_t = g(x_0, b)
    x_0 = x_t
    x_arr[b].append(x_t)


fig, ax = plt.subplots()
plt.xlabel('t')
plt.ylabel('x')
plt.plot(T_range, x_arr[b], marker='*')
print(b_range)
ax.grid(which='major')

plt.show()
