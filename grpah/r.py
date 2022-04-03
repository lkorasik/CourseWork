from sympy import Symbol, latex, sequence, Function
from sympy.series.sequences import RecursiveSeq

a = Symbol('\\alpha')
b = Symbol('\\beta')
x = Symbol('x')
eta = Symbol('\\eta')

q = (4 * (a ** 2) * (x ** 2) * ((b - 2 * x) ** 2)) / ((b + x) ** 14)
s = (36 * (a ** 2) * (x ** 4)) / ((b + x) ** 14)

y = Function("y")
n = Symbol("n")
fib = RecursiveSeq(y(n - 1) + y(n - 2), y(n), n, [0, 1])

if __name__ == "__main__":
    print(latex(q))

    print(sequence(n ** 2, (n, 0, 5)))
    print(list(sequence(n ** 2, (n, 0, 5))))

    print(fib[:6])
