import functions
from new.builder.single_newton import single_newton


def bifurcation_stables(time_range, x_start, b_range, a, x12, precision, function, dfunction, f):
    values = dict()

    result = []

    for b in b_range:
        values[b] = []
        x_0 = x_start
        for _ in time_range:
            x_t = f(a, b, x_0)
            if abs(x_t) > 10000:
                break
            x_0 = x_t
        for _ in time_range:
            x_t = f(a, b, x_0)
            if abs(x_t) > 10000:
                break
            x_0 = x_t
            values[b].append(x_t)

    difs = dict()
    for b in b_range:
        min_ = min(values[b])
        max_ = max(values[b])
        difs[b] = max_ - min_

    draw_x = []
    draw_y = []

    for b in b_range:
        x = values[b]
        for x_ in x:
            if x_ > 10:
                continue
            draw_x.append(b)
            draw_y.append(x_)

    result.append([draw_x, draw_y])

    # Нижняя, т.е. \bar{x}_1
    draw_x1 = []
    draw_y1 = []
    x = x12 - (x12 / 4)
    for b in b_range:
        x = single_newton(b, x, precision, lambda b, x: function(1, b, x), lambda b, x: dfunction(1, b, x))
        draw_x1.append(b)
        draw_y1.append(x)

    result.append([draw_x1, draw_y1])

    # Верхняя, т.е. \bar{x}_2
    draw_x2 = []
    draw_y2 = []
    x = x12 + (x12 / 4)
    for b in b_range:
        x = single_newton(b, x, precision, lambda b, x: function(1, b, x), lambda b, x: dfunction(1, b, x))
        if difs[b] > 0.001:
            draw_x2.append(b)
            draw_y2.append(x)

    result.append([draw_x2, draw_y2])

    # Верхняя, т.е. x_1^{-1}
    draw_x3 = []
    draw_y3 = []
    x1 = x12 - (x12 / 4)
    for b in b_range:
        delta_y = single_newton(b, x1, precision, lambda b, x: function(1, b, x), lambda b, x: dfunction(1, b, x))
        f = lambda a, b, c: functions.sf(a, b, c, delta_y)
        x = single_newton(b, x, precision, lambda b, x: f(1, b, x), lambda b, x: functions.dsf(1, b, x))
        x1 = delta_y
        draw_x3.append(b)
        draw_y3.append(x)

    result.append([draw_x3, draw_y3])

    return result