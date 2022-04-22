import numpy

from visual.line import Line


def mean(p_range, values):
    line = Line()
    for p in p_range:
        mean_ = numpy.mean(values[p])
        line.add_x(p)
        line.add_y(mean_)

    return line
