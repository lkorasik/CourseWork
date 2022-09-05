import numpy
from visual.line import Line


def mean(p_range, values):
    """
    Вычисление точек для построения графика матожидания

    Вход:
        p_ranges - итератор по значениям параметра
        values - словарь параметр - значения из бифуркации

    Вывод:
        Линия, набор точек
    """
    line = Line()
    for p in p_range:
        mean_ = numpy.mean(values[p])
        line.add(p, mean_)

    return line
