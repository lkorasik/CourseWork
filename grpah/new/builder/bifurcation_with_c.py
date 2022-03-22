import extrema


def bifurcation_with_c(b_range, left, right, step, f, draw_x, draw_y):
    result = [[draw_x, draw_y]]

    draw_x = []
    draw_y1 = []
    draw_y2 = []
    for b in b_range:
        max_ = extrema.find_local_max(left, right, step, lambda x: f(b, x))
        area_bounds = extrema.get_absorbing_area(max_, lambda x: f(b, x))
        draw_x.append(b)
        draw_y1.append(area_bounds[1])
        draw_y2.append(area_bounds[2])

    result.append([draw_x, draw_y1])
    result.append([draw_x, draw_y2])

    return result
