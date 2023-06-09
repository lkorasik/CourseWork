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
    # ε = 0.057877868652343754
    ε = 0.04

    F = function.F(α, β, σ, x_eq, y_eq)
    FT = np.transpose(F)

    W0 = [[1, 0], [0, 1]]

    E = [[1, 0], [0, 1]]
    Q = E

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

def run_eq_search():
    # x_eq = 0.420583
    x_eq = 0.420583
    # y_eq = 0.420583
    y_eq = 0.420583
    # σ = 0.022
    # σ = 0.0081
    α = 1.0
    β = 0.445
    σ = 0.02
    ε_left = 0.001
    ε_right = 0.1

    while abs(ε_left - ε_right) > 0.00001:
        ε = (ε_left + ε_right) / 2

        F = function.F(α, β, σ, x_eq, y_eq)
        FT = np.transpose(F)

        W0 = [[1, 0], [0, 1]]

        E = [[1, 0], [0, 1]]
        Q = E

        # Ограничние по итерациям: элементы матрицы i отличаются от элементов матрицы i+1 отличается в пятом знаке
        Wi = W0
        # print(Wi)
        for i in range(100):
            Wi = np.add(np.dot(np.dot(F, Wi), FT), Q)
            # print(i, Wi)

        Wi = np.array(Wi, dtype=float)

        # print(Wi)

        eigen_values, eigen_vectors = np.linalg.eig(Wi)

        λ1, λ2 = eigen_values
        v1 = [eigen_vectors[0][0], eigen_vectors[1][0]]
        v2 = [eigen_vectors[0][1], eigen_vectors[1][1]]

        # print(v1)
        # print(v2)

        # print(λ1)
        # print(λ2)

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

        min_x = min(xx)
        min_y = min(yy)

        if min_x <= 0 or min_y <= 0:
            ε_right = ε
        else:
            ε_left = ε

        print('ε = ', ε)

def run_c2():
    # можно тут добавить прогон а потом взять два последних элемента

    # x = [0.588023, 0.250809]
    # x = [0.85604, 0.158732]
    x = [0.179239, 0.857367]
    # x = [0.854848, 0.187168]
    # y = [0.250809, 0.588023]
    # y = [0.158732, 0.85604]
    y = [0.179239, 0.857367]
    # y = [0.854848, 0.187168]
    α = 1.0
    β = 0.4
    σ = 0.01
    ε = 0.045

    E = [[1, 0], [0, 1]]

    # additive
    Q1 = E
    Q2 = E
    # parametric
    # Q1 = [[(y[0] - x[0]) ** 2, -(y[0] - x[0]) ** 2], [-(y[0] - x[0]) ** 2, (y[0] - x[0]) ** 2]]
    # Q2 = [[(y[1] - x[1]) ** 2, -(y[1] - x[1]) ** 2], [-(y[1] - x[1]) ** 2, (y[1] - x[1]) ** 2]]

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


def run_c2_search():
    x = [0.588023, 0.250809]
    y = [0.250809, 0.588023]
    α = 1.0
    β = 0.445
    σ = 0.1
    ε_left = 0.1
    ε_right = 0.2

    while abs(ε_left - ε_right) > 0.0000001:
        ε = (ε_left + ε_right) / 2

        E = [[1, 0], [0, 1]]

        # Q1 = E
        # Q2 = E

        Q1 = [[(y[0] - x[0]) ** 2, -(y[0] - x[0]) ** 2], [-(y[0] - x[0]) ** 2, (y[0] - x[0]) ** 2]]
        Q2 = [[(y[1] - x[1]) ** 2, -(y[1] - x[1]) ** 2], [-(y[1] - x[1]) ** 2, (y[1] - x[1]) ** 2]]

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


        min_x = min(xx)
        min_y = min(yy)

        if min_x <= 0 or min_y <= 0:
            ε_right = ε
        else:
            ε_left = ε

        print('ε = ', ε)

def run_c2_linear_search():
    x = [0.588023, 0.250809]
    y = [0.250809, 0.588023]
    α = 1.0
    β = 0.445
    σ = 0.1

    for ε in np.arange(0.072985, 0.072988, 0.0000001):
        ε = round(ε, 8)
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

        min_x = min(xx)
        min_y = min(yy)

        if min_x <= 0 or min_y <= 0:
            print("upper")

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


        min_x = min(xx)
        min_y = min(yy)

        if min_x <= 0 or min_y <= 0:
            print("lower")

        print('ε = ', ε)
