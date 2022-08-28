from sympy import Symbol

import r as alg
from functions_pkg import symbols
from algorithms.get_absorbing_area import get_absorbing_area
from algorithms.list_spliter import split
from visual.line import Line


def m_b(b_range, a, left1, right1, left2, right2, left3, right3, left4, right4, m, values, q, s, s_, q_, f):
    alg.setup(q_, s_)
    result = []

    # Доверительный интервал у одного равновесия
    line = Line()
    result.append(line)
    for b in b_range:
        if b < left1 or b > right1:
            continue

        x = values[b]
        for x_ in x:
            line.add_x(b)
            line.add_y(m(a, b, x_))

    # Доверительный интервал для 2-цикла
    lines = [Line() for _ in range(2)]
    for line in lines:
        result.append(line)

    for b in b_range:
        if b < left2 or b > right2:
            continue

        x = values[b]
        x0, x1 = split(x, 2)

        for i in range(len(x0)):
            r = alg.get_m(2)
            m1_ = float(r[0].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]))
            m2_ = float(r[1].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]))

            for line in lines:
                line.add_x(b)

            lines[0].add_y(m1_)
            lines[1].add_y(m2_)

    # Доверительный интервал для 4-цикла
    lines = [Line() for _ in range(4)]
    for line in lines:
        result.append(line)

    for b in b_range:
        if b < left3 or b > right3:
            continue

        x = values[b]
        x0, x1, x2, x3 = split(x, 4)

        for i in range(len(x0)):
            r = alg.get_m(4)
            m1_ = float(
                r[0].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(
                    Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i]))
            m2_ = float(
                r[1].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(
                    Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i]))
            m3_ = float(
                r[2].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(
                    Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i]))
            m4_ = float(
                r[3].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(
                    Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i]))

            for line in lines:
                line.add_x(b)

            lines[0].add_y(m1_)
            lines[1].add_y(m2_)
            lines[2].add_y(m3_)
            lines[3].add_y(m4_)

    # Хаос
    lines = [Line() for _ in range(2)]
    for line in lines:
        result.append(line)

    for b in b_range:
        if b < left4 or b > right4:
            continue

        area_bounds = get_absorbing_area(b / 2, lambda x: f(b, x))

        c_1 = area_bounds[0]
        c = area_bounds[1]
        c1 = area_bounds[2]

        m1 = q(b, c) * s(b, c_1) + s(b, c)
        m2 = s(b, c_1)

        for line in lines:
            line.add_x(b)

        lines[0].add_y(m1)
        lines[1].add_y(m2)

    return result
