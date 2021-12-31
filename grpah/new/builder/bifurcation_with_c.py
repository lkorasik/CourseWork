import extrema


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
        r = extrema.get_cs(
            left,
            right,
            step,
            a,
            b
        )
        draw_x.append(b)
        draw_y1.append(r[1])
        draw_y2.append(r[2])

    result.append([draw_x, draw_y1])
    result.append([draw_x, draw_y2])

    return result
