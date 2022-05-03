def lyapunov(time_range, epsilon, b_range, x_start, T, f, lambda_):
    """
    Поиск показателей Ляпунова.

    time_range - итератор по времени. Должен начинаться с единицы
    epsilon - шаг по значения х.
    p_range - итератор по значениям параметра p
    x_start - начальное значение
    T -
    f - исследуемая функция
    lambda_ -
    """
    dxs = []
    bs = []

    for b in b_range:
        x0 = x_start
        summary = 0
        for _ in time_range:
            x0d = x0 + epsilon
            x0 = f(b, x0)
            x0d = f(b, x0d)
            summary += lambda_(abs(x0d - x0), epsilon)
        dxs.append(summary / T)
        bs.append(b)

    return bs, dxs
