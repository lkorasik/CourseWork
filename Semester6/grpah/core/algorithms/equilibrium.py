from core.algorithms.single_newton import single_newton
from visual.line import Line


def equilibrium(x12, b_range, precision, function, d_function, d):
    result = []

    # \bar{x}_1, \bar{x}_2, \bar{x}_{-1}
    xs = [x12 - (x12 / 4), x12 + (x12 / 4), 0]
    for x in xs:
        line = Line()
        for b in b_range:
            x = single_newton(x, precision, lambda x: function(b, x), lambda x: d_function(b, x))
            line.add(b, d(b, x))  # Значения производной
        result.append(line)

    line1 = Line()
    line2 = Line()
    result.append(line1)
    result.append(line2)
    for b in b_range:
        line1.add(b, 1)
        line2.add(b, -1)

    return result
