from sympy import Symbol, lambdify, diff

α = Symbol("\\alpha")
β = Symbol("\\beta")
γ = Symbol("\\gamma")
σ = Symbol("\\sigma")
x = Symbol("x")
y = Symbol("y")

_x = ((α * x ** 2) / ((β + x) ** 6)) + σ * (y - x)
_y = ((α * y ** 2) / ((β + y) ** 6)) - σ * (y - x)

__x = lambdify([α, β, σ, x, y], _x)
__y = lambdify([α, β, σ, x, y], _y)


def f(α, β, σ, x, y):
    nx = __x(α, β, σ, x, y)
    ny = __y(α, β, σ, x, y)
    return [nx, ny]


def F(a, b, s, xv, yv):
    a_ = diff(_x, x).subs(α, a).subs(β, b).subs(σ, s).subs(x, xv).subs(y, yv)
    b_ = diff(_x, y).subs(α, a).subs(β, b).subs(σ, s).subs(x, xv).subs(y, yv)
    c_ = diff(_y, x).subs(α, a).subs(β, b).subs(σ, s).subs(x, xv).subs(y, yv)
    d_ = diff(_y, y).subs(α, a).subs(β, b).subs(σ, s).subs(x, xv).subs(y, yv)
    return [[a_, b_], [c_, d_]]
