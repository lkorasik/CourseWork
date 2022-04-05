from sympy import lambdify
from functions_pkg.symbols import a, b, x

_f = (a * x ** 2) / ((b + x) ** 6)
f = lambdify([a, b, x], _f)


def f_subs(a_, b_, x_):
    return float(_f.subs(a, a_).subs(b, b_).subs(x, x_))
