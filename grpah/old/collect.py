# Возможно, это лишнее
from algorithms.convert_dict_to_lists import convert_dict_to_lists
from algorithms.line_to_dict import line_to_dict


def collect(fss, border):
    # border - fss
    result = dict()

    for x in border.x:
        result[x] = [0]

    fss_ = []
    for line_ in fss:
        fss_.append(line_to_dict(line_))
    fss = fss_

    border = line_to_dict(border)

    for line_ in fss:
        for x in line_.keys():
            y1 = line_[x]
            y2 = border[x]
            result[x] = [y1 - y2]

    return convert_dict_to_lists(result)
