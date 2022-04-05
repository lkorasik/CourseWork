from sympy import Symbol

s_a = Symbol('\\alpha')
s_b = Symbol('\\beta')
s_x = Symbol('x')
s_eta = Symbol('\\eta')

_f = (s_a * s_x ** 2) / ((s_b + s_x) ** 6)


def f(a, b, x):
    return float(_f.subs(s_a, a).subs(s_b, b).subs(s_x, x))
