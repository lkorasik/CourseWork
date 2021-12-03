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
    #im = ax.imshow(draw)
    m = cleanedList = [x for x in draw_c if str(x) != 'nan']
    print(max(m))
    #im = ax.imshow(draw, cmap='viridis', extent=[min(a_range), max(a_range), min(b_range), max(b_range)], vmin=min(m), vmax=max(m))

    # Используй scatter, теплова якарта не нужна
    im = ax.imshow(draw, cmap='plasma', extent=[min(a_range), max(a_range), min(b_range), max(b_range)], vmin=min(m), vmax=max(m))

    # Rotate the tick labels and set their alignment.
    #plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    # for i in range(len(a_range)):
    #     for j in range(len(b_range)):
    #         ax.text(a_range[i], b_range[j], draw[i][j], ha="center", va="center", color="red")

    ax.set_title("Harvest of local farmers (in tons/year)")
    fig.tight_layout()
    fig.colorbar(im)
    plt.show()
