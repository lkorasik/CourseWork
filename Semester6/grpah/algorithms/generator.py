from sympy import Symbol

from models.hassel.symbols import a, b, x

# q и s можно взять из пакета hassel
q = (4 * (a ** 2) * (x ** 2) * ((b - 2 * x) ** 2)) / ((x + b) ** 14)
s = (36 * (a ** 2) * (x ** 4)) / ((x + b) ** 14)


def setup(q_, s_):
    global q
    global s
    q = q_
    s = s_


def generator_r(t):
    delta = Symbol("\\Delta")

    qq = Symbol("qq")
    ss = Symbol("ss")

    base = qq * delta + ss
    formula = delta
    for i in range(t, 0, -1):
        qi = Symbol(f"q{i - 1}")
        si = Symbol(f"s{i - 1}")

        if i == 1:
            formula = formula.subs(delta, 0)
        else:
            formula = formula.subs(delta, base)

        formula = formula.subs(qq, qi).subs(ss, si)

    return formula


def generator_Q(t):
    delta = Symbol("\\Delta")

    base = q * delta
    formula = delta
    for i in range(t + 1, 0, -1):
        qi = Symbol(f"q{i - 1}")

        if i == 1:
            formula = formula.subs(delta, 1)
        else:
            formula = formula.subs(delta, base)

        formula = formula.subs(q, qi)

    return formula


def generator_xi(t):
    return [Symbol(f'x{i}') for i in range(1, t + 1)]


def generator_qi(t, x_):
    return [q.subs(x, x_[i]) for i in range(t)]


def generator_si(t, x_):
    return [s.subs(x, x_[i]) for i in range(t)]


def generate_M_i(R, Q, t):
    delta = Symbol("\\Delta")

    qq = Symbol("qq")
    ss = Symbol("ss")

    base = qq * delta + ss
    formula = delta
    for i in range(t, 0, -1):
        qi = Symbol(f"q{i - 1}")
        si = Symbol(f"s{i - 1}")

        if i == 1:
            formula = formula.subs(delta, R / (1 - Q))
        else:
            formula = formula.subs(delta, base)

        formula = formula.subs(qq, qi).subs(ss, si)

    return formula


def generate_M(R, Q, t):
    result = []
    for i in range(1, t + 1):
        result.append(generate_M_i(R, Q, i))
    return result


def to_dict(prefix, f_):
    d = dict()
    for i in range(len(f_)):
        d[Symbol(f"{prefix}{i + 1}")] = f_[i]
    return d


def subs_dict(formula, subs_f):
    for k, v in subs_f.items():
        formula = formula.subs(k, v)
    return formula


def get_m(k):
    x_ = generator_xi(k)
    q_ = generator_qi(k, x_)
    s_ = generator_si(k, x_)

    q_ = to_dict("q", q_)
    s_ = to_dict("s", s_)

    r_ = generator_r(k + 1)

    Q_ = generator_Q(k)

    formulas = []
    for i in range(k):
        result = generate_M(r_, Q_, k)[i]
        result = subs_dict(result, q_)
        result = subs_dict(result, s_)
        formulas.append(result)

    return formulas
