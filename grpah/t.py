from sympy.abc import x
from sympy.utilities.lambdify import lambdify, implemented_function
from sympy import Function
import numpy

f = implemented_function(Function('f'), lambda x: x + numpy.random.normal(0, 1))
lam_f = lambdify(x, f(x))

if __name__ == "__main__":
    print(lam_f(3))
