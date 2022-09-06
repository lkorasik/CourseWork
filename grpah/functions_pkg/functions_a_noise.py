from functions_pkg.functions_generator import generate_functions
from functions.symbols import a, b, x, eta

_f = ((a + eta) * (x ** 2)) / ((b + x) ** 6)

f, q, s, m, _q, _s = generate_functions(_f)
