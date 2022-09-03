import time


def time_series(time_range, x_start, f, skip):
    """
    Вычисление точек для построения графика временного ряда. График t(x).

    time_range - итератор по времени. Должен начинаться с единицы
    x_start - начальное значение
    f - функция
    skip - следует ли сделать холостой прогон функции?

    return [x, ...], [y, ...]
    """
    x = []

    x_0 = x_start
    if skip:
        for _ in time_range:
            x_0 = f(x_0)
    for _ in time_range:
        x_0 = f(x_0)
        x.append(x_0)

    t = list(time_range)

    # Вставляем в результаты начальную точку
    x.insert(0, x_start)
    t.insert(0, 0)

    return t, x
