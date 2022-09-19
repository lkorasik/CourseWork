from core.algorithms.old.single_newton import single_newton
from visual.line import Line


def bifurcation_with_equilibrium(b_range, x12, precision, function, d_function, f, sf, dsf, bifurcation,
                                 save_all=False):
    """
    Вычислить точки равновесий для изображения их на графике бифуркации

    Вход:
        b_range - итератор по значениям параметра
        x12
        precision
        function
        d_function
        f
        sf
        dsf
        bifurcation - словарь со значениями графика бифуркации. Ключ - параметр, значения - значения функции
        save_all - сохранять ли данные в области устойчивого равновесия

    Выход:
        line1
        line2
        line_1
    """
    diffs = dict()
    for b in b_range:
        diffs[b] = max(bifurcation[b]) - min(bifurcation[b])

    # Нижняя, т.е. \bar{x}_1
    line1 = Line()
    x = x12 - (x12 / 4)
    for b in b_range:
        x = single_newton(x, precision, lambda x_: function(b, x_), lambda x_: d_function(b, x_))
        line1.add(b, x)

    # Верхняя, т.е. \bar{x}_2
    line2 = Line()
    x = x12 + (x12 / 4)
    for b in b_range:
        x = single_newton(x, precision, lambda x_: function(b, x_), lambda x_: d_function(b, x_))
        # Находимся в области устойчивого равновесия
        if save_all:
            line2.add(b, x)
        elif diffs[b] > 0.001:
            line2.add(b, x)

    # Верхняя, т.е. x_1^{-1}
    line_1 = Line()
    x1 = x12 - (x12 / 4)
    for b in b_range:
        delta_y = single_newton(x1, precision, lambda x_: function(b, x_), lambda x_: d_function(b, x_))
        f = lambda b, c: sf(b, c, delta_y)
        x = single_newton(x, precision, lambda x_: f(b, x_), lambda x_: dsf(b, x_))
        x1 = delta_y
        line_1.add(b, x)

    return line1, line2, line_1
