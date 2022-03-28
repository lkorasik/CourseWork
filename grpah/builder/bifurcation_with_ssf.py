import math

import numpy as np

from algorithms.find_local_max import find_local_max
from algorithms.get_absorbing_area import get_absorbing_area


def bifurcation_with_ssf(b_range, a, left1, right1, left2, right2, left3, right3, left4, right4, m, m1, m2, epsilon, values, f, dfx, s):
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
        x0 = []
        x1 = []
        for i in range(len(x)):
            if i % 2 == 0:
                x0.append(x[i])
            else:
                x1.append(x[i])

        for i in range(len(x0)):
            draw_x2.append(b)

            # Под и над равновесием
            draw_y2_1.append(x0[i] - 3 * epsilon * np.sqrt(np.abs(m1(a, b, x0[i], x1[i]))))
            draw_y2_2.append(x1[i] - 3 * epsilon * np.sqrt(np.abs(m2(a, b, x0[i], x1[i]))))
            draw_y2_3.append(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1(a, b, x0[i], x1[i]))))
            draw_y2_4.append(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2(a, b, x0[i], x1[i]))))

    # Хаос
    draw_x3 = []
    draw_y3_1 = []
    draw_y3_2 = []
    for b in b_range:
        if b < left3 or b > right3:
            continue

        max_ = find_local_max(left3, right3, 0.001, lambda x: f(b, x))
        area_bounds = get_absorbing_area(max_, lambda x: f(b, x))

        c_1 = area_bounds[0]
        c = area_bounds[1]
        c1 = area_bounds[2]

        m1 = (dfx(b, c_1) ** 2) * s(b, c_1) + s(b, f(b, c_1))
        m2 = s(b, c_1)

        draw_x3.append(b)
        draw_y3_1.append(m1)
        draw_y3_2.append(m2) # верх, c - m2 * epsilon * 3 <- норм


    def q(a, b, x):
        return (4 * (a ** 2) * (x ** 2) * ((b - 2 * x) ** 2)) / ((b + x) ** 14)

    def s(a, b, x):
        return (36 * (a ** 2) * (x ** 4)) / ((b + x) ** 14)

    def r(a, b, x, t):
        if t == 0:
            return 0
        else:
            return q(a, b, x[t - 1]) * r(a, b, x, t - 1) + s(a, b, x[t - 1])

    def rq(a, b, x, k):
        result = 1
        for i in range(1, k + 1):
            result *= q(a, b, x[i])
        return result

    def m_(a, b, x, t):
        if t == 1:
            return r(a, b, x, t + 1) / (1 - rq(a, b, x, t))
        else:
            return q(a, b, x[t - 1]) * m_(a, b, x, t - 1) + s(a, b, x[t - 1])

    draw_x4 = []
    draw_y4_1 = []
    draw_y4_2 = []
    draw_y4_3 = []
    draw_y4_4 = []
    draw_y4_5 = []
    draw_y4_6 = []
    draw_y4_7 = []
    draw_y4_8 = []
    for b in b_range:
        if b < left4 or b > right4:
            continue

        x = values[b]
        m1_1 = x[0] + 3 * epsilon * np.sqrt(m_(a, b, x[0:4], 4))
        m1_2 = x[0] - 3 * epsilon * np.sqrt(m_(a, b, x[0:4], 4))
        m2_1 = x[1] + 3 * epsilon * np.sqrt(m_(a, b, x[0:4], 4))
        m2_2 = x[1] - 3 * epsilon * np.sqrt(m_(a, b, x[0:4], 4))
        m3_1 = x[2] + 3 * epsilon * np.sqrt(m_(a, b, x[0:4], 4))
        m3_2 = x[2] - 3 * epsilon * np.sqrt(m_(a, b, x[0:4], 4))
        m4_1 = x[3] + 3 * epsilon * np.sqrt(m_(a, b, x[0:4], 4))
        m4_2 = x[3] - 3 * epsilon * np.sqrt(m_(a, b, x[0:4], 4))

        draw_x4.append(b)
        draw_y4_1.append(m1_1)
        draw_y4_2.append(m1_2)
        draw_y4_3.append(m2_1)
        draw_y4_4.append(m2_2)
        draw_y4_5.append(m3_1)
        draw_y4_6.append(m3_2)
        draw_y4_7.append(m4_1)
        draw_y4_8.append(m4_2)

    return draw_x1, draw_y1_1, draw_y1_2, draw_x2, draw_y2_1, draw_y2_2, draw_y2_3, draw_y2_4, draw_x3, draw_y3_1, draw_y3_2, draw_x4, draw_y4_1, draw_y4_2, draw_y4_3, draw_y4_4, draw_y4_5, draw_y4_6, draw_y4_7, draw_y4_8
