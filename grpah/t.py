import numpy
from sympy.abc import x
from sympy.utilities.lambdify import lambdify, implemented_function

f = implemented_function('f', lambda x_: x_ + numpy.random.normal(0, 1))
lam_f = lambdify(x, f(x))

if __name__ == "__main__":
    print(lam_f(3))
