from core.utils.new_is_out_of_bounds import new_is_out_of_bounds


def time_series(skip_range, time_range, x_start, f, check_bounds, upper_bounds, lower_bounds):
    """
    Вычисление точек для построения графика временного ряда

    Вход:
        skip_range - итератор по времени для холостого прогона
        time_range - итератор по времени
        x_start - начальный вектор
        f - реккурентная функция. Принимает на вход вектор значений
        skip - следует ли сделать холостой прогон функции?

    Выход:
        Набор точек
    """
    line = [[0, x_start]]

    x_i = x_start
    for _ in skip_range:
        x_t = f(x_i)
        if check_bounds and new_is_out_of_bounds(x_t, upper_bounds, lower_bounds):
            break
        x_i = x_t
    for t in time_range:
        x_t = f(x_i)
        if check_bounds and new_is_out_of_bounds(x_t, upper_bounds, lower_bounds):
            break
        x_i = x_t
        line.append([t, x_i])

    return line
