from visual.line import Line


def line_to_dict(line: Line):
    result = dict()

    for i in range(len(line.x)):
        result[line.x[i]] = line.y[i]

    return result
