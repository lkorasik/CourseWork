def bifurcation(time_range, x_start, b_range, f):
    """
    Вычисление точек для построения графика бифуркации. График x(b)

    time_range - итератор по времени. Должен начинаться с единицы
    x_start - начальное значение
    b_range - итератор по значениям параметра b
    f - функция

    return [x, ...], [y, ...]
    """
    values = dict()

    for b in b_range:
        values[b] = []
        x_0 = x_start

        for _ in time_range:
            x_t = f(b, x_0)
            if abs(x_t) > 10000:
                break
            if abs(x_t) < 1e-5:
                break
            x_0 = x_t
        for _ in time_range:
            x_t = f(b, x_0)
            if abs(x_t) > 10000:
                break
            if abs(x_t) < 1e-5:
                break
            x_0 = x_t
            values[b].append(x_t)

    return values
