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

    # x = [0.179239, 0.857367]
    x = [0.179239, 0.857367]
    # y = [0.179239, 0.857367]
    y = [0.857367, 0.179239]
    α = 1.0
    β = 0.4
    σ = 0.02
    ε = 0.02

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

    file = open("C:\\users\\lkora\\desktop\\dd\\ellips1.txt", "w")
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

    file = open("C:\\users\\lkora\\desktop\\dd\\ellips2.txt", "w")
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

def run_c6():
    # можно тут добавить прогон а потом взять два последних элемента

    # 6.1
    # x = [0.5719927893810252, 0.22834498152534183, 0.6533768799336029, 0.12037751048988818, 0.5941670677042235, 0.14120570444488975]
    # y = [0.32247291303079295, 0.5762418829073082, 0.19877809003468694, 0.6777760394303515, 0.07880744084981842, 0.43982704889612767]

    # 6.2
    x = [0.6777760394303517, 0.07880744084981736, 0.4398270488961216, 0.3224729130307987, 0.5762418829073052, 0.1987780900346871]
    y = [0.120377510489885, 0.5941670677042156, 0.1412057044448971, 0.5719927893810377, 0.22834498152533095, 0.653376879933606]

    α = 1.0
    β = 0.445
    σ = 0.27
    ε = 0.0005

    E = [[1, 0], [0, 1]]

    # additive
    Q1 = E
    Q2 = E
    Q3 = E
    Q4 = E
    Q5 = E
    Q6 = E
    # parametric
    # Q1 = [[(y[0] - x[0]) ** 2, -(y[0] - x[0]) ** 2], [-(y[0] - x[0]) ** 2, (y[0] - x[0]) ** 2]]
    # Q2 = [[(y[1] - x[1]) ** 2, -(y[1] - x[1]) ** 2], [-(y[1] - x[1]) ** 2, (y[1] - x[1]) ** 2]]
    # Q3 = [[(y[2] - x[2]) ** 2, -(y[2] - x[2]) ** 2], [-(y[2] - x[2]) ** 2, (y[2] - x[2]) ** 2]]
    # Q4 = [[(y[3] - x[3]) ** 2, -(y[3] - x[3]) ** 2], [-(y[3] - x[3]) ** 2, (y[3] - x[3]) ** 2]]
    # Q5 = [[(y[4] - x[4]) ** 2, -(y[4] - x[4]) ** 2], [-(y[4] - x[4]) ** 2, (y[4] - x[4]) ** 2]]
    # Q6 = [[(y[5] - x[5]) ** 2, -(y[5] - x[5]) ** 2], [-(y[5] - x[5]) ** 2, (y[5] - x[5]) ** 2]]

    F1 = function.F(α, β, σ, x[0], y[0])
    F2 = function.F(α, β, σ, x[1], y[1])
    F3 = function.F(α, β, σ, x[2], y[2])
    F4 = function.F(α, β, σ, x[3], y[3])
    F5 = function.F(α, β, σ, x[4], y[4])
    F6 = function.F(α, β, σ, x[5], y[5])

    F1T = np.transpose(F1)
    F2T = np.transpose(F2)
    F3T = np.transpose(F3)
    F4T = np.transpose(F4)
    F5T = np.transpose(F5)
    F6T = np.transpose(F6)

    Q_1 = Q6
    Q_2 = np.dot(np.dot(F6, Q5), F6T)
    Q_3 = np.dot(np.dot(np.dot(np.dot(F6, F5), Q4), F5T), F6T)
    Q_4 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F6, F5), F4), Q3), F4T), F5T), F6T)
    Q_5 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F6, F5), F4), F3), Q2), F3T), F4T), F5T), F6T)
    Q_6 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F6, F5), F4), F3), F2), Q1), F2T), F3T), F4T), F5T), F6T)
    Q = np.add(np.add(np.add(np.add(np.add(Q_1, Q_2), Q_3), Q_4), Q_5), Q_6)

    B = np.dot(np.dot(np.dot(np.dot(np.dot(F6, F5), F4), F3), F2), F1)
    BT = np.transpose(B)

    W1 = E
    for i in range(100):
        W1 = np.add(np.dot(np.dot(B, W1), BT), Q)
        # print(i, W1)

    W2 = np.add(np.dot(np.dot(F1, W1), F1T), Q1)
    W3 = np.add(np.dot(np.dot(F2, W2), F2T), Q2)
    W4 = np.add(np.dot(np.dot(F3, W3), F3T), Q3)
    W5 = np.add(np.dot(np.dot(F4, W4), F4T), Q4)
    W6 = np.add(np.dot(np.dot(F5, W5), F5T), Q5)

    W1 = np.array(W1, dtype=float)
    W2 = np.array(W2, dtype=float)
    W3 = np.array(W3, dtype=float)
    W4 = np.array(W4, dtype=float)
    W5 = np.array(W5, dtype=float)
    W6 = np.array(W6, dtype=float)

    Ws = [W1, W2, W3, W4, W5, W6]
    names = ["1", "2", "3", "4", "5", "6"]
    for i in range(len(Ws)):
        W = Ws[i]
        eigen_values, eigen_vectors = np.linalg.eig(W)

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
            xxx = x[i] + (z1 * v22 - z2 * v12) / (v11 * v22 - v12 * v21)
            yyy = y[i] + (z2 * v11 - z1 * v21) / (v11 * v22 - v12 * v21)
            xx.append(xxx)
            yy.append(yyy)

        file = open("C:\\users\\lkora\\desktop\\dd\\ellips" + names[i] + ".txt", "w")
        for i in range(len(xx)):
            file.write(str(xx[i]) + " " + str(yy[i]) + "\n")
        file.close()

