from old.single_newton import single_newton


def equilibrium(x12, b_range, precision, function, d_function, d):
    # Нижняя, т.е. \bar{x}_1
    root = []
    draw_x1 = []
    draw_y1 = []
    x = x12 - (x12 / 4)
    for b in b_range:
        x = single_newton(x, precision, lambda x: function(b, x), lambda x: d_function(b, x))
        root.append(x)
        draw_x1.append(b)
        draw_y1.append(d(b, x))  # Значения производной

    result = [draw_x1, draw_y1]

    # Верхняя, т.е. \bar{x}_2
    root = []
    draw_x2 = []
    draw_y2 = []
    x = x12 + (x12 / 4)
    for b in b_range:
        x = single_newton(x, precision, lambda x: function(b, x), lambda x: d_function(b, x))
        root.append(x)
        draw_x2.append(b)
        draw_y2.append(d(b, x))

    result.append(draw_x2)
    result.append(draw_y2)

    # Верхняя, т.е. x_0
    root = []
    draw_x3 = []
    draw_y3 = []
    x = 0
    for b in b_range:
        x = single_newton(x, precision, lambda x: function(b, x), lambda x: d_function(b, x))
        root.append(x)
        draw_x3.append(b)
        draw_y3.append(d(b, x))

    result.append(draw_x3)
    result.append(draw_y3)

    draw_x4 = []
    draw_y4 = []
    for b in b_range:
        draw_x4.append(b)
        draw_y4.append(1)

    result.append(draw_x4)
    result.append(draw_y4)

    draw_x4 = []
    draw_y4 = []
    for b in b_range:
        draw_x4.append(b)
        draw_y4.append(-1)

    result.append(draw_x4)
    result.append(draw_y4)

    return result
