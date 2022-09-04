from visual.line import Line


def convert_line_to_dict(line: Line):
    """
    Конветировать два списка вида:
    [
        [x0, x1, x2, ...],
        [y0, y1, y2, ...]
    ]

    В словарь вида
    {
        x0: y0
        x1: y1
        x2: y2
        ...
    }
    """
    result = dict()
    for i in range(len(line.x)):
        result[line.x[i]] = line.y[i]
    return result
