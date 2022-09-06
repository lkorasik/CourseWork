from functions_pkg.functions_generator import generate_functions
from functions.symbols import a, b, x, eta

_f = (a * x ** 2) / ((b + x) ** 6) + eta

f, q, s, m, _q, _s = generate_functions(_f)
