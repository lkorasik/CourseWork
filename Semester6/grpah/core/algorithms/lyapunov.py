import math

from visual.line import Line


def lyapunov(time_range, epsilon, b_range, x_start, T, f):
    """
    Поиск показателей Ляпунова. Вычисляется алгоритмом Бенеттина

    Вход:
        time_range - итератор по времени. Должен начинаться с единицы
        epsilon - шаг по значения х.
        p_range - итератор по значениям параметра p
        x_start - начальное значение
        T - небольшой временной интервал
        f - исследуемая функция

    Выход:
        Линия - показатель ляпунова
    """
    line = Line()

    for b in b_range:
        x0 = x_start
        summary = 0
        for _ in range(1, T + 1):
            x0d = x0 + epsilon
            x0 = f(b, x0)
            x0d = f(b, x0d)

            dx = abs(x0d - x0)
            if dx == 0:
                summary += 0
            else:
                summary += math.log(dx / epsilon)
        line.add(b, summary / T)

    return line
