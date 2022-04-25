from algorithms.single_newton import single_newton
from visual.line import Line


def equilibrium(x12, b_range, precision, function, d_function, d):
    result = []

    # Нижняя, т.е. \bar{x}_1
    root = []
    line = Line()
    result.append(line)
    x = x12 - (x12 / 4)
    for b in b_range:
        x = single_newton(x, precision, lambda x: function(b, x), lambda x: d_function(b, x))
        root.append(x)
        line.add_x(b).add_y(d(b, x))  # Значения производной

    # Верхняя, т.е. \bar{x}_2
    root = []
    line = Line()
    result.append(line)
    x = x12 + (x12 / 4)
    for b in b_range:
        x = single_newton(x, precision, lambda x: function(b, x), lambda x: d_function(b, x))
        root.append(x)
        line.add_x(b).add_y(d(b, x))

    # Верхняя, т.е. \bar{x}_{-1}
    root = []
    line = Line()
    result.append(line)
    x = 0
    for b in b_range:
        x = single_newton(x, precision, lambda x: function(b, x), lambda x: d_function(b, x))
        root.append(x)
        line.add_x(b).add_y(d(b, x))

    line1 = Line()
    line2 = Line()
    result.append(line1)
    result.append(line2)
    for b in b_range:
        line1.add_x(b).add_y(1)
        line2.add_x(b).add_y(-1)

    return result
