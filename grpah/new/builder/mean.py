import statistics


def mean(b_range, values):
    draw_x = []
    draw_y = []
    for b in b_range:
        mean_ = statistics.mean(values[b])
        draw_x.append(b)
        draw_y.append(mean_)

    return draw_x, draw_y
