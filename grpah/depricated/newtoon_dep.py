"""
Have new realization
"""
#b = 0.582355932
b = 0.563

prec = 0.000001


def g(x):
    return x - (x ** 2) / ((b + x) ** 6)


def gs(x):
    return 2 * x * (2 * x - b) / ((b + x) ** 7) + 1


def h(x, shift):
    return (x ** 2) / ((b + x) ** 6) - shift


def hs(x):
    return 2 * x * (b - 2 * x) / ((b + x) ** 7)


x_0 = 0.08
for i in range(0, 100):
    x_n = x_0 - g(x_0) / gs(x_0)
    if abs(x_n - x_0) < prec:
        break
    x_0 = x_n
res = x_0
print(res)


x_0 = 0.45
for i in range(0, 100):
    x_n = x_0 - h(x_0, res) / hs(x_0)
    if abs(x_n - x_0) < prec:
        break
    x_0 = x_n
print(x_0)

