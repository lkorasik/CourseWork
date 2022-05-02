import numpy
from functions_pkg.symbols import a, b, x, eta
from sympy.utilities.lambdify import lambdify

_f = ((a + eta) * (x ** 2)) / ((b + x) ** 6)

_q = ((_f.diff(x).subs(eta, 0)) ** 2).simplify()
_s = ((_f.diff(eta).subs(eta, 0)) ** 2).simplify()

_m = (_s / (1 - _q)).simplify()

_lam_f = lambdify([a, b, x, eta], _f)

_lam_q = lambdify([a, b, x, eta], _q)
_lam_s = lambdify([a, b, x, eta], _s)

_lam_m = lambdify([a, b, x, eta], _m)


def f(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    return float(_lam_f(val_a, val_b, val_x, val_eta))


def q(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    return float(_lam_q(val_a, val_b, val_x, val_eta))


def s(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    return float(_lam_s(val_a, val_b, val_x, val_eta))


def m(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    return float(_lam_m(val_a, val_b, val_x, val_eta))


def f_chaos_a(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _f.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def q_chaos_a(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _q.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def s_chaos_a(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _s.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)


def m_chaos_a(val_a, val_b, val_x, val_epsilon):
    val_eta = numpy.random.normal(0, 1) * val_epsilon
    value = _m.subs(a, val_a).subs(b, val_b).subs(x, val_x).subs(eta, val_eta)
    return float(value)
