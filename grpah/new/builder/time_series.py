def time_series(time_range, x_start, f, skip):
    """
    Вычисление точек для построения графика временного ряда. График t(x)

    time_range - итератор по времени. Должен начинаться с единицы
    x_start - начальное значение
    f - функция
    skip - следует ли сделать холостой прогон функции?

    return [x, ...], [y, ...]
    """
    results = [] # Значения по вертикальной оси x

    x_0 = x_start
    if skip:
        for _ in time_range:
            x_0 = f(x_0)
    for _ in time_range:
        x_0 = f(x_0)
        results.append(x_0)

    time_range = list(time_range)

    # Вставляем в результаты начальную точку
    results.insert(0, x_start)
    time_range.insert(0, 0)

    return time_range, results
