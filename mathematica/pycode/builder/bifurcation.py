def bifurcation(time_range, x_start, b_range, a):
    def f(a, b, x):
        return (a * x ** 2) / ((b + x) ** 6)

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
        x = x_arr[b]
        for x_ in x:
            if x_ > 10:
                continue
            draw_x.append(b)
            draw_y.append(x_)

    return draw_x, draw_y