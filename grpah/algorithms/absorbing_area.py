from algorithms.find_local_max import find_local_max
from algorithms.get_absorbing_area import get_absorbing_area


def absorbing_area(p_range, left, right, step, f):
    """
    Вычсиление точек для построения absorbing area на графике бифуркации

    p_range - итератор по значениям параметра p
    left - левая граница для поиска локального максимума
    right - правая граница для поиска локального максимума
    step - шаг для поиска локального максимума
    f - исследуемая функция

    return координаты по оси параметра, координаты первой линии по оси значений, координаты второй линии по оси
    значений
    """

    draw_x = []
    draw_y_up = []
    draw_y_down = []

    for p in p_range:
        max_ = find_local_max(left, right, step, lambda x: f(p, x))
        area_bounds = get_absorbing_area(max_, lambda x: f(p, x))

        draw_x.append(p)
        draw_y_up.append(area_bounds[1])
        draw_y_down.append(area_bounds[2])

    return draw_x, draw_y_up, draw_y_down
