def bifurcation(time_range, x_start, p_range, f, up_border, down_border):
    """
    Вычисление точек для построения графика бифуркации. Точки для графика x(p)

    time_range - итератор по времени. Должен начинаться с единицы
    x_start - начальное значение
    p_range - итератор по значениям параметра p
    f - исследуемая функция
    up_border - врехняя граница отсечения, если None то ничего не будет отсекаться
    down_border - нижняя граница отсечения, если None то ничего не будет отсекаться

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
            if up_border is not None and abs(x_t) > up_border:
                break
            if down_border is not None and abs(x_t) < down_border:
                break
            x_0 = x_t
        for _ in time_range:
            x_t = f(p, x_0)
            if up_border is not None and abs(x_t) > up_border:
                break
            if down_border is not None and abs(x_t) < down_border:
                break
            x_0 = x_t
            values[p].append(x_t)

    return values
