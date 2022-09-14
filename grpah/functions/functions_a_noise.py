from functions.generate_additional_functions import generate_additional_functions
from functions.symbols import a, b, x, eta

_f = ((a + eta) * (x ** 2)) / ((b + x) ** 6)

f, q, s, m, _q, _s = generate_additional_functions(_f)
