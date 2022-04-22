import statistics

from algorithms.bifurcation import bifurcation
from algorithms.mean import mean
from visual.line import Line


def cyclical_mean(time_range, x_start, b_range, f, count):
    line = Line()
    for b in b_range:
        line.add_x(b)

    data = []
    for i in range(count):
        values = bifurcation(time_range, x_start, b_range, f, down_border=None)
        mean_ = mean(b_range, values).y
        data.append(mean_)

    for i in range(len(data[0])):
        arr = []
        for item in data:
            arr.append(item[i])
        line.add_y(statistics.mean(arr))

    return line