import numpy as np


def bifurcation_with_ssf(b_range, a, left1, right1, right2, left2, m, m1, m2, epsilon, values):
    bifurcation_x = []
    bifurcation_y = []

    for b in b_range:
        x = values[b]
        for x_ in x:
            bifurcation_x.append(b)
            bifurcation_y.append(x_)

    # Доверительный интервал у одного равновесия
    down_x1 = []
    down_y1 = []
    up_x1 = []
    up_y1 = []
    for b in b_range:
        if b < left1 or b > right1:
            continue

        x = values[b]
        for x_ in x:
            # Под равновесием
            down_x1.append(b)
            down_y1.append(x_ - 3 * epsilon * np.sqrt(m(a, b, x_)))

            # Над равновесием
            up_x1.append(b)
            up_y1.append(x_ + 3 * epsilon * np.sqrt(m(a, b, x_)))

    # Доверительный интервал для 2-цикла
    down_x2 = []
    down_y2 = []
    up_x2 = []
    up_y2 = []
    for b in b_range:
        if b < left2 or b > right1:
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
            down_x2.append(b)
            down_x2.append(b)
            down_y2.append(x0[i] - 3 * epsilon * np.sqrt(np.abs(m1(a, b, x0[i], x1[i]))))
            down_y2.append(x1[i] - 3 * epsilon * np.sqrt(np.abs(m2(a, b, x0[i], x1[i]))))

            down_x2.append(b)
            down_x2.append(b)
            down_y2.append(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1(a, b, x0[i], x1[i]))))
            down_y2.append(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2(a, b, x0[i], x1[i]))))

    return down_x1, down_y1, up_x1, up_y1, down_x2, down_y2, up_x2, up_y2
