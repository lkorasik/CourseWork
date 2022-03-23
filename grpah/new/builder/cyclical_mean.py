import statistics

from new.builder.bifurcation import bifurcation
from new.builder.mean import mean


def cyclical_mean(time_range, x_start, b_range, a, f, count):
    draw_x = []
    for b in b_range:
        draw_x.append(b)

    data = []
    for i in range(count):
        values = bifurcation(time_range, x_start, b_range, lambda b, x: f(1, b, x))
        draw_y = mean(b_range, values)[1]
        data.append(draw_y)

    length = len(data[0])
    result = []
    for i in range(length):
        arr = []
        for item in data:
            arr.append(item[i])
        result.append(statistics.mean(arr))

    return draw_x, result
