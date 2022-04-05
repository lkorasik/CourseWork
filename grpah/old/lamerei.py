import numpy as np


def lamerei(x_start, time_range, skip, xmin, xmax, f, g):
    x0 = x_start
    result = []
    if skip:
        for _ in time_range:
            x1 = f(x0)
            x0 = x1
    for _ in time_range:
        x1 = f(x0)
        result.append((x0, x0, x0, x1))
        result.append((x0, x1, x1, x1))
        x0 = x1

    draw_x = np.arange(xmin, xmax, 0.01)

    return result, draw_x, g(draw_x), f(draw_x)
