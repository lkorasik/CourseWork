from new.algorithms.converter import convert_dict_to_lists
from new.builder.single_newton import single_newton


def bifurcation_with_equilibrium(b_range, x12, precision, function, d_function, f, sf, dsf, bifurcation):
    result = []

    diffs = dict()
    for b in b_range:
        min_ = min(bifurcation[b])
        max_ = max(bifurcation[b])
        diffs[b] = max_ - min_

    draw_x, draw_y = convert_dict_to_lists(bifurcation)

    result.append([draw_x, draw_y])

    # Нижняя, т.е. \bar{x}_1
    draw_x1 = []
    draw_y1 = []
    x = x12 - (x12 / 4)
    for b in b_range:
        x = single_newton(x, precision, lambda x: function(b, x), lambda x: d_function(b, x))
        draw_x1.append(b)
        draw_y1.append(x)

    result.append([draw_x1, draw_y1])

    # Верхняя, т.е. \bar{x}_2
    draw_x2 = []
    draw_y2 = []
    x = x12 + (x12 / 4)
    for b in b_range:
        x = single_newton(x, precision, lambda x: function(b, x), lambda x: d_function(b, x))
        if diffs[b] > 0.001:
            draw_x2.append(b)
            draw_y2.append(x)

    result.append([draw_x2, draw_y2])

    # Верхняя, т.е. x_1^{-1}
    draw_x3 = []
    draw_y3 = []
    x1 = x12 - (x12 / 4)
    for b in b_range:
        delta_y = single_newton(x1, precision, lambda x: function(b, x), lambda x: d_function(b, x))
        f = lambda b, c: sf(b, c, delta_y)
        x = single_newton(x, precision, lambda x: f(b, x), lambda x: dsf(b, x))
        x1 = delta_y
        draw_x3.append(b)
        draw_y3.append(x)

    result.append([draw_x3, draw_y3])

    return result
