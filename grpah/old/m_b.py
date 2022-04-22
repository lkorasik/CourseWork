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
    line1 = Line()
    result.append(line1)
    for b in b_range:
        if b < left1 or b > right1:
            continue

        x = values[b]
        for x_ in x:
            line1.add_x(b)
            line1.add_y(m(a, b, x_))

    # Доверительный интервал для 2-цикла
    line1 = Line()
    line2 = Line()
    result.append(line1)
    result.append(line2)
    for b in b_range:
        if b < left2 or b > right2:
            continue

        x = values[b]
        x0, x1 = split(x, 2)

        for i in range(len(x0)):
            r = alg.get_m(2)
            m1_ = r[0].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i])
            m2_ = r[1].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i])
            m1_ = float(m1_)
            m2_ = float(m2_)

            line1.add_x(b)
            line2.add_x(b)
            line1.add_y(m1_)
            line2.add_y(m2_)

    # Доверительный интервал для 4-цикла
    line1 = Line()
    line2 = Line()
    line3 = Line()
    line4 = Line()
    result.append(line1)
    result.append(line2)
    result.append(line3)
    result.append(line4)
    for b in b_range:
        if b < left3 or b > right3:
            continue

        x = values[b]
        x0, x1, x2, x3 = split(x, 4)

        for i in range(len(x0)):
            r = alg.get_m(4)
            m1_ = r[0].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i])
            m2_ = r[1].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i])
            m3_ = r[2].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i])
            m4_ = r[3].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i])
            m1_ = float(m1_)
            m2_ = float(m2_)
            m3_ = float(m3_)
            m4_ = float(m4_)

            line1.add_x(b)
            line2.add_x(b)
            line3.add_x(b)
            line4.add_x(b)
            line1.add_y(m1_)
            line2.add_y(m2_)
            line3.add_y(m3_)
            line4.add_y(m4_)

    # Хаос
    line1 = Line()
    line2 = Line()
    result.append(line1)
    result.append(line2)
    for b in b_range:
        if b < left4 or b > right4:
            continue

        area_bounds = get_absorbing_area(b / 2, lambda x: f(b, x))

        c_1 = area_bounds[0]
        c = area_bounds[1]
        c1 = area_bounds[2]

        m1 = q(b, c) * s(b, c_1) + s(b, c)
        m2 = s(b, c_1)

        line1.add_x(b)
        line2.add_x(b)
        line1.add_y(m1)
        line2.add_y(m2)

    return result
