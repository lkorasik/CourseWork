import numpy as np


def f(a, b, x):
    return (a * x ** 2) / ((b + x) ** 6)


def find_local_max(left, right, step, a, b):
    max_ = -1
    x = None
    for i in np.arange(left, right, step):
        new_ = f(a, b, i)
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
    c = f(a, b, c_1)
    c1 = f(a, b, c)

    return [c_1, c, c1]


def bifurcation_with_c(time_range, x_start, b_range, a, left, right, step):
    def f(a, b, x):
        return (a * x ** 2) / ((b + x) ** 6)

    x_arr = dict()
    result = []

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
        x = x_arr[b]
        for x_ in x:
            if x_ > 10:
                continue
            draw_x.append(b)
            draw_y.append(x_)

    result.append([draw_x, draw_y])

    draw_x = []
    draw_y1 = []
    draw_y2 = []
    for b in b_range:
        r = get_cs(
            left=left,
            right=right,
            step=step,
            a=a,
            b=b
        )
        draw_x.append(b)
        draw_y1.append(r[1])
        draw_y2.append(r[2])

    result.append([draw_x, draw_y1])
    result.append([draw_x, draw_y2])

    return result
