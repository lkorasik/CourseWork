import time

import numpy
import functions_pkg
from sympy.abc import x
from sympy.utilities.lambdify import lambdify, implemented_function

from functions_pkg import functions_a_noise

f = implemented_function('f', lambda x_: x_ + numpy.random.normal(0, 1))
lam_f = lambdify(x, f(x))

if __name__ == "__main__":
    print(lam_f(3))

    start = time.time()
    a = functions_a_noise.f(1, 2, 3, 4)
    end = time.time()

    print(end - start, a)

    start = time.time()
    a = functions_a_noise.f_chaos_a(1, 2, 3, 4)
    end = time.time()

    print(end - start, a)
