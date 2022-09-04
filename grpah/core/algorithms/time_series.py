def time_series(time_range, x_start, f, skip):
    """
    Вычисление точек для построения графика временного ряда

    Вход:
        time_range - итератор по времени. Должен начинаться с единицы
        x_start - начальное значение
        f - реккурентная функция
        skip - следует ли сделать холостой прогон функции?

    Выход:
        [x, ...]
        [y, ...]
    """
    x = []

    x_i = x_start
    if skip:
        for _ in time_range:
            x_i = f(x_i)
    for _ in time_range:
        x_i = f(x_i)
        x.append(x_i)

    t = list(time_range)

    # Вставляем в результаты начальную точку
    x.insert(0, x_start)
    t.insert(0, 0)

    return t, x
