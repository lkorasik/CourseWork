import numpy
from sympy import Symbol

a = Symbol('\\alpha')
b = Symbol('\\beta')
x = Symbol('x')
eta = Symbol('\\eta')

_f = (a * x ** 2) / ((b + x) ** 6)


def f(val_a, val_b, val_x):
    return float(_f.subs(a, val_a).subs(b, val_b).subs(x, val_x))
