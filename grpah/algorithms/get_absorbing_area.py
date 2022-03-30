def get_absorbing_area(max_, d, f):
    # c_1 = max_
    c_1 = d
    c = f(c_1)
    c1 = f(c)

    return [c_1, c, c1]
