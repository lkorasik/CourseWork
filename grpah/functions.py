import math


class Functions:
    @staticmethod
    def f(a, b, x):
        return (a * x ** 2) / ((b + x) ** 6)

    @staticmethod
    def df(a, b, x):
        return (2 * a * x * (b - 2 * x))/((b + x) ** 7)

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
        return (2 * a * x * (2 * x - b))/((b + x) ** 7) + 1

    @staticmethod
    def lambda_(dx, T, epsilon):
        if dx == 0:
            return None
        return math.log(dx / epsilon) / T
