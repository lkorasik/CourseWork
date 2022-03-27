def bifurcation(time_range, x_start, p_range, f):
    """
    Вычисление точек для построения графика бифуркации. Точки для графика x(p)

    time_range - итератор по времени. Должен начинаться с единицы
    x_start - начальное значение
    b_range - итератор по значениям параметра p
    f - исследуемая функция

    return dict

    Ключ - значение параметра p
    Значение - список соответствующих значений функции
    """
    values = dict()

    for p in p_range:
        values[p] = []
        x_0 = x_start

        for _ in time_range:
            x_t = f(p, x_0)
            if abs(x_t) > 10000:
                break
            if abs(x_t) < 1e-5:
                break
            x_0 = x_t
        for _ in time_range:
            x_t = f(p, x_0)
            if abs(x_t) > 10000:
                break
            if abs(x_t) < 1e-5:
                break
            x_0 = x_t
            values[p].append(x_t)

    return values
