def time_series_probability(time_range, x_start, b, a, f, epsilon, skip):
    """Построить временной ряд"""
    x_arr = dict()

    x_arr[b] = [x_start]
    x_0 = x_start
    if skip:
        for t in time_range:
            x_t = f(a, b, x_0, epsilon)
            x_0 = x_t
    for t in time_range:
        x_t = f(a, b, x_0, epsilon)
        x_0 = x_t
        x_arr[b].append(x_t)

    time_range = list(time_range)
    time_range.insert(0, 0)

    return time_range, x_arr[b]