from models.hassel.generate_additional_functions import generate_additional_functions
from models.hassel.symbols import a, b, x, eta

_f = (a * x ** 2) / ((b + x) ** 6) + eta

f, q, s, m, _q, _s = generate_additional_functions(_f)
