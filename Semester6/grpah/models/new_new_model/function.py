from sympy import Symbol, lambdify

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
