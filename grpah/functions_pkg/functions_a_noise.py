import numpy
from sympy import Symbol, latex

a = Symbol('\\alpha')
b = Symbol('\\beta')
x = Symbol('x')
eta = Symbol('\\eta')

_f_ca = ((a + eta) * (x ** 2)) / ((b + x) ** 6)

_q_ca = ((_f_ca.diff(x).subs(eta, 0)) ** 2).simplify()
_s_ca = ((_f_ca.diff(eta).subs(eta, 0)) ** 2).simplify()

_m_ca = (_s_ca / (1 - _q_ca)).simplify()

x1 = Symbol('x1')
x2 = Symbol('x2')

_q1_ca = _q_ca.subs(x, x1).simplify()
_q2_ca = _q_ca.subs(x, x2).simplify()
_s1_ca = _s_ca.subs(x, x1).simplify()
_s2_ca = _s_ca.subs(x, x2).simplify()

_m1_ca = (_q2_ca * _s1_ca + _s2_ca) / (1 - _q1_ca * _q2_ca)
_m2_ca = (_q1_ca * _s2_ca + _s1_ca) / (1 - _q1_ca * _q2_ca)


def f_chaos_a(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _f_ca.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def q_chaos_a(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _q_ca.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def s_chaos_a(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _s_ca.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def m_chaos_a(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m_ca.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def m1_chaos_a(val_a, val_b, val_x1, val_x2, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m1_ca.subs(a, val_a).subs(b, val_b).subs(x1, val_x1).subs(x2, val_x2).subs(eta, val_eta)
    return float(value)


def m2_chaos_a(val_a, val_b, val_x1, val_x2, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m2_ca.subs(a, val_a).subs(b, val_b).subs(x1, val_x1).subs(x2, val_x2).subs(eta, val_eta)
    return float(value)