def run_c10():
    # можно тут добавить прогон а потом взять два последних элемента
    x = [0.6363902563591886, 0.10844281002339379, 0.5221381325173345, 0.2506827382623543, 0.6599765764088453,
     0.10006111821309613, 0.5266295824777721, 0.2167039349062764, 0.641904368425501, 0.1442853518016976]
    y = [0.1000611182130943, 0.5266295824777656, 0.21670393490628337, 0.6419043684255001, 0.14428535180169838,
     0.6363902563591907, 0.10844281002339257, 0.5221381325173328, 0.25068273826235443, 0.6599765764088449]

    α = 1.0
    β = 0.445
    σ = 0.27
    ε = 0.0005

    E = [[1, 0], [0, 1]]

    # additive
    # Q1 = E
    # Q2 = E
    # Q3 = E
    # Q4 = E
    # Q5 = E
    # Q6 = E
    # Q7 = E
    # Q8 = E
    # Q9 = E
    # Q10 = E
    # parametric
    Q1 = [[(y[0] - x[0]) ** 2, -(y[0] - x[0]) ** 2], [-(y[0] - x[0]) ** 2, (y[0] - x[0]) ** 2]]
    Q2 = [[(y[1] - x[1]) ** 2, -(y[1] - x[1]) ** 2], [-(y[1] - x[1]) ** 2, (y[1] - x[1]) ** 2]]
    Q3 = [[(y[2] - x[2]) ** 2, -(y[2] - x[2]) ** 2], [-(y[2] - x[2]) ** 2, (y[2] - x[2]) ** 2]]
    Q4 = [[(y[3] - x[3]) ** 2, -(y[3] - x[3]) ** 2], [-(y[3] - x[3]) ** 2, (y[3] - x[3]) ** 2]]
    Q5 = [[(y[4] - x[4]) ** 2, -(y[4] - x[4]) ** 2], [-(y[4] - x[4]) ** 2, (y[4] - x[4]) ** 2]]
    Q6 = [[(y[5] - x[5]) ** 2, -(y[5] - x[5]) ** 2], [-(y[5] - x[5]) ** 2, (y[5] - x[5]) ** 2]]
    Q7 = [[(y[6] - x[6]) ** 2, -(y[6] - x[6]) ** 2], [-(y[6] - x[6]) ** 2, (y[6] - x[6]) ** 2]]
    Q8 = [[(y[7] - x[7]) ** 2, -(y[7] - x[7]) ** 2], [-(y[7] - x[7]) ** 2, (y[7] - x[7]) ** 2]]
    Q9 = [[(y[8] - x[8]) ** 2, -(y[8] - x[8]) ** 2], [-(y[8] - x[8]) ** 2, (y[8] - x[8]) ** 2]]
    Q10 = [[(y[9] - x[9]) ** 2, -(y[9] - x[9]) ** 2], [-(y[9] - x[9]) ** 2, (y[9] - x[9]) ** 2]]

    F1 = function.F(α, β, σ, x[0], y[0])
    F2 = function.F(α, β, σ, x[1], y[1])
    F3 = function.F(α, β, σ, x[2], y[2])
    F4 = function.F(α, β, σ, x[3], y[3])
    F5 = function.F(α, β, σ, x[4], y[4])
    F6 = function.F(α, β, σ, x[5], y[5])
    F7 = function.F(α, β, σ, x[6], y[6])
    F8 = function.F(α, β, σ, x[7], y[7])
    F9 = function.F(α, β, σ, x[8], y[8])
    F10 = function.F(α, β, σ, x[9], y[9])

    F1T = np.transpose(F1)
    F2T = np.transpose(F2)
    F3T = np.transpose(F3)
    F4T = np.transpose(F4)
    F5T = np.transpose(F5)
    F6T = np.transpose(F6)
    F7T = np.transpose(F7)
    F8T = np.transpose(F8)
    F9T = np.transpose(F9)
    F10T = np.transpose(F10)

    Q_1 = Q10
    Q_2 = np.dot(np.dot(F10, Q9), F10T)
    Q_3 = np.dot(np.dot(np.dot(np.dot(F10, F9), Q8), F9T), F10T)
    Q_4 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F10, F9), F8), Q7), F8T), F9T), F10T)
    Q_5 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F10, F9), F8), F7), Q6), F7T), F8T), F9T), F10T)
    Q_6 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F10, F9), F8), F7), F6), Q5), F6T), F7T), F8T), F9T), F10T)
    Q_7 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F10, F9), F8), F7), F6), F5), Q4), F5T), F6T), F7T), F8T), F9T), F10T)
    Q_8 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F10, F9), F8), F7), F6), F5), F4), Q3), F4T), F5T), F6T), F7T), F8T), F9T), F10T)
    Q_9 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F10, F9), F8), F7), F6), F5), F4), F3), Q2), F3T), F4T), F5T), F6T), F7T), F8T), F9T), F10T)
    Q_10 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F10, F9), F8), F7), F6), F5), F4), F3), F2), Q1), F2T), F3T), F4T), F5T), F6T), F7T), F8T), F9T), F10T)
    Q = np.add(np.add(np.add(np.add(np.add(np.add(np.add(np.add(np.add(Q_1, Q_2), Q_3), Q_4), Q_5), Q_6), Q_7), Q_8), Q_9), Q_10)

    B = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(F10, F9), F8), F7), F6), F5), F4), F3), F2), F1)
    BT = np.transpose(B)

    W1 = E
    for i in range(100):
        W1 = np.add(np.dot(np.dot(B, W1), BT), Q)
        # print(i, W1)

    W2 = np.add(np.dot(np.dot(F1, W1), F1T), Q1)
    W3 = np.add(np.dot(np.dot(F2, W2), F2T), Q2)
    W4 = np.add(np.dot(np.dot(F3, W3), F3T), Q3)
    W5 = np.add(np.dot(np.dot(F4, W4), F4T), Q4)
    W6 = np.add(np.dot(np.dot(F5, W5), F5T), Q5)
    W7 = np.add(np.dot(np.dot(F6, W6), F6T), Q6)
    W8 = np.add(np.dot(np.dot(F7, W7), F7T), Q7)
    W9 = np.add(np.dot(np.dot(F8, W8), F8T), Q8)
    W10 = np.add(np.dot(np.dot(F9, W9), F9T), Q9)

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
    names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    for i in range(len(Ws)):
        W = Ws[i]
        eigen_values, eigen_vectors = np.linalg.eig(W)

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
            xxx = x[i] + (z1 * v22 - z2 * v12) / (v11 * v22 - v12 * v21)
            yyy = y[i] + (z2 * v11 - z1 * v21) / (v11 * v22 - v12 * v21)
            xx.append(xxx)
            yy.append(yyy)

        file = open("C:\\users\\lkora\\desktop\\dd\\ellips" + names[i] + ".txt", "w")
        for i in range(len(xx)):
            file.write(str(xx[i]) + " " + str(yy[i]) + "\n")
        file.close()
