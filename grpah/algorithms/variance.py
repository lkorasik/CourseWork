import statistics
from visual.line import Line


def variance(p_range, values):
    line = Line()
    for p in p_range:
        variance_ = statistics.variance(values[p])
        line.add_x(p)
        line.add_y(variance_)

    return line
