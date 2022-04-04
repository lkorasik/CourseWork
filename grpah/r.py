from sympy import Symbol, latex, SeqFormula, Function
from sympy.series.sequences import RecursiveSeq

a = Symbol('a')
x = Symbol('x')
b = Symbol('b')

q = (4 * (a ** 2) * (x ** 2) * ((b - 2 * x) ** 2)) / ((x + b) ** 14)
s = (36 * (a ** 2) * (x ** 4)) / ((x + b) ** 14)

count = 2
x_ = [Symbol(f'x{i}') for i in range(1, count + 1)]
q_ = [q.subs(x, x_[i]) for i in range(count)]
s_ = [s.subs(x, x_[i]) for i in range(count)]

r = Function('r')
t = Symbol('t')

q_.insert(0, 0)
s_.insert(0, 0)


def generator_r(t):
    rt = Symbol("rt")

    base = q * rt + s
    collect = rt
    for i in range(t, 0, -1):
        qi = Symbol(f"q{i - 1}")
        si = Symbol(f"s{i - 1}")

        if i == 1:
            collect = collect.subs(rt, 0)
        else:
            collect = collect.subs(rt, base)

        collect = collect.subs(q, qi).subs(s, si)

    return collect


if __name__ == "__main__":
    print(x_)
    print(q_)
    print(s_)

    print(generator_r(5))
