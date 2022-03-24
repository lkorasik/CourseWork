import numpy as np


def find_local_max(left, right, step, f):
    max_ = -1
    result = None
    for x in np.arange(left, right, step):
        new_ = f(x)
        if new_ > max_:
            max_ = new_
            result = x
    return result


def get_absorbing_area(max_, f):
    c_1 = max_
    c = f(c_1)
    c1 = f(c)

    return [c_1, c, c1]
