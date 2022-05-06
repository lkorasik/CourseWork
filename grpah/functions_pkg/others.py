from sympy import lambdify
from functions_pkg.symbols import a, b, x

_g = a * x
g = lambdify([a, x], _g)

_h = x - (a * x ** 2) / ((b + x) ** 6)
h = lambdify([a, b, x], _h)

_h_dx = _h.diff(x).simplify()
h_dx = lambdify([a, b, x], _h_dx)
