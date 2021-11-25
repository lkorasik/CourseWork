import math

from matplotlib import pyplot as plt

import functions
from functions import Functions


class Lyapunov:
    @staticmethod
    def calc(epsilon, a, b_range, x_0, T_range, T, has_next_graphic):
        fig, ax = plt.subplots()
        ax.grid(which='major')

        x_0d = x_0 + epsilon

        dxs = []
        bs = []

        for b in b_range:
            x0 = x_0
            x0d = x_0d
            for t in T_range:
                x0 = Functions.f(a, b, x0)
                x0d = Functions.f(a, b, x0d)
            dxs.append(abs(x0d - x0))
            bs.append(b)

        lambdas = []

        for i in range(len(dxs)):
            x = dxs[i]
            lambdas.append(Functions.lambda_(x, T, epsilon))

        for i in range(len(lambdas)):
            print(str(dxs[i]) + " -> " + str(lambdas[i]))

        plt.plot(lambdas, bs)

        plt.title("Lyapunov")
        fig.canvas.manager.set_window_title('Lyapunov')
        plt.show(block=not has_next_graphic)
