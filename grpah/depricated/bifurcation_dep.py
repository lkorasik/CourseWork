"""
Have new realization
"""
import matplotlib.pyplot as plt
import numpy as np

from setup import *


def g(x, b):
    return (a*x**2)/((b+x)**6)


T_range = range(1, 1001)
x_start = 0.05
b_range = np.arange(0, 0.6, 0.001)

x_arr = dict()

# x_0 возможно эта точка лишняя

for b in b_range:
    x_arr[b] = []
    x_0 = x_start
    for t in T_range:
        x_t = g(x_0, b)
        if abs(x_t) > 10000:
            break
        x_0 = x_t
    for t in T_range:
        x_t = g(x_0, b)
        if abs(x_t) > 10000:
            break
        x_0 = x_t
        x_arr[b].append(x_t)

draw_x = []
draw_y = []

c = 0
for b in b_range:
    x = x_arr[b]
    for x_ in x:
        if x_ > 10:
            continue
        draw_x.append(b)
        draw_y.append(x_)
        c+=1


fig, ax = plt.subplots()
plt.xlabel('b')
plt.ylabel('x')
#plt.yscale('log')
plt.scatter(draw_x, draw_y, marker='.', rasterized=True, linewidths=0.01)
print(c)

ax.grid(which='major')

plt.show()
