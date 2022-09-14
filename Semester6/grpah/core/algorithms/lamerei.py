from visual.line import Line


def lamerei(x_start, time_range, skip, f):
    """
    Алгоритм построения лестницы ламерея

    Вход:
        time_range - итератор по времени. Должен начинаться с единицы
        x_start - начальное значение
        f - реккурентная функция
        skip - следует ли сделать холостой прогон функции?

    Выход:
        Список отрезков лестницы Ламерея
    """
    result = []

    x0 = x_start
    if skip:
        for _ in time_range:
            x0 = f(x0)
    for _ in time_range:
        x1 = f(x0)
        result.append(Line().add(x0, x0).add(x0, x1))
        result.append(Line().add(x0, x1).add(x1, x1))
        x0 = x1

    return result
