def lamerei(x_start, time_range, skip, f):
    result = []
    x0 = x_start
    if skip:
        for _ in time_range:
            x1 = f(x0)
            x0 = x1
    for _ in time_range:
        x1 = f(x0)
        result.append((x0, x0, x0, x1))
        result.append((x0, x1, x1, x1))
        x0 = x1

    return result
