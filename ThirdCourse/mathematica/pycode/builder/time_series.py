def time_series(time_range, x_start, b, a, f, skip):
    """Построить временной ряд"""
    x_arr = dict()

    # x_0 возможно эта точка лишняя
    x_arr[b] = []
    x_0 = x_start
    if skip:
        for t in time_range:
            x_t = f(a, b, x_0)
            x_0 = x_t
    for t in time_range:
        x_t = f(a, b, x_0)
        x_0 = x_t
        x_arr[b].append(x_t)

    return time_range, x_arr[b]
