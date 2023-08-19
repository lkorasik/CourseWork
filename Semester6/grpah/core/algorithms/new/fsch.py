from math import sqrt, sin, cos

import numpy as np

from core.utils.convert_dict_to_lists import convert_dict_to_lists
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

def new_eq():
    # p_range0 = np.arange(0.0, 0.27, 0.0001)
    p_range0 = np.arange(0.0, 0.27, 0.001)
    time_range = range(20000)
    build_range = range(500)
    α = 1
    β = 0.445
    x_start = 0.88
    # x_start = 0.096
    # y_start = 0.4
    y_start = 0.17
    # y_start = 0.087
    f = lambda p, x, y: function.__x(α, β, p, x, y)
    g = lambda p, x, y: function.__y(α, β, p, x, y)

    upper_bound = 1000
    lower_bound = None

    # ->
    values_x0 = dict()
    values_y0 = dict()

    dx = 0.02
    dy = 0.03

    x_0 = x_start
    y_0 = y_start
    for p in p_range0:
        values_x0[p] = []
        values_y0[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out high", p)
                break
            x_0 = x_t
            y_0 = y_t
        for _ in build_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out high", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_x0[p].append(x_t)
            values_y0[p].append(y_t)

    line = ""
    for σ in p_range0:
        if σ > 0.042:
            break

        x_eq = values_x0[σ][0]
        y_eq = values_y0[σ][0]

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

    with open("C:\\users\\lkora\\desktop\\dd\\fsch_eq.txt", 'w') as file:
        file.write(line)

    line_min1 = ""
    line_min2 = ""
    line_max1 = ""
    line_max2 = ""
    for σ in p_range0:
        if σ > 0.2175:
            break
        if σ < 0.0427:
            continue

        x_c2_1 = values_x0[σ][0]
        y_c2_1 = values_y0[σ][0]
        x_c2_2 = values_x0[σ][1]
        y_c2_2 = values_y0[σ][1]

        # additive
        Q1 = E
        Q2 = E
        # parametric
        # Q1 = [[(y[0] - x[0]) ** 2, -(y[0] - x[0]) ** 2], [-(y[0] - x[0]) ** 2, (y[0] - x[0]) ** 2]]
        # Q2 = [[(y[1] - x[1]) ** 2, -(y[1] - x[1]) ** 2], [-(y[1] - x[1]) ** 2, (y[1] - x[1]) ** 2]]

        F1 = function.F(α, β, σ, x_c2_1, y_c2_1)
        F2 = function.F(α, β, σ, x_c2_2, y_c2_2)

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

        min1 = min(λ1, λ2)
        max1 = max(λ1, λ2)

        eigen_values, eigen_vectors = np.linalg.eig(W2)

        λ1, λ2 = eigen_values

        min2 = min(λ1, λ2)
        max2 = max(λ1, λ2)

        line_min1 += str(σ) + " " + str(min1) + "\n"
        line_min2 += str(σ) + " " + str(min2) + "\n"
        line_max1 += str(σ) + " " + str(max1) + "\n"
        line_max2 += str(σ) + " " + str(max2) + "\n"

    with open("C:\\users\\lkora\\desktop\\dd\\fsch_c2_min1.txt", 'w') as file:
        file.write(line_min1)
    with open("C:\\users\\lkora\\desktop\\dd\\fsch_c2_min2.txt", 'w') as file:
        file.write(line_min2)
    with open("C:\\users\\lkora\\desktop\\dd\\fsch_c2_max1.txt", 'w') as file:
        file.write(line_max1)
    with open("C:\\users\\lkora\\desktop\\dd\\fsch_c2_max2.txt", 'w') as file:
        file.write(line_max2)

    line_min = [""] * 10
    line_max = [""] * 10
    for σ in p_range0:
        if σ > 0.2481:
            break
        if σ < 0.27:
            continue

        x = values_x0[σ]
        y = values_y0[σ]

        # additive
        Q = [E] * 10
        # parametric
        # Q1 = [[(y[0] - x[0]) ** 2, -(y[0] - x[0]) ** 2], [-(y[0] - x[0]) ** 2, (y[0] - x[0]) ** 2]]
        # Q2 = [[(y[1] - x[1]) ** 2, -(y[1] - x[1]) ** 2], [-(y[1] - x[1]) ** 2, (y[1] - x[1]) ** 2]]

        F = []
        for i in range(10):
            Fi = function.F(α, β, σ, x[i], y[i])
            F.append(Fi)

        FT = []
        for Fi in F:
            FTi = np.transpose(Fi)
            FT.append(FTi)

        Q = np.add(Q[1], np.dot(np.dot(F[1], Q[0]), FT[1]))

        B = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F[9], F[8]), F[7]), F[6]), F[5]), F[4]), F[3]), F[2]), F[1]), F[0])
        BT = np.transpose(B)

        W1 = E
        for i in range(100):
            W1 = np.add(np.dot(np.dot(B, W1), BT), Q)

        W2 = np.add(np.dot(np.dot(F[0], W1), FT[0]), Q[0])
        W3 = np.add(np.dot(np.dot(F[1], W2), FT[1]), Q[1])
        W4 = np.add(np.dot(np.dot(F[2], W3), FT[2]), Q[2])
        W5 = np.add(np.dot(np.dot(F[3], W4), FT[3]), Q[3])
        W6 = np.add(np.dot(np.dot(F[4], W5), FT[4]), Q[4])
        W7 = np.add(np.dot(np.dot(F[5], W6), FT[5]), Q[5])
        W8 = np.add(np.dot(np.dot(F[6], W7), FT[6]), Q[6])
        W9 = np.add(np.dot(np.dot(F[7], W8), FT[7]), Q[7])
        W10 = np.add(np.dot(np.dot(F[8], W9), FT[8]), Q[8])

        W1 = np.array(W1, dtype=float)
        W2 = np.array(W2, dtype=float)
        W3 = np.array(W3, dtype=float)
        W4 = np.array(W4, dtype=float)
        W5 = np.array(W5, dtype=float)
        W6 = np.array(W6, dtype=float)
        W7 = np.array(W7, dtype=float)
        W8 = np.array(W8, dtype=float)
        W9 = np.array(W9, dtype=float)
        W10 = np.array(W10, dtype=float)

        Ws = [W1, W2, W3, W4, W5, W6, W7, W8, W9, W10]

        for i in range(len(Ws)):
            W = Ws[i]
            eigen_values, eigen_vectors = np.linalg.eig(W)

            λ1, λ2 = eigen_values

            min1 = min(λ1, λ2)
            max1 = max(λ1, λ2)

            line_min[i] += str(σ) + " " + str(min1) + "\n"
            line_max[i] += str(σ) + " " + str(max1) + "\n"

    for i in range(len(line_min)):
        with open("C:\\users\\lkora\\desktop\\dd\\fsch_c10_min" + str(i + 1) + ".txt", 'w') as file:
            file.write(line_min[i])
        with open("C:\\users\\lkora\\desktop\\dd\\fsch_c10_max" + str(i + 1) + ".txt", 'w') as file:
            file.write(line_max[i])
