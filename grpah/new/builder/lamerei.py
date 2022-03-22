import numpy as np


def lamerei(a, x_start, b, time_range, skip, xmin, xmax, f, g):
    total = []

    x0 = x_start
    result = []
    if skip:
        for i in time_range:
            x1 = f(a, b, x0)
            x0 = x1
    for i in time_range:
        x1 = f(a, b, x0)
        result.append((x0, x0, x0, x1))
        result.append((x0, x1, x1, x1))
        x0 = x1

    total.append(result)

    x = np.arange(xmin, xmax, 0.01)
    total.append([x, g(a, x)])
    total.append([x, f(a, b, x)])

    return total