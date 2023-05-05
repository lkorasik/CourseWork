from math import sqrt, sin, cos

import numpy as np

from models.new_new_model import function


def run0():
    # x_eq = 0.420583
    x_eq = 0.420583
    # y_eq = 0.420583
    y_eq = 0.420583
    # σ = 0.022
    # σ = 0.0081
    σ = 0.0366
    α = 1.0
    β = 0.445

    F = function.F(α, β, σ, x_eq, y_eq)
    FT = np.transpose(F)

    W0 = [[1, 0], [0, 1]]

    Q = [[1, 0], [0, 1]]

    # Ограничние по итерациям: элементы матрицы i отличаются от элементов матрицы i+1 отличается в пятом знаке
    Wi = W0
    print(Wi)
    for i in range(100):
        Wi = np.add(np.dot(np.dot(F, Wi), FT), Q)
        print(i, Wi)

    Wi = np.array(Wi, dtype=float)

    print(Wi)

    eigen_values, eigen_vectors = np.linalg.eig(Wi)

    λ1, λ2 = eigen_values
    v1 = [eigen_vectors[0][0], eigen_vectors[1][0]]
    v2 = [eigen_vectors[0][1], eigen_vectors[1][1]]

    print(v1)
    print(v2)

    print(λ1)
    print(λ2)

    P = 0.95
    q = sqrt(-np.log(1 - P))
    ε = 0.01

    v11 = v1[0]
    v12 = v1[1]
    v21 = v2[0]
    v22 = v2[1]

    xx = []
    yy = []

    for ϕ in np.arange(0, 2*np.pi, 0.01):
        z1 = ε * q * sqrt(2 * λ1) * cos(ϕ)
        z2 = ε * q * sqrt(2 * λ2) * sin(ϕ)
        x = x_eq + (z1 * v22 - z2 * v12) / (v11 * v22 - v12 * v21)
        y = y_eq + (z2 * v11 - z1 * v21) / (v11 * v22 - v12 * v21)
        xx.append(x)
        yy.append(y)

    file = open("C:\\users\\lkora\\desktop\\ellips.txt", "w")
    for i in range(len(xx)):
        file.write(str(xx[i]) + " " + str(yy[i]) + "\n")
    file.close()
