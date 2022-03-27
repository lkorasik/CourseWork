from new.algorithms.find_local_max import find_local_max
from new.algorithms.get_absorbing_area import get_absorbing_area


def bifurcation_with_absorbing_area(b_range, left, right, step, f, draw_x, draw_y):
    result = [[draw_x, draw_y]]

    draw_x = []
    draw_y1 = []
    draw_y2 = []
    for b in b_range:
        max_ = find_local_max(left, right, step, lambda x: f(b, x))
        area_bounds = get_absorbing_area(max_, lambda x: f(b, x))
        draw_x.append(b)
        draw_y1.append(area_bounds[1])
        draw_y2.append(area_bounds[2])

    result.append([draw_x, draw_y1])
    result.append([draw_x, draw_y2])

    return result
