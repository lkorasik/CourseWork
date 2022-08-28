from algorithms.single_newton import single_newton_unlimited
from visual.line import Line


def bifurcation_with_equilibrium(b_range, x12, precision, function, d_function, f, sf, dsf, bifurcation,
                                 save_all=False):
    result = []

    diffs = dict()
    for b in b_range:
        diffs[b] = max(bifurcation[b]) - min(bifurcation[b])

    # Нижняя, т.е. \bar{x}_1
    line = Line()
    result.append(line)
    x = x12 - (x12 / 4)
    for b in b_range:
        x = single_newton_unlimited(x, precision, lambda x_: function(b, x_), lambda x_: d_function(b, x_))
        line.add_x(b).add_y(x)

    # Верхняя, т.е. \bar{x}_2
    line = Line()
    result.append(line)
    x = x12 + (x12 / 4)
    for b in b_range:
        x = single_newton_unlimited(x, precision, lambda x_: function(b, x_), lambda x_: d_function(b, x_))
        # Находимся в области устойчивого равновесия
        if save_all:
            line.add_x(b).add_y(x)
        elif diffs[b] > 0.001:
            line.add_x(b).add_y(x)

    # Верхняя, т.е. x_1^{-1}
    line = Line()
    result.append(line)
    x1 = x12 - (x12 / 4)
    for b in b_range:
        delta_y = single_newton_unlimited(x1, precision, lambda x_: function(b, x_), lambda x_: d_function(b, x_))
        f = lambda b, c: sf(b, c, delta_y)
        x = single_newton_unlimited(x, precision, lambda x_: f(b, x_), lambda x_: dsf(b, x_))
        x1 = delta_y
        line.add_x(b).add_y(x)

    return result
