def convert_dict_to_lists(data: dict):
    draw_x = []
    draw_y = []

    for b in data.keys():
        x = data[b]
        for x_ in x:
            draw_x.append(b)
            draw_y.append(x_)

    return draw_x, draw_y
