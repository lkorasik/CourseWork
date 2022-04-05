import numpy
from sympy import Symbol
from functions_pkg.symbols import a, b, x, eta

_f_c = (a * x ** 2) / ((b + x) ** 6) + eta

_q_c = ((_f_c.diff(x).subs(eta, 0)) ** 2).simplify()
_s_c = ((_f_c.diff(eta).subs(eta, 0)) ** 2).simplify()

_m_c = (_s_c / (1 - _q_c)).simplify()

x1 = Symbol('x1')
x2 = Symbol('x2')

_q1_c = _q_c.subs(x, x1).simplify()
_q2_c = _q_c.subs(x, x2).simplify()
_s1_c = _s_c.subs(x, x1).simplify()
_s2_c = _s_c.subs(x, x2).simplify()

_m1_c = (_q2_c * _s1_c + _s2_c) / (1 - _q1_c * _q2_c)
_m2_c = (_q1_c * _s2_c + _s1_c) / (1 - _q1_c * _q2_c)


def f_chaos(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _f_c.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def q_chaos(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _q_c.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def s_chaos(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _s_c.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def m_chaos(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m_c.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def m1_chaos_b(val_a, val_b, val_x1, val_x2, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m1_c.subs(a, val_a).subs(b, val_b).subs(x1, val_x1).subs(x2, val_x2).subs(eta, val_eta)
    return float(value)


def m2_chaos_b(val_a, val_b, val_x1, val_x2, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m2_c.subs(a, val_a).subs(b, val_b).subs(x1, val_x1).subs(x2, val_x2).subs(eta, val_eta)
    return float(value)
