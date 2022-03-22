def time_series(time_range, x_start, f, skip):
    """
    Вычисление точек для построения графика временного ряда. График t(x)

    time_range - итератор по времени. Должен начинаться с единицы
    x_start - начальное значение
    f - функция
    skip - следует ли сделать холостой прогон функции?

    return [x, ...], [y, ...]
    """
    draw_ord = []

    x_0 = x_start
    if skip:
        for _ in time_range:
            x_0 = f(x_0)
    for _ in time_range:
        x_0 = f(x_0)
        draw_ord.append(x_0)

    draw_abs = list(time_range)

    # Вставляем в результаты начальную точку
    draw_ord.insert(0, x_start)
    draw_abs.insert(0, 0)

    return draw_abs, draw_ord
