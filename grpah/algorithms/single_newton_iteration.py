import numpy as np


def single_newton_iteration(a, b, x_start, precision, function, dfunction):
    """Найти один корень с помощью метода Ньютона"""
    x_0 = x_start
    for i in range(0, 10 ** 4):
        x_n = x_0 - function(a, b, x_0) / dfunction(a, b, x_0)
        if np.isnan(x_n):
            break
        if abs(x_n - x_0) < precision:
            break
        x_0 = x_n

    return x_0
