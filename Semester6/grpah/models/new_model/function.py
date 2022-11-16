from sympy import Symbol, lambdify

α = Symbol("\\alpha")
β = Symbol("\\beta")
γ = Symbol("\\gamma")
x = Symbol("x")
y = Symbol("y")

_x = (α * x ** 2) / ((β + x) ** 6) - γ * x * y
_y = y + γ * y * (x - y)

__x = lambdify([α, β, γ, x, y], _x)
__y = lambdify([α, β, γ, x, y], _y)


def plain_x(α, β, γ, x, y):
    return (α * x ** 2) / ((β + x) ** 6) - γ * x * y


def plain_y(α, β, γ, x, y):
    return y + γ * y * (x - y)


def f(α, β, γ, x, y):
    nx = __x(α, β, γ, x, y)
    ny = __y(α, β, γ, x, y)
    return [nx, ny]
