def convert_dict_to_lists(data: dict):
    """
    Конветировать словарь вида
    {
        x0: [y01, y02, y03, ...]
        x1: [y11, y12, y13, ...]
        ...
    }

    В два списка вида
    [
        [x0,  x0,  x0,  ..., x1,  x1,  x1,  ...],
        [y01, y02, y03, ..., y11, y12, y13, ...]
    ]
    """
    draw_x = []
    draw_y = []

    for b in data.keys():
        x = data[b]
        for x_ in x:
            draw_x.append(b)
            draw_y.append(x_)

    return draw_x, draw_y
