from math import sqrt, sin, cos

import numpy as np

from models.new_new_model import function


def run_eq():
    x_eq = 0.420583
    y_eq = 0.420583
    α = 1.0
    β = 0.445

    line = ""
    for σ in np.arange(0.0, 0.0421, 0.001):
        F = function.F(α, β, σ, x_eq, y_eq)
        FT = np.transpose(F)

        W0 = [[1, 0], [0, 1]]

        E = [[1, 0], [0, 1]]
        Q = E

        # Ограничние по итерациям: элементы матрицы i отличаются от элементов матрицы i+1 отличается в пятом знаке
        Wi = W0
        for i in range(100):
            Wi = np.add(np.dot(np.dot(F, Wi), FT), Q)
            print(i, Wi)

        Wi = np.array(Wi, dtype=float)

        eigen_values, eigen_vectors = np.linalg.eig(Wi)

        λ1, λ2 = eigen_values

        line += str(σ) + " " + str(λ1) + " " + str(λ2) + "\n"

    with open("C:\\users\\lkora\\desktop\\fsch.txt", 'w') as file:
        file.write(line)

def run_c2():
    # можно тут добавить прогон а потом взять два последних элемента

    # x = [0.588023, 0.250809]
    x = [0.85604, 0.158732]
    x = [0.179239, 0.857367]
    # x = [0.854848, 0.187168]
    # y = [0.250809, 0.588023]
    y = [0.158732, 0.85604]
    y = [0.857367, 0.179239]
    # y = [0.854848, 0.187168]
    α = 1.0
    β = 0.4

    flag1 = 0
    flag2 = 0

    line_min1 = ""
    line_min2 = ""
    line_max1 = ""
    line_max2 = ""
    for σ in np.arange(0.0426, 0.216, 0.0001):
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

        W2 = np.add(np.dot(np.dot(F1, W1), F1T), Q1)

        W1 = np.array(W1, dtype=float)
        W2 = np.array(W2, dtype=float)

        eigen_values, eigen_vectors = np.linalg.eig(W1)

        λ1, λ2 = eigen_values

        if flag1 == 0:
            if λ1 < λ2:
                flag1 = 1
            else:
                flag1 = 2

        if flag1 == 1:
            min1 = λ1
            max1 = λ2
        else:
            min1 = λ2
            max1 = λ1

        eigen_values, eigen_vectors = np.linalg.eig(W2)

        λ1, λ2 = eigen_values

        if flag2 == 0:
            if λ1 < λ2:
                flag2 = 1
            else:
                flag2 = 2

        if flag2 == 1:
            min2 = λ1
            max2 = λ2
        else:
            min2 = λ2
            max2 = λ1

        line_min1 += str(σ) + " " + str(min1) + "\n"
        line_min2 += str(σ) + " " + str(min2) + "\n"
        line_max1 += str(σ) + " " + str(max1) + "\n"
        line_max2 += str(σ) + " " + str(max2) + "\n"

    with open("C:\\users\\lkora\\desktop\\fsch_min1.txt", 'w') as file:
        file.write(line_min1)
    with open("C:\\users\\lkora\\desktop\\fsch_min2.txt", 'w') as file:
        file.write(line_min2)
    with open("C:\\users\\lkora\\desktop\\fsch_max1.txt", 'w') as file:
        file.write(line_max1)
    with open("C:\\users\\lkora\\desktop\\fsch_max2.txt", 'w') as file:
        file.write(line_max2)