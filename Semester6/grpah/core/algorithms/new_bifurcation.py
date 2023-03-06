from core.algorithms.time_series import time_series
from core.utils.is_out_of_bounds import is_out_of_bounds


def new_bifurcation(time_range, x_start, p_range, f, upper_bound=[10_000], lower_bound=[1e-5]):
    """
    Вычисление точек для построения графика бифуркации

    Вход:
        time_range - итератор по времени. Должен начинаться с единицы
        x_start - начальное значение
        p_range - итератор по значениям параметра
        f - исследуемая реккурентная функция
        upper_bound - врехняя граница отсечения, если None то ничего не будет отсекаться
        lower_bound - нижняя граница отсечения, если None то ничего не будет отсекаться

    Выход:
        {
            p0: [x00, x01, x02, ...]
            p1: [x10, x11, x12, ...]
            ...
        }

        Ключ - значения параметра
        Значение - список соответствующих значений функции
    """
    values = dict()

    for p in p_range:
        values[p] = []

        result = time_series(
            skip_range=time_range,
            time_range=time_range,
            x_start=x_start,
            f=lambda x: f(p, x),
            check_bounds=True,
            upper_bounds=upper_bound,
            lower_bounds=lower_bound
        )

        # x_0 = x_start
        # for _ in time_range:
        #     x_t = f(p, x_0)
        #     if is_out_of_bounds(x_t, upper_bound, lower_bound):
        #         break
        #     x_0 = x_t
        # for _ in time_range:
        #     x_t = f(p, x_0)
        #     if is_out_of_bounds(x_t, upper_bound, lower_bound):
        #         break
        #     x_0 = x_t
        #     values[p].append(x_t)

        result = list(map(lambda x: x[1], result))

        values[p] = result

    return values
