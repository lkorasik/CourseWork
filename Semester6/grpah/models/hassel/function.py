from sympy import lambdify
from models.hassel.symbols import a, b, x

_f = (a * x ** 2) / ((b + x) ** 6)
f = lambdify([a, b, x], _f)

_f_dx = _f.diff(x).simplify()
f_dx = lambdify([a, b, x], _f_dx)

_g = a * x
g = lambdify([a, x], _g)

_h = x - (a * x ** 2) / ((b + x) ** 6)
h = lambdify([a, b, x], _h)

_h_dx = _h.diff(x).simplify()
h_dx = lambdify([a, b, x], _h_dx)