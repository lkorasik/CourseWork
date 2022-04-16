from visual.line import Line


def convert_dict_to_lists(data: dict):
    draw_x = []
    draw_y = []

    for b in data.keys():
        x = data[b]
        for x_ in x:
            draw_x.append(b)
            draw_y.append(x_)

    return draw_x, draw_y


def line_to_dict(line: Line):
    result = dict()

    for i in range(len(line.x)):
        result[line.x[i]] = line.y[i]

    return result
