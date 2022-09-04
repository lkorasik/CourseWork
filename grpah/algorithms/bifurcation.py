from core.utils.is_out_of_bounds import is_out_of_bounds


def bifurcation(time_range, x_start, p_range, f, up_border=10_000, down_border=1e-5):
    """
    Вычисление точек для построения графика бифуркации.

    time_range - итератор по времени. Должен начинаться с единицы
    x_start - начальное значение
    p_range - итератор по значениям параметра
    f - исследуемая функция
    up_border - врехняя граница отсечения, если None то ничего не будет отсекаться
    down_border - нижняя граница отсечения, если None то ничего не будет отсекаться

    return dict

    Ключ - значения параметра
    Значение - список соответствующих значений функции
    """
    values = dict()

    for p in p_range:
        values[p] = []

        x_0 = x_start
        for _ in time_range:
            x_t = f(p, x_0)
            if is_out_of_bounds(x_t, up_border, down_border):
                break
            x_0 = x_t
        for _ in time_range:
            x_t = f(p, x_0)
            if is_out_of_bounds(x_t, up_border, down_border):
                break
            x_0 = x_t
            values[p].append(x_t)

    return values
