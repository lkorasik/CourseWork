from sympy import Symbol, latex, SeqFormula, Function
from sympy.series.sequences import RecursiveSeq

a = Symbol('a')
x = Symbol('x')
b = Symbol('b')

q = (4 * (a ** 2) * (x ** 2) * ((b - 2 * x) ** 2)) / ((x + b) ** 14)
s = (36 * (a ** 2) * (x ** 4)) / ((x + b) ** 14)

# count = 2
# x_ = [Symbol(f'x{i}') for i in range(1, count + 1)]
# q_ = [q.subs(x, x_[i]) for i in range(count)]
# s_ = [s.subs(x, x_[i]) for i in range(count)]
#
# r = Function('r')
# t = Symbol('t')
#
# q_.insert(0, 0)
# s_.insert(0, 0)


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


if __name__ == "__main__":
    k = 2

    x_ = generator_xi(k)
    q_ = generator_qi(k, x_)
    s_ = generator_si(k, x_)

    print(x_)

    q_ = to_dict("q", q_)
    s_ = to_dict("s", s_)
    print(q_)
    print(s_)

    r_ = generator_r(k + 1)
    print(r_)

    Q_ = generator_Q(k)
    print(latex(Q_))

    print(generate_M(r_, Q_, k))

    for i in range(k):
        result = generate_M(r_, Q_, k)[i]
        result = subs_dict(result, q_)
        result = subs_dict(result, s_)
        print(result.simplify())

    # result = generate_M(r_, Q_, k)[0]
    # for k, v in q_.items():
    #     # qi = Symbol(f"q{i + 1}")
    #     result = result.subs(k, v)
    # print(result)
