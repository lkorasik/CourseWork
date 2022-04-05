from collections import Counter

import functions
from old.single_newton_iteration import single_newton_iteration


def find_all_roots(x_range, a_range, b_range, precision):
    result = dict()
    for a in a_range:
        result[a] = dict()
        for b in b_range:
            result[a][b] = []

    for a in a_range:
        print(a)
        for b in b_range:
            for x in x_range:
                res = single_newton_iteration(
                    a=a,
                    b=b,
                    x_start=x,
                    precision=precision,
                    function=functions.h,
                    dfunction=functions.dh)
                result[a][b].append(res)

    for a in a_range:
        for b in b_range:
            for i in range(len(result[a][b])):
                result[a][b][i] = round(result[a][b][i], 3)

    for a in a_range:
        for b in b_range:
            print(Counter(result[a][b]))
