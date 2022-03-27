import math


def q(a, b, x):
    return (4 * (a ** 2) * (x ** 2) * ((b - 2 * x) ** 2)) / ((b + x) ** 14)


def s(a, b, x):
    return (36 * (a ** 2) * (x ** 4)) / ((b + x) ** 14)


def r(a, b, x, t):
    if t == 0:
        return 0
    else:
        return q(a, b, x[t-1]) * r(a, b, x, t-1) + s(a, b, x[t-1])


def rq(a, b, x, k):
    result = 1
    for i in range(1, k + 1):
        result *= q(a, b, x[i])
    return result


def m(a, b, x, t):
    if t == 1:
        return r(a, b, x, t + 1) / (1 - rq(a, b, x, t))
    else:
        return q(a, b, x[t-1]) * m(a, b, x, t-1) + s(a, b, x[t-1])


if __name__ == "__main__":
    print(0.102255 + 0.01 * math.sqrt(m(1, 0.37, [0.102255, 0.168519, 0.953025, 1.16013], 1)))
    print(0.168519 + 0.01 * math.sqrt(m(1, 0.37, [0.102255, 0.168519, 0.953025, 1.16013], 1)))
    print(0.953025 + 0.01 * math.sqrt(m(1, 0.37, [0.102255, 0.168519, 0.953025, 1.16013], 1)))
    print(1.16013 + 0.01 * math.sqrt(m(1, 0.37, [0.102255, 0.168519, 0.953025, 1.16013], 1)))
