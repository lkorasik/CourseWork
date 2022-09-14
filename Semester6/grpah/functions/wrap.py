import numpy


def wrap(func):
    def inner(val_a, val_b, val_x, val_epsilon):
        val_eta = numpy.random.normal(0, 1) * val_epsilon
        return float(func(val_a, val_b, val_x, val_eta))
    return inner