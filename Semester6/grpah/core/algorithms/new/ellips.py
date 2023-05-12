from math import sqrt, sin, cos

import numpy as np

from models.new_new_model import function


def run_eq():
    # x_eq = 0.420583
    x_eq = 0.420583
    # y_eq = 0.420583
    y_eq = 0.420583
    # σ = 0.022
    # σ = 0.0081
    α = 1.0
    β = 0.445
    σ = 0.02
    ε = 0.1

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

def run_c2():
    x = [0.588023, 0.250809]
    y = [0.250809, 0.588023]
    α = 1.0
    β = 0.445
    σ = 0.1
    ε = 0.1

    E = [[1, 0], [0, 1]]

    Q1 = E
    Q2 = E

    F1 = function.F(α, β, σ, x[0], y[0])
    F2 = function.F(α, β, σ, x[1], y[1])

    F1T = np.transpose(F1)
    F2T = np.transpose(F2)

    Q = np.add(Q2, np.dot(np.dot(F2, Q1), F2T))

    B = np.dot(F2, F1)
    BT = np.transpose(B)

    W1 = E
    for i in range(100):
        W1 = np.add(np.dot(np.dot(B, W1), BT), Q)
        # print(i, W1)

    W2 = np.add(np.dot(np.dot(F1, W1), F1T), Q1)

    W1 = np.array(W1, dtype=float)
    W2 = np.array(W2, dtype=float)

    eigen_values, eigen_vectors = np.linalg.eig(W1)

    λ1, λ2 = eigen_values
    v1 = [eigen_vectors[0][0], eigen_vectors[1][0]]
    v2 = [eigen_vectors[0][1], eigen_vectors[1][1]]

    P = 0.95
    q = sqrt(-np.log(1 - P))

    v11 = v1[0]
    v12 = v1[1]
    v21 = v2[0]
    v22 = v2[1]

    xx = []
    yy = []

    for ϕ in np.arange(0, 2 * np.pi, 0.01):
        z1 = ε * q * sqrt(2 * λ1) * cos(ϕ)
        z2 = ε * q * sqrt(2 * λ2) * sin(ϕ)
        xxx = x[0] + (z1 * v22 - z2 * v12) / (v11 * v22 - v12 * v21)
        yyy = y[0] + (z2 * v11 - z1 * v21) / (v11 * v22 - v12 * v21)
        xx.append(xxx)
        yy.append(yyy)

    file = open("C:\\users\\lkora\\desktop\\ellips1.txt", "w")
    for i in range(len(xx)):
        file.write(str(xx[i]) + " " + str(yy[i]) + "\n")
    file.close()

    eigen_values, eigen_vectors = np.linalg.eig(W2)

    λ1, λ2 = eigen_values
    v1 = [eigen_vectors[0][0], eigen_vectors[1][0]]
    v2 = [eigen_vectors[0][1], eigen_vectors[1][1]]

    P = 0.95
    q = sqrt(-np.log(1 - P))

    v11 = v1[0]
    v12 = v1[1]
    v21 = v2[0]
    v22 = v2[1]

    xx = []
    yy = []

    for ϕ in np.arange(0, 2 * np.pi, 0.01):
        z1 = ε * q * sqrt(2 * λ1) * cos(ϕ)
        z2 = ε * q * sqrt(2 * λ2) * sin(ϕ)
        xxx = x[1] + (z1 * v22 - z2 * v12) / (v11 * v22 - v12 * v21)
        yyy = y[1] + (z2 * v11 - z1 * v21) / (v11 * v22 - v12 * v21)
        xx.append(xxx)
        yy.append(yyy)

    file = open("C:\\users\\lkora\\desktop\\ellips2.txt", "w")
    for i in range(len(xx)):
        file.write(str(xx[i]) + " " + str(yy[i]) + "\n")
    file.close()
