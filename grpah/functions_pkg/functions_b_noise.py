import numpy
from sympy import Symbol
from functions_pkg.symbols import a, b, x, eta

_f_bn = (a * x ** 2) / ((b + x + eta) ** 6)

_q_bn = ((_f_bn.diff(x).subs(eta, 0)) ** 2).simplify()
_s_bn = ((_f_bn.diff(eta).subs(eta, 0)) ** 2).simplify()

_m_bn = (_s_bn / (1 - _q_bn)).simplify()

x1 = Symbol('x1')
x2 = Symbol('x2')

_q1_bn = _q_bn.subs(x, x1).simplify()
_q2_bn = _q_bn.subs(x, x2).simplify()
_s1_bn = _s_bn.subs(x, x1).simplify()
_s2_bn = _s_bn.subs(x, x2).simplify()

_m1_bn = (_q2_bn * _s1_bn + _s2_bn) / (1 - _q1_bn * _q2_bn)
_m2_bn = (_q1_bn * _s2_bn + _s1_bn) / (1 - _q1_bn * _q2_bn)


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


def m1_chaos_b(val_a, val_b, val_x1, val_x2, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m1_bn.subs(a, val_a).subs(b, val_b).subs(x1, val_x1).subs(x2, val_x2).subs(eta, val_eta)
    return float(value)


def m2_chaos_b(val_a, val_b, val_x1, val_x2, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m2_bn.subs(a, val_a).subs(b, val_b).subs(x1, val_x1).subs(x2, val_x2).subs(eta, val_eta)
    return float(value)
