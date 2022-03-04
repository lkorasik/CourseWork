import statistics


def mean(time_range, x_start, b_range, a, f):
    x_arr = dict()

    for b in b_range:
        x_arr[b] = []
        x_0 = x_start
        for t in time_range:
            x_t = f(a, b, x_0)
            if abs(x_t) > 10000:
                break
            x_0 = x_t
        for t in time_range:
            x_t = f(a, b, x_0)
            if abs(x_t) > 10000:
                break
            x_0 = x_t
            x_arr[b].append(x_t)

    draw_x = []
    draw_y = []
    for b in b_range:
        mean_ = statistics.mean(x_arr[b])
        draw_x.append(b)
        draw_y.append(mean_)

    return draw_x, draw_y
