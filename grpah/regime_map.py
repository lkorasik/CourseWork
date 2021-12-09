import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

from functions import Functions


def build_regime_map(x_0, a_range, b_range, T_range):
    endless = []
    stable = []

    draw_a = []
    draw_b = []
    draw_c = []
    draw = []

    min_ = 10
    max_ = -10
    for y in range(len(a_range)):
        draw.append([])
        for x in range(len(b_range)):
            draw[y].append(0)

    for y in range(len(a_range)):
        a = a_range[y]
        for x in range(len(b_range)):
            b = b_range[x]
            x0 = x_0
            for t in T_range:
                x_t = Functions.f(a, b, x0)
                if abs(x_t) > 10000:
                    endless.append([a, b])
                x0 = x_t
            print(a, b, x0)
            draw_a.append(a)
            draw_b.append(b)
            draw_c.append(x0)
            draw[y][x] = x0

            if min_ > x0:
                min_ = x0
            if max_ < x0:
                max_ = x0

    fig, ax = plt.subplots()
    m = [x for x in draw_c if str(x) != 'nan']
    print(max(m))

    ax.set_title("Harvest of local farmers (in tons/year)")
    fig.tight_layout()
    plt.show()
