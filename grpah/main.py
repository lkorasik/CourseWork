import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

from funcs import *
from setup import *

x = np.arange(x_min, x_max, step)

fig, ax = plt.subplots()

ax.tick_params(axis='both', which='major', length=20)

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

ax.grid(which='major')

plt.plot(x, y1(x))
plt.plot(x, y2(x))

plt.ylim(x_min, x_max)
plt.xlim(y_min, y_max)

plt.show()
# fig.savefig('C:\\users\\user\\desktop\\demo.png')
