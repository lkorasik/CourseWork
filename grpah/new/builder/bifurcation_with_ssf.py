import numpy as np


def bifurcation_with_ssf(time_range, x_start, b_range, a, left1, right1, left2, right2, m, m1, m2, epsilon, f):
    x_arr = dict()

    for b in b_range:
        x_arr[b] = []
        x_0 = x_start
        for t in time_range:
            x_t = f(a, b, x_0)
            if abs(x_t) > 10000:
                break
            if abs(x_t) < 1e-5:
                break
            x_0 = x_t
        for t in time_range:
            x_t = f(a, b, x_0)
            if abs(x_t) > 10000:
                break
            if abs(x_t) < 1e-5:
                break
            x_0 = x_t
            x_arr[b].append(x_t)

    draw_x = []
    draw_y = []

    for b in b_range:
        x = x_arr[b]
        for x_ in x:
            if x_ > 10:
                continue
            draw_x.append(b)
            draw_y.append(x_)


    # Доверительный над одним равновесием
    down_x1 = []
    down_y1 = []
    for b in b_range:
        if b < left1 or b > right1:
            continue

        x = x_arr[b]
        for x_ in x:
            if x_ > 10:
                continue
            down_x1.append(b)
            down_y1.append(x_ - 3 * epsilon * np.sqrt(m(a, b, x_)))

    # Доверительный под одним равновесием
    up_x1 = []
    up_y1 = []
    for b in b_range:
        if b < left1 or b > right1:
            continue

        x = x_arr[b]
        for x_ in x:
            if x_ > 10:
                continue
            up_x1.append(b)
            up_y1.append(x_ + 3 * epsilon * np.sqrt(m(a, b, x_)))


    # Доверительный под 2-циклом
    down_x2 = []
    down_y2 = []
    for b in b_range:
        if b < left2 or b > right1:
            continue

        x = x_arr[b]
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

    # Доверительный под 2-циклом
    up_x2 = []
    up_y2 = []
    for b in b_range:
        if b < left2 or b > right1:
            continue

        x = x_arr[b]
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
            down_y2.append(x0[i] + 3 * epsilon * np.sqrt(np.abs(m1(a, b, x0[i], x1[i]))))
            down_y2.append(x1[i] + 3 * epsilon * np.sqrt(np.abs(m2(a, b, x0[i], x1[i]))))

    return down_x1, down_y1, up_x1, up_y1, down_x2, down_y2, up_x2, up_y2
