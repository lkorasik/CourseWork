import numpy as np

from new.builder.extrema import find_local_max, get_absorbing_area


def bifurcation_with_ssf(b_range, a, left1, right1, left2, right2, left3, right3, m, m1, m2, epsilon, values, f, dfx, s):
    bifurcation_x = []
    bifurcation_y = []

    for b in b_range:
        x = values[b]
        for x_ in x:
            bifurcation_x.append(b)
            bifurcation_y.append(x_)

    # Доверительный интервал у одного равновесия
    x_arr = []
    y_arr = []
    for b in b_range:
        if b < left1 or b > right1:
            continue

        x = values[b]
        for x_ in x:
            # Под равновесием
            x_arr.append(b)
            y_arr.append(x_ - 3 * epsilon * np.sqrt(m(a, b, x_)))

            # Над равновесием
            x_arr.append(b)
            y_arr.append(x_ + 3 * epsilon * np.sqrt(m(a, b, x_)))

    # Доверительный интервал для 2-цикла
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
            # Под равновесием
            x_arr.append(b)
            x_arr.append(b)
            y_arr.append(x0[i] - 3 * epsilon * np.sqrt(np.abs(m1(a, b, x0[i], x1[i]))))
            y_arr.append(x1[i] - 3 * epsilon * np.sqrt(np.abs(m2(a, b, x0[i], x1[i]))))

            # Над равновесием
            x_arr.append(b)
            x_arr.append(b)
            y_arr.append(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1(a, b, x0[i], x1[i]))))
            y_arr.append(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2(a, b, x0[i], x1[i]))))

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

        print(b, m1, m2)

        x_arr.append(b)
        x_arr.append(b)
        y_arr.append(m1)
        y_arr.append(m2)

    return x_arr, y_arr
