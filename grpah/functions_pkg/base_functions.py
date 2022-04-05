from sympy import Symbol, lambdify

a = Symbol('\\alpha')
b = Symbol('\\beta')
x = Symbol('x')

_f = (a * x ** 2) / ((b + x) ** 6)


def f_subs(a_, b_, x_):
    return float(_f.subs(a, a_).subs(b, b_).subs(x, x_))


f = lambdify([a, b, x], _f)
