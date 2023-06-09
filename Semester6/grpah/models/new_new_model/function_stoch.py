from sympy import Symbol, lambdify, diff
import numpy

α = Symbol("\\alpha")
β1 = Symbol("\\beta_1")
β2 = Symbol("\\beta_2")
γ = Symbol("\\gamma")
σ = Symbol("\\sigma")
x = Symbol("x")
y = Symbol("y")
ε = Symbol("\\varepsilon")
ξ = Symbol("\\xi")
ξ1t = Symbol("\\xi_{1, t}")
ξ2t = Symbol("\\xi_{2, t}")
δ1 = Symbol("\\delta_1")
δ2 = Symbol("\\delta_2")

_x = ((α * x ** 2) / ((β1 + x) ** 6)) + σ * (y - x) + δ1 * ε * ξ * (y - x) + δ2 * ε * ξ1t
_y = ((α * y ** 2) / ((β2 + y) ** 6)) + σ * (x - y) + δ1 * ε * ξ * (x - y) + δ2 * ε * ξ2t

__x = lambdify([α, β1, σ, x, y, ε, δ1, δ2, ξ, ξ1t, ξ2t], _x)
__y = lambdify([α, β2, σ, x, y, ε, δ1, δ2, ξ, ξ1t, ξ2t], _y)

def f(α, β1, β2, σ, x, y, ε, δ1, δ2):
    ξ = numpy.random.normal(0, 1)
    ξ1t = numpy.random.normal(0, 1)
    ξ2t = numpy.random.normal(0, 1)
    nx = __x(α, β1, σ, x, y, ε, δ1, δ2, ξ, ξ1t, ξ2t)
    ny = __y(α, β2, σ, x, y, ε, δ1, δ2, ξ, ξ1t, ξ2t)
    return [nx, ny]

def F(a, b, s, xv, yv, epsilon, delta1, delta2, xi, xi1t, xi2t):
    a_ = (diff(_x, x)
          .subs(α, a).subs(β1, b).subs(σ, s)
          .subs(x, xv).subs(y, yv)
          .subs(ε, epsilon)
          .subs(δ1, delta1).subs(δ2, delta2)
          .subs(ξ, xi).subs(ξ1t, xi1t).subs(ξ2t, xi2t))
    b_ = (diff(_x, y)
          .subs(α, a).subs(β1, b).subs(σ, s)
          .subs(x, xv).subs(y, yv)
          .subs(ε, epsilon)
          .subs(δ1, delta1).subs(δ2, delta2)
          .subs(ξ, xi).subs(ξ1t, xi1t).subs(ξ2t, xi2t))
    c_ = (diff(_y, x)
          .subs(α, a).subs(β1, b).subs(σ, s)
          .subs(x, xv).subs(y, yv)
          .subs(ε, epsilon)
          .subs(δ1, delta1).subs(δ2, delta2)
          .subs(ξ, xi).subs(ξ1t, xi1t).subs(ξ2t, xi2t))
    d_ = (diff(_y, y)
          .subs(α, a).subs(β1, b).subs(σ, s)
          .subs(x, xv).subs(y, yv)
          .subs(ε, epsilon)
          .subs(δ1, delta1).subs(δ2, delta2)
          .subs(ξ, xi).subs(ξ1t, xi1t).subs(ξ2t, xi2t))
    return [[a_, b_], [c_, d_]]