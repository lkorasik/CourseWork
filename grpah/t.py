from multiprocessing import Process, Queue

import numpy
from sympy.abc import x, y
from sympy.utilities.lambdify import lambdify, implemented_function

f = implemented_function('f', lambda x_, y_: x_ * y_ + numpy.random.normal(0, 1))
lam_f = lambdify([x, y], f(x, y))


def g(x, y):
    return x + y


def h(x, y, result: Queue):
    result.put(lam_f(x, y))


if __name__ == "__main__":
    print(lam_f(3, 2))

    result = Queue()
    f = Process(target=h, args=(1, 2, result))
    f.start()
    f.join()

    print(result.get())
