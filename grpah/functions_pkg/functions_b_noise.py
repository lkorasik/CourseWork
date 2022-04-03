import numpy
from sympy import Symbol

a = Symbol('\\alpha')
b = Symbol('\\beta')
x = Symbol('x')
eta = Symbol('\\eta')

_f_cb = (a * x ** 2) / ((b + x + eta) ** 6)

_q_cb = ((_f_cb.diff(x).subs(eta, 0)) ** 2).simplify()
_s_cb = ((_f_cb.diff(eta).subs(eta, 0)) ** 2).simplify()

_m_cb = (_s_cb / (1 - _q_cb)).simplify()


def f_chaos_b(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _f_cb.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def q_chaos_b(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _q_cb.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def s_chaos_b(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _s_cb.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def m_chaos_b(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m_cb.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)
