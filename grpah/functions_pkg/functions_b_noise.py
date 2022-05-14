from functions_pkg.functions_generator import generate_functions
from functions_pkg.symbols import a, b, x, eta

_f = (a * x ** 2) / ((b + x + eta) ** 6)

f, q, s, m = generate_functions(_f)

# import numpy
# from functions_pkg.symbols import a, b, x, eta
# from sympy.utilities.lambdify import lambdify
#
# _f = (a * x ** 2) / ((b + x + eta) ** 6)
#
# _q = ((_f.diff(x).subs(eta, 0)) ** 2).simplify()
# _s = ((_f.diff(eta).subs(eta, 0)) ** 2).simplify()
#
# _m = (_s / (1 - _q)).simplify()
#
# _lam_f = lambdify([a, b, x, eta], _f)
#
# _lam_q = lambdify([a, b, x, eta], _q)
# _lam_s = lambdify([a, b, x, eta], _s)
#
# _lam_m = lambdify([a, b, x, eta], _m)
#
#
# def f(val_a, val_b, val_x, val_epsilon):
#     val_eta = numpy.random.normal(0, 1) * val_epsilon
#     return float(_lam_f(val_a, val_b, val_x, val_eta))
#
#
# def q(val_a, val_b, val_x, val_epsilon):
#     val_eta = numpy.random.normal(0, 1) * val_epsilon
#     return float(_lam_q(val_a, val_b, val_x, val_eta))
#
#
# def s(val_a, val_b, val_x, val_epsilon):
#     val_eta = numpy.random.normal(0, 1) * val_epsilon
#     return float(_lam_s(val_a, val_b, val_x, val_eta))
#
#
# def m(val_a, val_b, val_x, val_epsilon):
#     val_eta = numpy.random.normal(0, 1) * val_epsilon
#     return float(_lam_m(val_a, val_b, val_x, val_eta))
