import math
import numpy

# Use function_pkg.function
# def f(a, b, x):
#     return (a * x ** 2) / ((b + x) ** 6)


# def m(a, b, x):
#     return (36 * (a ** 2) * (x ** 4)) / (((b + x) ** 14) * (1 - ((4 * (a ** 2) * ((b - 2 * x) ** 2) * (x ** 2)) / ((b + x) ** 14))))


# def q(a, b, x):
#     return (4 * (a ** 2) * (x ** 2) * ((b - 2 * x) ** 2)) / ((b + x) ** 14)


# def s(a, b, x):
#     return (36 * (a ** 2) * (x ** 4)) / ((b + x) ** 14)


# def m1(a, b, x1, x2):
#     return (q(a, b, x2) * s(a, b, x1) + s(a, b, x2)) / (1 - q(a, b, x1) * q(a, b, x2))


# def m2(a, b, x1, x2):
#     return (q(a, b, x1) * s(a, b, x2) + s(a, b, x1)) / (1 - q(a, b, x1) * q(a, b, x2))


def lambda_(dx, epsilon):
    if dx == 0:
        return 0
    return math.log(dx / epsilon)


# def g(a, x):
#     return a * x


def sf(a, b, x, shift):
    """Сдвиг функции f"""
    return (a * x ** 2) / ((b + x) ** 6) - shift


def h(a, b, x):
    return x - (a * x ** 2) / ((b + x) ** 6)


def dh(a, b, x):
    return (2 * a * x * (2 * x - b)) / ((b + x) ** 7) + 1


def f_pb(a, b, x, epsilon):
    xi = numpy.random.normal(0, 1)
    return (a * x ** 2) / ((b + (epsilon * xi) + x) ** 6)


def f_pa(a, b, x, epsilon):
    xi = numpy.random.normal(0, 1)
    return ((a + (epsilon * xi)) * x ** 2) / ((b + x) ** 6)


def f_p(a, b, x, epsilon):
    xi = numpy.random.normal(0, 1)
    return (a * x ** 2) / ((b + x) ** 6) + (epsilon * xi)


def df(a, b, x):
    return (2 * a * x * (b - 2 * x)) / ((b + x) ** 7)


def dfx2(a, b, x):
    return (16 * (a ** 6) * (x ** 6) * (((b ** 6) + ((a * (x ** 3) * (-5 * b + 4 * x)) / ((b + x) ** 7)) + b * x * (
                -2 + ((a * x * (-2 * b + 7 * x)) / ((b + x) ** 7)))) ** 2)) / (
                       ((b + x) ** 26) + ((b + ((a * x ** 2) / ((b + x) ** 6))) ** 14))
