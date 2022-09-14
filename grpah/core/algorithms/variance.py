import statistics
from visual.line import Line


def variance(p_range, values):
    """
    Вычисление точек для построения графика дисперсии

    Вход:
        p_ranges - итератор по значениям параметра
        values - словарь параметр - значения из бифуркации

    Вывод:
        Линия, набор точек
    """
    line = Line()
    for p in p_range:
        variance_ = statistics.variance(values[p])
        line.add(p, variance_)

    return line
