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
