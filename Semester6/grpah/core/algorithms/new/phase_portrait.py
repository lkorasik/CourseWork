from visual.line import Line


def phase_portrait(time_range, x_start, y_start, x, y, skip):
    line = Line().add(x_start, y_start)

    x_i = x_start
    y_i = y_start
    if skip:
        for _ in time_range:
            nx = x(x_i, y_i)
            ny = y(x_i, y_i)
            x_i = nx
            y_i = ny
    for _ in time_range:
        nx = x(x_i, y_i)
        ny = y(x_i, y_i)
        x_i = nx
        y_i = ny
        line.add(nx, ny)

    return line
