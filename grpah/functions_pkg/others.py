from sympy import lambdify
from functions_pkg.symbols import a, x

_g = a * x
g = lambdify([a, x], _g)
