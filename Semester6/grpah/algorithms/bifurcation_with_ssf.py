import numpy as np
from sympy import Symbol

from models.hassel import symbols
from visual.line import Line
from core.utils.get_absorbing_area import get_absorbing_area
from core.utils.list_spliter import split
from algorithms import generator as Alg


def bifurcation_with_ssf(b_range, a, borders, m, epsilon, values, f, s, q, s_, q_):
    result = []

    # Доверительный интервал у одного равновесия
    lines = [Line() for _ in range(2)]
    for line in lines:
        result.append(line)

    for b in b_range:
        if b < borders[0][0] or b > borders[0][1]:
            continue

        x = values[b]
        for x_ in x:
            for line in lines:
                line.add_x(b)

            lines[0].add_y(x_ - 3 * epsilon * np.sqrt(m(a, b, x_)))
            lines[1].add_y(x_ + 3 * epsilon * np.sqrt(m(a, b, x_)))

    Alg.setup(q_, s_)

    # Доверительный интервал для 2-цикла
    lines = [Line() for _ in range(4)]
    for line in lines:
        result.append(line)

    for b in b_range:
        if b < borders[1][0] or b > borders[1][1]:
            continue

        x = values[b]
        x0, x1 = split(x, 2)

        for i in range(len(x0)):
            all_m = Alg.get_m(2)
            m1_ = float(
                all_m[0].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]))
            m2_ = float(
                all_m[1].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]))

            for line in lines:
                line.add_x(b)

            lines[0].add_y(x0[i] - 3 * epsilon * np.sqrt(np.abs(m1_)))
            lines[1].add_y(x1[i] - 3 * epsilon * np.sqrt(np.abs(m2_)))
            lines[2].add_y(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1_)))
            lines[3].add_y(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2_)))

    # Доверительный интервал для 4-цикла
    lines = [Line() for _ in range(8)]
    for line in lines:
        result.append(line)

    for b in b_range:
        if b < borders[2][0] or b > borders[2][1]:
            continue

        x = values[b]
        x0, x1, x2, x3 = split(x, 4)

        for i in range(len(x0)):
            all_m = Alg.get_m(4)
            m1_ = float(
                all_m[0].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(
                    Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i]))
            m2_ = float(
                all_m[1].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(
                    Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i]))
            m3_ = float(
                all_m[2].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(
                    Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i]))
            m4_ = float(
                all_m[3].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(
                    Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i]))

            for line in lines:
                line.add_x(b)

            lines[0].add_y(x0[i] - 3 * epsilon * np.sqrt(np.abs(m1_)))
            lines[1].add_y(x1[i] - 3 * epsilon * np.sqrt(np.abs(m2_)))
            lines[2].add_y(x2[i] - 3 * epsilon * np.sqrt(np.abs(m3_)))
            lines[3].add_y(x3[i] - 3 * epsilon * np.sqrt(np.abs(m4_)))
            lines[4].add_y(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1_)))
            lines[5].add_y(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2_)))
            lines[6].add_y(x2[i] + 3 * epsilon * np.sqrt(np.abs(m3_)))
            lines[7].add_y(x3[i] + 3 * epsilon * np.sqrt(np.abs(m4_)))

    # Хаос
    lines = [Line() for _ in range(2)]
    for line in lines:
        result.append(line)

    for b in b_range:
        if b < borders[3][0] or b > borders[3][1]:
            continue

        area_bounds = get_absorbing_area(b / 2, lambda x: f(b, x))

        c_1 = area_bounds[0]
        c = area_bounds[1]
        c1 = area_bounds[2]

        m1 = q(b, c) * s(b, c_1) + s(b, c)
        m2 = s(b, c_1)

        for line in lines:
            line.add_x(b)

        lines[0].add_y(c1 - 3 * epsilon * np.sqrt(m1))
        lines[1].add_y(c + 3 * epsilon * np.sqrt(m2))

    return result
