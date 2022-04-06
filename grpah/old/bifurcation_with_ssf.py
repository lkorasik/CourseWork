import numpy as np
from sympy import Symbol

from old.get_absorbing_area import get_absorbing_area
from old.list_spliter import split
import r as Alg


def bifurcation_with_ssf(b_range, a, left1, right1, left2, right2, left3, right3, left4, right4, m, m1, m2, epsilon, values, f, s, q, s_, q_):
    # Доверительный интервал у одного равновесия
    draw_x1 = []
    draw_y1_1 = []
    draw_y1_2 = []
    for b in b_range:
        if b < left1 or b > right1:
            continue

        x = values[b]
        for x_ in x:
            draw_x1.append(b)

            # Под и над равновесием
            draw_y1_1.append(x_ - 3 * epsilon * np.sqrt(m(a, b, x_)))
            draw_y1_2.append(x_ + 3 * epsilon * np.sqrt(m(a, b, x_)))

    Alg.setup(q_, s_)

    # Доверительный интервал для 2-цикла
    draw_x2 = []
    draw_y2_1 = []
    draw_y2_2 = []
    draw_y2_3 = []
    draw_y2_4 = []
    for b in b_range:
        if b < left2 or b > right2:
            continue

        x = values[b]
        x0, x1 = split(x, 2)

        for i in range(len(x0)):
            draw_x2.append(b)

            r = Alg.get_m(2)
            m1_ = r[0].subs(Symbol("a"), a).subs(Symbol("b"), b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i])
            m2_ = r[1].subs(Symbol("a"), a).subs(Symbol("b"), b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i])
            m1_ = float(m1_)
            m2_ = float(m2_)

            # Под и над равновесием
            draw_y2_1.append(x0[i] - 3 * epsilon * np.sqrt(np.abs(m1_)))
            draw_y2_2.append(x1[i] - 3 * epsilon * np.sqrt(np.abs(m2_)))
            draw_y2_3.append(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1_)))
            draw_y2_4.append(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2_)))

    # Доверительный интервал для 4-цикла
    draw_x3 = []
    draw_y3_1 = []
    draw_y3_2 = []
    draw_y3_3 = []
    draw_y3_4 = []
    draw_y3_5 = []
    draw_y3_6 = []
    draw_y3_7 = []
    draw_y3_8 = []
    for b in b_range:
        if b < left4 or b > right4:
            continue

        x = values[b]
        x0, x1, x2, x3 = split(x, 4)

        for i in range(len(x0)):
            draw_x3.append(b)

            r = Alg.get_m(4)
            m1_ = r[0].subs(Symbol("a"), a).subs(Symbol("b"), b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i])
            m2_ = r[1].subs(Symbol("a"), a).subs(Symbol("b"), b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i])
            m3_ = r[2].subs(Symbol("a"), a).subs(Symbol("b"), b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i])
            m4_ = r[3].subs(Symbol("a"), a).subs(Symbol("b"), b).subs(Symbol("x1"), x0[i]).subs(Symbol("x2"), x1[i]).subs(Symbol("x3"), x2[i]).subs(Symbol("x4"), x3[i])
            m1_ = float(m1_)
            m2_ = float(m2_)
            m3_ = float(m3_)
            m4_ = float(m4_)

            # Под и над равновесием
            draw_y3_1.append(x0[i] - 3 * epsilon * np.sqrt(np.abs(m1_)))
            draw_y3_2.append(x1[i] - 3 * epsilon * np.sqrt(np.abs(m2_)))
            draw_y3_3.append(x2[i] - 3 * epsilon * np.sqrt(np.abs(m3_)))
            draw_y3_4.append(x3[i] - 3 * epsilon * np.sqrt(np.abs(m4_)))
            draw_y3_5.append(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1_)))
            draw_y3_6.append(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2_)))
            draw_y3_7.append(x2[i] + 3 * epsilon * np.sqrt(np.abs(m3_)))
            draw_y3_8.append(x3[i] + 3 * epsilon * np.sqrt(np.abs(m4_)))

    # Хаос
    draw_x4 = []
    draw_y4_1 = []
    draw_y4_2 = []
    for b in b_range:
        if b < left3 or b > right3:
            continue

        # max_ = find_local_max(left3, right3, 0.001, lambda x: f(b, x))
        area_bounds = get_absorbing_area(b/2, lambda x: f(b, x))

        c_1 = area_bounds[0]
        c = area_bounds[1]
        c1 = area_bounds[2]

        m1 = q(b, c) * s(b, c_1) + s(b, c)
        m2 = s(b, c_1)

        draw_x4.append(b)
        draw_y4_1.append(c1 - 3 * epsilon * np.sqrt(m1))
        draw_y4_2.append(c + 3 * epsilon * np.sqrt(m2))

    return draw_x1, draw_y1_1, draw_y1_2, draw_x2, draw_y2_1, draw_y2_2, draw_y2_3, draw_y2_4, draw_x3, draw_y3_1, draw_y3_2, draw_y3_3, draw_y3_4, draw_y3_5, draw_y3_6, draw_y3_7, draw_y3_8
