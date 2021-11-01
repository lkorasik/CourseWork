import numpy as np
import matplotlib.pyplot as plt

a = 1


T_range = range(1, 101)
x_start = 0.05
b_range = np.arange(0, 0.6, 0.001)
b = 0.3
skip = False


def f(x, b):
    return (a * x ** 2)/((b + x) ** 6)


def g(x):
    return a * x


def h(x):
    return (a * x** 2)/((b + x) ** 6)


fig, ax = plt.subplots()
ax.grid(which='major')

x0 = 0.6
result = []
#result.append((x0, x0, 0, x0))
if skip:
    for i in T_range:
        x1 = h(x0)
        x0 = x1
for i in T_range:
    x1 = h(x0)
    result.append((x0, x0, x0, x1))
    result.append((x0, x1, x1, x1))
    x0 = x1


for i in result:
    plt.plot([i[0], i[1]], [i[2], i[3]], 'red')

x = np.arange(0, 2, 0.01)
plt.plot(x, g(x))

x = np.arange(0, 2, 0.00001)
plt.plot(x, h(x))

plt.show()