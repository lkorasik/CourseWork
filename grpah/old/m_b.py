import r as Alg


def m_b(b_range, a, left1, right1, left2, right2, m, m1, m2, values, s, q, s_, q_):
    draw_x = []
    draw_y = []

    for b in b_range:
        x = values[b]
        for x_ in x:
            draw_x.append(b)
            draw_y.append(x_)

    Alg.setup(q_, s_)

    # Доверительный над одним равновесием
    down_x1 = []
    down_y1 = []
    for b in b_range:
        if b < left1 or b > right1:
            continue

        x = values[b]
        for x_ in x:
            if x_ > 10:
                continue
            down_x1.append(b)
            down_y1.append(m(a, b, x_))


    # Доверительный под 2-циклом
    down_x2 = []
    down_y2 = []
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
            down_x2.append(b)
            down_x2.append(b)
            down_y2.append(m1(a, b, x0[i], x1[i]))
            down_y2.append(m2(a, b, x0[i], x1[i]))

    return down_x1, down_y1, down_x2, down_y2
