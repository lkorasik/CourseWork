import numpy as np
from sympy import Symbol

from functions_pkg import symbols
from visual.line import Line
from algorithms.get_absorbing_area import get_absorbing_area
from old.list_spliter import split
import r as Alg


def bifurcation_with_ssf(b_range, a, left1, right1, left2, right2, left3, right3, left4, right4, m, epsilon, values, f, s, q, s_, q_):
    result = []

    # Доверительный интервал у одного равновесия
    line1 = Line()
    line2 = Line()
    result.append(line1)
    result.append(line2)
    for b in b_range:
        if b < left1 or b > right1:
            continue

        x = values[b]
        for x_ in x:
            line1.add_x(b)
            line2.add_x(b)
            line1.add_y(x_ - 3 * epsilon * np.sqrt(m(a, b, x_)))
            line2.add_y(x_ + 3 * epsilon * np.sqrt(m(a, b, x_)))

    Alg.setup(q_, s_)

    # Доверительный интервал для 2-цикла
    line1 = Line()
    line2 = Line()
    line3 = Line()
    line4 = Line()
    result.append(line1)
    result.append(line2)
    result.append(line3)
    result.append(line4)
    for b in b_range:
        if b < left2 or b > right2:
            continue

        x = values[b]
        x0, x1 = split(x, 2)

        for i in range(len(x0)):
            r = Alg.get_m(2)
            m1_ = r[0].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i])
            m2_ = r[1].subs(symbols.a, a).subs(symbols.b, b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i])
            # m1_ = r[0].subs(Symbol("a"), a).subs(Symbol("b"), b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i])
            # m2_ = r[1].subs(Symbol("a"), a).subs(Symbol("b"), b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i])
            m1_ = float(m1_)
            m2_ = float(m2_)

            line1.add_x(b)
            line2.add_x(b)
            line3.add_x(b)
            line4.add_x(b)
            line1.add_y(x0[i] - 3 * epsilon * np.sqrt(np.abs(m1_)))
            line2.add_y(x1[i] - 3 * epsilon * np.sqrt(np.abs(m2_)))
            line3.add_y(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1_)))
            line4.add_y(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2_)))

    # Доверительный интервал для 4-цикла
    line1 = Line()
    line2 = Line()
    line3 = Line()
    line4 = Line()
    line5 = Line()
    line6 = Line()
    line7 = Line()
    line8 = Line()
    result.append(line1)
    result.append(line2)
    result.append(line3)
    result.append(line4)
    result.append(line5)
    result.append(line6)
    result.append(line7)
    result.append(line8)
    for b in b_range:
        if b < left4 or b > right4:
            continue

        x = values[b]
        x0, x1, x2, x3 = split(x, 4)

        for i in range(len(x0)):
            r = Alg.get_m(4)
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
            line5.add_x(b)
            line6.add_x(b)
            line7.add_x(b)
            line8.add_x(b)

            line1.add_y(x0[i] - 3 * epsilon * np.sqrt(np.abs(m1_)))
            line2.add_y(x1[i] - 3 * epsilon * np.sqrt(np.abs(m2_)))
            line3.add_y(x2[i] - 3 * epsilon * np.sqrt(np.abs(m3_)))
            line4.add_y(x3[i] - 3 * epsilon * np.sqrt(np.abs(m4_)))
            line5.add_y(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1_)))
            line6.add_y(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2_)))
            line7.add_y(x2[i] + 3 * epsilon * np.sqrt(np.abs(m3_)))
            line8.add_y(x3[i] + 3 * epsilon * np.sqrt(np.abs(m4_)))

    # Хаос
    line1 = Line()
    line2 = Line()
    result.append(line1)
    result.append(line2)
    for b in b_range:
        if b < left3 or b > right3:
            continue

        area_bounds = get_absorbing_area(b/2, lambda x: f(b, x))

        c_1 = area_bounds[0]
        c = area_bounds[1]
        c1 = area_bounds[2]

        m1 = q(b, c) * s(b, c_1) + s(b, c)
        m2 = s(b, c_1)

        line1.add_x(b)
        line2.add_x(b)
        line1.add_y(c1 - 3 * epsilon * np.sqrt(m1))
        line2.add_y(c + 3 * epsilon * np.sqrt(m2))

    return result
