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


def job(input: Queue, output: Queue, n):
    while not input.empty():
        value = input.get()
        print(n, value)
        output.put(value)


if __name__ == "__main__":
    print(lam_f(3, 2))

    input = Queue()
    for i in range(1000):
        input.put(i)
    output = Queue()

    f1 = Process(target=job, args=(input, output, 1))
    f2 = Process(target=job, args=(input, output, 2))
    f1.start()
    f2.start()
    f1.join()
    f2.join()
