def bifurcation_chaos(time_range, x_start, b_range, f, a, epsilon):
    x_arr = dict()

    for b in b_range:
        x_arr[b] = []
        x_0 = x_start
        for t in time_range:
            x_t = f(a, b, x_0, epsilon)
            if abs(x_t) > 10000:
                break
            if abs(x_t) < 1e-5:
                break
            x_0 = x_t
        for t in time_range:
            x_t = f(a, b, x_0, epsilon)
            if abs(x_t) > 10000:
                break
            if abs(x_t) < 1e-5:
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
