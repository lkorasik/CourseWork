def time_series(skip_range, time_range, x_start, f, skip):
    """
    Вычисление точек для построения графика временного ряда

    Вход:
        time_range - итератор по времени. Должен начинаться с единицы
        x_start - начальное значение
        f - реккурентная функция
        skip - следует ли сделать холостой прогон функции?

    Выход:
        Набор точек
    """
    line = []

    x_i = x_start
    if skip:
        for _ in skip_range:
            x_i = f(x_i)
    for t in time_range:
        x_i = f(x_i)
        line.append([t, x_i])

    return line
