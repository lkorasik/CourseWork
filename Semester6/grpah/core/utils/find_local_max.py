import numpy as np


def find_local_max(left, right, step, f):
    """
    Найти максимум функции на отрезке

    Вход:
        left - левая граница
        right - правая граница
        step - шаг
        f - функция

    Выход:
        Координату, где достигается минимум
    """
    max_ = -10000
    result = None
    for x in np.arange(left, right, step):
        new_ = f(x)
        if new_ > max_:
            max_ = new_
            result = x
    return result
