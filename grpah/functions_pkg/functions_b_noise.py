import numpy
from sympy import Symbol
from functions_pkg.symbols import a, b, x, eta

_f_bn = (a * x ** 2) / ((b + x + eta) ** 6)

_q_bn = ((_f_bn.diff(x).subs(eta, 0)) ** 2).simplify()
_s_bn = ((_f_bn.diff(eta).subs(eta, 0)) ** 2).simplify()

_m_bn = (_s_bn / (1 - _q_bn)).simplify()


def f_chaos_b(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _f_bn.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def q_chaos_b(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _q_bn.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def s_chaos_b(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _s_bn.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def m_chaos_b(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m_bn.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)

