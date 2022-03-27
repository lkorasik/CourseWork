from sympy import *

x = Symbol('x')
y = Symbol('y')
f = 2*x + 2*y
g = diff(f, x)


if __name__ == "__main__":
    print(f.subs(x, 3).subs(y, 3))
    print(g.subs(x, 3).subs(y, 3))
    print(f)
