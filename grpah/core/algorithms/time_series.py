from visual.line import Line


def time_series(time_range, x_start, f, skip):
    """
    Вычисление точек для построения графика временного ряда

    Вход:
        time_range - итератор по времени. Должен начинаться с единицы
        x_start - начальное значение
        f - реккурентная функция
        skip - следует ли сделать холостой прогон функции?

    Выход:
        Line - линия, набор точек
    """
    line = Line().add(0, x_start)

    x_i = x_start
    if skip:
        for _ in time_range:
            x_i = f(x_i)
    for t in time_range:
        x_i = f(x_i)
        line.add(t, x_i)

    return line
