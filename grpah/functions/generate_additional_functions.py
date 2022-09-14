from sympy.utilities.lambdify import lambdify

from functions.symbols import a, b, x, eta
from functions.wrap import wrap


def generate_additional_functions(_f):
    _q = ((_f.diff(x).subs(eta, 0)) ** 2).simplify()
    _s = ((_f.diff(eta).subs(eta, 0)) ** 2).simplify()

    _m = (_s / (1 - _q)).simplify()

    _lam_f = lambdify([a, b, x, eta], _f)

    _lam_q = lambdify([a, b, x, eta], _q)
    _lam_s = lambdify([a, b, x, eta], _s)

    _lam_m = lambdify([a, b, x, eta], _m)

    f = wrap(_lam_f)
    q = wrap(_lam_q)
    s = wrap(_lam_s)
    m = wrap(_lam_m)

    return f, q, s, m, _q, _s
