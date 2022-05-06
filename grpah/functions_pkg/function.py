from sympy import lambdify
from functions_pkg.symbols import a, b, x

_f = (a * x ** 2) / ((b + x) ** 6)
f = lambdify([a, b, x], _f)

_f_dx = _f.diff(x).simplify()
f_dx = lambdify([a, b, x], _f_dx)
