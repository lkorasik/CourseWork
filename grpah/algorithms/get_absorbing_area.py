def get_absorbing_area(max_, f):
    c_1 = max_
    c = f(c_1)
    c1 = f(c)

    return [c_1, c, c1]
