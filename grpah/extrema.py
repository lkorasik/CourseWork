import numpy as np

from functions import Functions


def find_local_max(left, right, step, a, b):
    max_ = -1
    x = None
    for i in np.arange(left, right, step):
        new_ = Functions.f(a, b, i)
        if new_ > max_:
            max_ = new_
            x = i
    return x


def get_cs(left, right, step, a, b):
    c_1 = find_local_max(
        left,
        right,
        step,
        a,
        b
    )
    c = Functions.f(a, b, c_1)
    c1 = Functions.f(a, b, c)

    return [c_1, c, c1]
