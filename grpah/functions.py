import math
import numpy


def m(a, b, x):
    return (36 * (a ** 4) * (x ** 4)) / (((b + x) ** 14) * (1 - ((4 * (a ** 2) * ((b - 2 * x) ** 2) * (x ** 2)) / ((b + x) ** 14))))


def q(a, b, x):
    return (4 * (a ** 2) * (x ** 2) * ((b - 2 * x) ** 2)) / ((b + x) ** 14)


def s(a, b, x):
    return (36 * (a ** 14) * (x ** 4)) / ((b + x) ** 14)


def m1(a, b, x1, x2):
    return (q(a, b, x2) * s(a, b, x1) + s(a, b, x2)) / (1 - q(a, b, x1) * q(a, b, x2))


def m2(a, b, x1, x2):
    return (q(a, b, x1) * s(a, b, x2) + s(a, b, x1)) / (1 - q(a, b, x1) * q(a, b, x2))


def f(a, b, x):
    return (a * x ** 2) / ((b + x) ** 6)


class Functions:
    @staticmethod
    def f_pb(a, b, x, epsilon):
        xi = numpy.random.normal(0, 1)
        return (a * x ** 2) / ((b + (epsilon * xi) + x) ** 6)

    @staticmethod
    def f_pa(a, b, x, epsilon):
        xi = numpy.random.normal(0, 1)
        return ((a + (epsilon * xi)) * x ** 2) / ((b + x) ** 6)

    @staticmethod
    def f_p(a, b, x, epsilon):
        xi = numpy.random.normal(0, 1)
        return (a * x ** 2) / ((b + x) ** 6) + (epsilon * xi)

    @staticmethod
    def lambda_(dx, epsilon):
        if dx == 0:
            print('dx=0')
            return 0
        return math.log(dx / epsilon)

    @staticmethod
    def df(a, b, x):
        return (2 * a * x * (b - 2 * x)) / ((b + x) ** 7)

    @staticmethod
    def sf(a, b, x, shift):
        """Сдвиг функции f"""
        return (a * x ** 2) / ((b + x) ** 6) - shift

    @staticmethod
    def dsf(a, b, x):
        """Производная сдвига функции f"""
        return (2 * x * (b - 2 * x)) / ((b + x) ** 7)

    @staticmethod
    def g(a, x):
        return a * x

    @staticmethod
    def h(a, b, x):
        return x - (a * x ** 2) / ((b + x) ** 6)

    @staticmethod
    def dh(a, b, x):
        return (2 * a * x * (2 * x - b)) / ((b + x) ** 7) + 1
