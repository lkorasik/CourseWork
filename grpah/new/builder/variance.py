import statistics


def variance(b_range, values):
    draw_x = []
    draw_y = []
    for b in b_range:
        variance_ = statistics.variance(values[b])
        draw_x.append(b)
        draw_y.append(variance_)

    return draw_x, draw_y
