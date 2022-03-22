import numpy as np


def single_newton(x_start, precision, function, d_function):
    """Найти один корень с помощью метода Ньютона"""
    x_0 = x_start
    while True:
        x_n = x_0 - function(x_0) / d_function(x_0)
        if np.isnan(x_n):
            break
        if abs(x_n - x_0) < precision:
            break
        x_0 = x_n
    res = x_0
    return res