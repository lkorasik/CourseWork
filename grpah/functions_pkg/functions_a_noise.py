import numpy
from functions_pkg.symbols import a, b, x, eta

_f_ca = ((a + eta) * (x ** 2)) / ((b + x) ** 6)

_q_ca = ((_f_ca.diff(x).subs(eta, 0)) ** 2).simplify()
_s_ca = ((_f_ca.diff(eta).subs(eta, 0)) ** 2).simplify()

_m_ca = (_s_ca / (1 - _q_ca)).simplify()


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
