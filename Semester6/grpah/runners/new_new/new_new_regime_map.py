from collections import Counter

import numpy as np

from core.utils.is_out_of_bounds import is_out_of_bounds
from models.new_new_model import function


def run0():
    α = 1
    a_range = np.arange(0, 1, 0.001)  # β
    b_range = np.arange(0, 1, 0.001)  # σ
    x_start = 0.2
    # x_start = 0.88
    y_start = 0.3
    # y_start = 0.17
    time_range = range(0, 10000 + 1)
    f = lambda β, σ, x, y: function.__x(α, β, σ, x, y)
    g = lambda β, σ, x, y: function.__y(α, β, σ, x, y)
    file_path = "C:\\users\\lkora\\desktop\\data3\\"
    lower_bound = 0
    upper_bound = 1000

    result_x = dict()
    result_y = dict()
    for a in a_range:
        fk = round(a, 5)
        result_x[fk] = dict()
        result_y[fk] = dict()
        print(fk)
        for b_x in b_range:
            sc = round(b_x, 5)
            result_x[fk][sc] = []
            result_y[fk][sc] = []
            x0 = x_start
            y0 = y_start
            for _ in time_range:
                xt = f(a, b_x, x0, y0)
                yt = g(a, b_x, x0, y0)
                if is_out_of_bounds(xt, upper_bound, lower_bound):
                    print("a ", fk, " b ", sc, " x ", xt)
                    break
                if is_out_of_bounds(yt, upper_bound, lower_bound):
                    print("a ", fk, " b ", sc, " y ", yt)
                    break
                x0 = xt
                y0 = yt
            for t in range(20):
                xt = f(a, b_x, x0, y0)
                yt = g(a, b_x, x0, y0)
                if is_out_of_bounds(xt, upper_bound, lower_bound):
                    print("a ", fk, " b ", sc, " x ", xt)
                    break
                if is_out_of_bounds(yt, upper_bound, lower_bound):
                    print("a ", fk, " b ", sc, " y ", yt)
                    break
                result_x[fk][sc].append(xt)
                result_y[fk][sc].append(yt)
                x0 = xt
                y0 = yt

    print("data collected")

    res_x = dict()
    res_y = dict()
    for j in range(1, 15 + 1):
        res_x[j] = []
        res_y[j] = []
        for a in a_range:
            fk = round(a, 5)
            for b_x in b_range:
                sc = round(b_x, 5)
                data_x = result_x[fk][sc]
                data_y = result_y[fk][sc]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)

                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                # можно забить на это условие?
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([fk, sc, di_x.keys()])
                    res_y[j].append([fk, sc, di_y.keys()])
                    continue

    for j in res_x.keys():
        for i in res_x[j]:
            print(i[0], i[1], set(i[2]))
    for j in res_y.keys():
        for i in res_y[j]:
            print(i[0], i[1], set(i[2]))

    peq_x = open(file_path + "eqX2Gt2X1_x.txt", "w")
    peq1_x = open(file_path + "eqX2Lt2X1_x.txt", 'w')
    c2_x = open(file_path + 'cycle2_x.txt', 'w')
    c3_x = open(file_path + 'cycle3_x.txt', 'w')
    c4_x = open(file_path + 'cycle4_x.txt', 'w')
    c5_x = open(file_path + 'cycle5_x.txt', 'w')
    c6_x = open(file_path + 'cycle6_x.txt', 'w')
    c7_x = open(file_path + 'cycle7_x.txt', 'w')
    c8_x = open(file_path + 'cycle8_x.txt', 'w')
    c9_x = open(file_path + 'cycle9_x.txt', 'w')
    c11_x = open(file_path + 'cycle11_x.txt', 'w')
    c10_x = open(file_path + 'cycle10_x.txt', 'w')
    c12_x = open(file_path + 'cycle12_x.txt', 'w')
    c13_x = open(file_path + 'cycle13_x.txt', 'w')
    c14_x = open(file_path + 'cycle14_x.txt', 'w')
    c15_x = open(file_path + 'cycle15_x.txt', 'w')

    peq_y = open(file_path + "eqX2Gt2X1_y.txt", "w")
    peq1_y = open(file_path + "eqX2Lt2X1_y.txt", 'w')
    c2_y = open(file_path + 'cycle2_y.txt', 'w')
    c3_y = open(file_path + 'cycle3_y.txt', 'w')
    c4_y = open(file_path + 'cycle4_y.txt', 'w')
    c5_y = open(file_path + 'cycle5_y.txt', 'w')
    c6_y = open(file_path + 'cycle6_y.txt', 'w')
    c7_y = open(file_path + 'cycle7_y.txt', 'w')
    c8_y = open(file_path + 'cycle8_y.txt', 'w')
    c9_y = open(file_path + 'cycle9_y.txt', 'w')
    c11_y = open(file_path + 'cycle11_y.txt', 'w')
    c10_y = open(file_path + 'cycle10_y.txt', 'w')
    c12_y = open(file_path + 'cycle12_y.txt', 'w')
    c13_y = open(file_path + 'cycle13_y.txt', 'w')
    c14_y = open(file_path + 'cycle14_y.txt', 'w')
    c15_y = open(file_path + 'cycle15_y.txt', 'w')

    for j in range(1, 10 + 1):
        line = ""
        k = ""
        for item in res_x[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_x.write(k)
            peq_x.write(line)
        if j == 2:
            c2_x.write(line)
        if j == 3:
            c3_x.write(line)
        if j == 4:
            c4_x.write(line)
        if j == 5:
            c5_x.write(line)
        if j == 6:
            c6_x.write(line)
        if j == 7:
            c7_x.write(line)
        if j == 8:
            c8_x.write(line)
        if j == 9:
            c9_x.write(line)
        if j == 10:
            c10_x.write(line)
        if j == 11:
            c11_x.write(line)
        if j == 12:
            c12_x.write(line)
        if j == 13:
            c13_x.write(line)
        if j == 14:
            c14_x.write(line)
        if j == 15:
            c15_x.write(line)

    for j in range(1, 10 + 1):
        line = ""
        k = ""
        for item in res_y[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_y.write(k)
            peq_y.write(line)
        if j == 2:
            c2_y.write(line)
        if j == 3:
            c3_y.write(line)
        if j == 4:
            c4_y.write(line)
        if j == 5:
            c5_y.write(line)
        if j == 6:
            c6_y.write(line)
        if j == 7:
            c7_y.write(line)
        if j == 8:
            c8_y.write(line)
        if j == 9:
            c9_y.write(line)
        if j == 10:
            c10_y.write(line)
        if j == 11:
            c11_y.write(line)
        if j == 12:
            c12_y.write(line)
        if j == 13:
            c13_y.write(line)
        if j == 14:
            c14_y.write(line)
        if j == 15:
            c15_y.write(line)

    peq1_x.close()
    peq_x.close()
    c2_x.close()
    c3_x.close()
    c4_x.close()
    c5_x.close()
    c6_x.close()
    c7_x.close()
    c8_x.close()
    c9_x.close()
    c10_x.close()
    c11_x.close()
    c12_x.close()
    c13_x.close()
    c14_x.close()
    c15_x.close()

    peq1_y.close()
    peq_y.close()
    c2_y.close()
    c3_y.close()
    c4_y.close()
    c5_y.close()
    c6_y.close()
    c7_y.close()
    c8_y.close()
    c9_y.close()
    c10_y.close()
    c11_y.close()
    c12_y.close()
    c13_y.close()
    c14_y.close()
    c15_y.close()


def run1():
    α = 1
    a_range = np.arange(0.3962, 0.59, 0.001)  # β
    ra_range = np.arange(0.3962, 0.0, -0.001)  # β
    b_range = np.arange(0, 0.9, 0.001)  # σ
    x_start = 0.2
    y_start = 0.3
    time_range = range(0, 10000 + 1)
    f = lambda β, σ, x, y: function.__x(α, β, σ, x, y)
    g = lambda β, σ, x, y: function.__y(α, β, σ, x, y)
    file_path = "C:\\users\\lkora\\desktop\\data4\\"

    result_x = dict()
    result_y = dict()
    for a in a_range:
        fk = round(a, 5)
        result_x[fk] = dict()
        result_y[fk] = dict()
        print(fk)
        x0 = x_start
        y0 = y_start
        for b_x in b_range:
            sc = round(b_x, 5)
            result_x[fk][sc] = []
            result_y[fk][sc] = []
            for _ in time_range:
                xt = f(a, b_x, x0, y0)
                yt = g(a, b_x, x0, y0)
                x0 = xt
                y0 = yt
            for t in range(20):
                xt = f(a, b_x, x0, y0)
                yt = g(a, b_x, x0, y0)
                # if is_out_of_bounds(xt, 10, 0):
                #     break
                # if is_out_of_bounds(yt, 10, 0):
                #     break
                result_x[fk][sc].append(xt)
                result_y[fk][sc].append(yt)
                x0 = xt
                y0 = yt
    for a in ra_range:
        fk = round(a, 5)
        result_x[fk] = dict()
        result_y[fk] = dict()
        print(fk)
        x0 = x_start
        y0 = y_start
        for b_x in b_range:
            sc = round(b_x, 5)
            result_x[fk][sc] = []
            result_y[fk][sc] = []
            for _ in time_range:
                xt = f(a, b_x, x0, y0)
                yt = g(a, b_x, x0, y0)
                x0 = xt
                y0 = yt
            for t in range(20):
                xt = f(a, b_x, x0, y0)
                yt = g(a, b_x, x0, y0)
                result_x[fk][sc].append(xt)
                result_y[fk][sc].append(yt)
                x0 = xt
                y0 = yt

    print("data collected")

    res_x = dict()
    res_y = dict()
    for j in range(1, 10 + 1):
        res_x[j] = []
        res_y[j] = []
        for a in a_range:
            fk = round(a, 5)
            for b_x in b_range:
                sc = round(b_x, 5)
                data_x = result_x[fk][sc]
                data_y = result_y[fk][sc]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)

                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                # можно забить на это условие?
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([fk, sc, di_x.keys()])
                    res_y[j].append([fk, sc, di_y.keys()])
                    continue
        for a in ra_range:
            fk = round(a, 5)
            for b_x in b_range:
                sc = round(b_x, 5)
                data_x = result_x[fk][sc]
                data_y = result_y[fk][sc]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)

                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                # можно забить на это условие?
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([fk, sc, di_x.keys()])
                    res_y[j].append([fk, sc, di_y.keys()])
                    continue

    for j in res_x.keys():
        for i in res_x[j]:
            print(i[0], i[1], set(i[2]))
    for j in res_y.keys():
        for i in res_y[j]:
            print(i[0], i[1], set(i[2]))

    peq_x = open(file_path + "eqX2Gt2X1_x.txt", "w")
    peq1_x = open(file_path + "eqX2Lt2X1_x.txt", 'w')
    c2_x = open(file_path + 'cycle2_x.txt', 'w')
    c3_x = open(file_path + 'cycle3_x.txt', 'w')
    c4_x = open(file_path + 'cycle4_x.txt', 'w')
    c5_x = open(file_path + 'cycle5_x.txt', 'w')
    c6_x = open(file_path + 'cycle6_x.txt', 'w')
    c7_x = open(file_path + 'cycle7_x.txt', 'w')
    c8_x = open(file_path + 'cycle8_x.txt', 'w')
    c9_x = open(file_path + 'cycle9_x.txt', 'w')
    c11_x = open(file_path + 'cycle11_x.txt', 'w')
    c10_x = open(file_path + 'cycle10_x.txt', 'w')
    c12_x = open(file_path + 'cycle12_x.txt', 'w')
    c13_x = open(file_path + 'cycle13_x.txt', 'w')
    c14_x = open(file_path + 'cycle14_x.txt', 'w')
    c15_x = open(file_path + 'cycle15_x.txt', 'w')

    peq_y = open(file_path + "eqX2Gt2X1_y.txt", "w")
    peq1_y = open(file_path + "eqX2Lt2X1_y.txt", 'w')
    c2_y = open(file_path + 'cycle2_y.txt', 'w')
    c3_y = open(file_path + 'cycle3_y.txt', 'w')
    c4_y = open(file_path + 'cycle4_y.txt', 'w')
    c5_y = open(file_path + 'cycle5_y.txt', 'w')
    c6_y = open(file_path + 'cycle6_y.txt', 'w')
    c7_y = open(file_path + 'cycle7_y.txt', 'w')
    c8_y = open(file_path + 'cycle8_y.txt', 'w')
    c9_y = open(file_path + 'cycle9_y.txt', 'w')
    c11_y = open(file_path + 'cycle11_y.txt', 'w')
    c10_y = open(file_path + 'cycle10_y.txt', 'w')
    c12_y = open(file_path + 'cycle12_y.txt', 'w')
    c13_y = open(file_path + 'cycle13_y.txt', 'w')
    c14_y = open(file_path + 'cycle14_y.txt', 'w')
    c15_y = open(file_path + 'cycle15_y.txt', 'w')

    for j in range(1, 10 + 1):
        line = ""
        k = ""
        for item in res_x[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_x.write(k)
            peq_x.write(line)
        if j == 2:
            c2_x.write(line)
        if j == 3:
            c3_x.write(line)
        if j == 4:
            c4_x.write(line)
        if j == 5:
            c5_x.write(line)
        if j == 6:
            c6_x.write(line)
        if j == 7:
            c7_x.write(line)
        if j == 8:
            c8_x.write(line)
        if j == 9:
            c9_x.write(line)
        if j == 10:
            c10_x.write(line)
        if j == 11:
            c11_x.write(line)
        if j == 12:
            c12_x.write(line)
        if j == 13:
            c13_x.write(line)
        if j == 14:
            c14_x.write(line)
        if j == 15:
            c15_x.write(line)

    for j in range(1, 10 + 1):
        line = ""
        k = ""
        for item in res_y[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_y.write(k)
            peq_y.write(line)
        if j == 2:
            c2_y.write(line)
        if j == 3:
            c3_y.write(line)
        if j == 4:
            c4_y.write(line)
        if j == 5:
            c5_y.write(line)
        if j == 6:
            c6_y.write(line)
        if j == 7:
            c7_y.write(line)
        if j == 8:
            c8_y.write(line)
        if j == 9:
            c9_y.write(line)
        if j == 10:
            c10_y.write(line)
        if j == 11:
            c11_y.write(line)
        if j == 12:
            c12_y.write(line)
        if j == 13:
            c13_y.write(line)
        if j == 14:
            c14_y.write(line)
        if j == 15:
            c15_y.write(line)

    peq1_x.close()
    peq_x.close()
    c2_x.close()
    c3_x.close()
    c4_x.close()
    c5_x.close()
    c6_x.close()
    c7_x.close()
    c8_x.close()
    c9_x.close()
    c10_x.close()
    c11_x.close()
    c12_x.close()
    c13_x.close()
    c14_x.close()
    c15_x.close()

    peq1_y.close()
    peq_y.close()
    c2_y.close()
    c3_y.close()
    c4_y.close()
    c5_y.close()
    c6_y.close()
    c7_y.close()
    c8_y.close()
    c9_y.close()
    c10_y.close()
    c11_y.close()
    c12_y.close()
    c13_y.close()
    c14_y.close()
    c15_y.close()


def run2():
    α = 1
    x_start = 0.88
    y_start = 0.17
    time_range = range(0, 10000 + 1)
    f = lambda β, σ, x, y: function.__x(α, β, σ, x, y)
    g = lambda β, σ, x, y: function.__y(α, β, σ, x, y)
    file_path = "C:\\users\\lkora\\desktop\\data6\\"

    result_x = dict()
    result_y = dict()

    dx = 0.00175  # 0.175
    dy = 0.01  # 0.1

    sx = 0.42
    sy = 0

    x2 = [sx + i * dx for i in range(100)]  # 11
    y2 = [sy + i * dy for i in range(100)]  # 11

    file = open(file_path + "test.txt", 'w')

    rx = x_start
    ry = y_start
    for pair in list(zip(x2, y2)):
        a = pair[0]  # β
        b = pair[1]  # σ

        file.write(str(a) + " " + str(b) + "\n")

        result_x[b] = dict()
        result_y[b] = dict()

        result_x[b][a] = []
        result_y[b][a] = []

        print(a, b)

        x0 = rx
        y0 = ry
        for _ in time_range:
            xt = f(a, b, x0, y0)
            yt = g(a, b, x0, y0)
            x0 = xt
            y0 = yt
        for t in range(20):
            xt = f(a, b, x0, y0)
            yt = g(a, b, x0, y0)
            result_x[b][a].append(xt)
            result_y[b][a].append(yt)
            x0 = xt
            y0 = yt

        rx = x0
        ry = y0

        x0 = rx
        y0 = ry
        for x in np.arange(a - 0.01, 0, -0.01):  # 0.1
            result_x[b][x] = []
            result_y[b][x] = []

            print(x, b)

            for _ in time_range:
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                x0 = xt
                y0 = yt
            for t in range(20):
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                result_x[b][x].append(xt)
                result_y[b][x].append(yt)
                x0 = xt
                y0 = yt

        x0 = rx
        y0 = ry
        for x in np.arange(a + 0.01, 1, 0.01):  # 0.1
            result_x[b][x] = []
            result_y[b][x] = []

            print(x, b)

            for _ in time_range:
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                x0 = xt
                y0 = yt
            for t in range(20):
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                result_x[b][x].append(xt)
                result_y[b][x].append(yt)
                x0 = xt
                y0 = yt

    res_x = dict()
    res_y = dict()
    for j in range(1, 10 + 1):
        res_x[j] = []
        res_y[j] = []
        for pair in list(zip(x2, y2)):
            a = pair[0]  # x
            b = pair[1]  # y

            data_x = result_x[b][a]
            data_y = result_y[b][a]
            for i in range(len(data_x)):
                data_x[i] = round(data_x[i], 5)
            for i in range(len(data_y)):
                data_y[i] = round(data_y[i], 5)
            # используй set
            di_x = Counter(data_x)
            di_y = Counter(data_y)
            # print(fk, sc, Counter(data))
            if len(di_x.keys()) == j and len(di_y.keys()) == j:
                res_x[j].append([b, a, di_x.keys()])
                res_y[j].append([b, a, di_y.keys()])
                # continue

            for x in np.arange(a - 0.01, 0, -0.01):  # 0.1
                data_x = result_x[b][x]
                data_y = result_y[b][x]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)
                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([b, x, di_x.keys()])
                    res_y[j].append([b, x, di_y.keys()])
                    continue

            for x in np.arange(a + 0.01, 1, 0.01):  # 0.1
                data_x = result_x[b][x]
                data_y = result_y[b][x]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)
                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([b, x, di_x.keys()])
                    res_y[j].append([b, x, di_y.keys()])
                    continue

    for j in res_x.keys():
        for i in res_x[j]:
            print(i[0], i[1], set(i[2]))
    for j in res_y.keys():
        for i in res_y[j]:
            print(i[0], i[1], set(i[2]))

    peq_x = open(file_path + "eqX2Gt2X1_x.txt", "w")
    peq1_x = open(file_path + "eqX2Lt2X1_x.txt", 'w')
    c2_x = open(file_path + 'cycle2_x.txt', 'w')
    c3_x = open(file_path + 'cycle3_x.txt', 'w')
    c4_x = open(file_path + 'cycle4_x.txt', 'w')
    c5_x = open(file_path + 'cycle5_x.txt', 'w')
    c6_x = open(file_path + 'cycle6_x.txt', 'w')
    c7_x = open(file_path + 'cycle7_x.txt', 'w')
    c8_x = open(file_path + 'cycle8_x.txt', 'w')
    c9_x = open(file_path + 'cycle9_x.txt', 'w')
    c11_x = open(file_path + 'cycle11_x.txt', 'w')
    c10_x = open(file_path + 'cycle10_x.txt', 'w')
    c12_x = open(file_path + 'cycle12_x.txt', 'w')
    c13_x = open(file_path + 'cycle13_x.txt', 'w')
    c14_x = open(file_path + 'cycle14_x.txt', 'w')
    c15_x = open(file_path + 'cycle15_x.txt', 'w')

    peq_y = open(file_path + "eqX2Gt2X1_y.txt", "w")
    peq1_y = open(file_path + "eqX2Lt2X1_y.txt", 'w')
    c2_y = open(file_path + 'cycle2_y.txt', 'w')
    c3_y = open(file_path + 'cycle3_y.txt', 'w')
    c4_y = open(file_path + 'cycle4_y.txt', 'w')
    c5_y = open(file_path + 'cycle5_y.txt', 'w')
    c6_y = open(file_path + 'cycle6_y.txt', 'w')
    c7_y = open(file_path + 'cycle7_y.txt', 'w')
    c8_y = open(file_path + 'cycle8_y.txt', 'w')
    c9_y = open(file_path + 'cycle9_y.txt', 'w')
    c11_y = open(file_path + 'cycle11_y.txt', 'w')
    c10_y = open(file_path + 'cycle10_y.txt', 'w')
    c12_y = open(file_path + 'cycle12_y.txt', 'w')
    c13_y = open(file_path + 'cycle13_y.txt', 'w')
    c14_y = open(file_path + 'cycle14_y.txt', 'w')
    c15_y = open(file_path + 'cycle15_y.txt', 'w')

    for j in range(1, 10 + 1):
        line = ""
        k = ""
        for item in res_x[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_x.write(k)
            peq_x.write(line)
        if j == 2:
            c2_x.write(line)
        if j == 3:
            c3_x.write(line)
        if j == 4:
            c4_x.write(line)
        if j == 5:
            c5_x.write(line)
        if j == 6:
            c6_x.write(line)
        if j == 7:
            c7_x.write(line)
        if j == 8:
            c8_x.write(line)
        if j == 9:
            c9_x.write(line)
        if j == 10:
            c10_x.write(line)
        if j == 11:
            c11_x.write(line)
        if j == 12:
            c12_x.write(line)
        if j == 13:
            c13_x.write(line)
        if j == 14:
            c14_x.write(line)
        if j == 15:
            c15_x.write(line)

    for j in range(1, 10 + 1):
        line = ""
        k = ""
        for item in res_y[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_y.write(k)
            peq_y.write(line)
        if j == 2:
            c2_y.write(line)
        if j == 3:
            c3_y.write(line)
        if j == 4:
            c4_y.write(line)
        if j == 5:
            c5_y.write(line)
        if j == 6:
            c6_y.write(line)
        if j == 7:
            c7_y.write(line)
        if j == 8:
            c8_y.write(line)
        if j == 9:
            c9_y.write(line)
        if j == 10:
            c10_y.write(line)
        if j == 11:
            c11_y.write(line)
        if j == 12:
            c12_y.write(line)
        if j == 13:
            c13_y.write(line)
        if j == 14:
            c14_y.write(line)
        if j == 15:
            c15_y.write(line)

    file.close()

    peq1_x.close()
    peq_x.close()
    c2_x.close()
    c3_x.close()
    c4_x.close()
    c5_x.close()
    c6_x.close()
    c7_x.close()
    c8_x.close()
    c9_x.close()
    c10_x.close()
    c11_x.close()
    c12_x.close()
    c13_x.close()
    c14_x.close()
    c15_x.close()

    peq1_y.close()
    peq_y.close()
    c2_y.close()
    c3_y.close()
    c4_y.close()
    c5_y.close()
    c6_y.close()
    c7_y.close()
    c8_y.close()
    c9_y.close()
    c10_y.close()
    c11_y.close()
    c12_y.close()
    c13_y.close()
    c14_y.close()
    c15_y.close()


def run3():
    α = 1
    x_start = 0.88
    y_start = 0.17
    time_range = range(0, 10000 + 1)
    f = lambda β, σ, x, y: function.__x(α, β, σ, x, y)
    g = lambda β, σ, x, y: function.__y(α, β, σ, x, y)
    file_path = "C:\\users\\lkora\\desktop\\data7\\"

    result_x = dict()
    result_y = dict()

    n = 200
    dx = (0.595 - 0.42) / n
    dy = (1 - 0) / n

    sx = 0.42
    sy = 0

    x2 = [sx + i * dx for i in range(n)]  # 11
    y2 = [sy + i * dy for i in range(n)]  # 11

    file = open(file_path + "test.txt", 'w')

    rx = x_start
    ry = y_start
    for pair in list(zip(x2, y2)):
        a = pair[0]  # β
        b = pair[1]  # σ

        file.write(str(a) + " " + str(b) + "\n")

        result_x[b] = dict()
        result_y[b] = dict()

        result_x[b][a] = []
        result_y[b][a] = []

        print(a, b)

        x0 = rx
        y0 = ry
        for _ in time_range:
            xt = f(a, b, x0, y0)
            yt = g(a, b, x0, y0)
            x0 = xt
            y0 = yt
        for t in range(20):
            xt = f(a, b, x0, y0)
            yt = g(a, b, x0, y0)
            result_x[b][a].append(xt)
            result_y[b][a].append(yt)
            x0 = xt
            y0 = yt

        rx = x0
        ry = y0

        x0 = rx
        y0 = ry
        for x in np.arange(a - 0.001, 0, -0.001):  # 0.1
            result_x[b][x] = []
            result_y[b][x] = []

            print(x, b)

            for _ in time_range:
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                x0 = xt
                y0 = yt
            for t in range(20):
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                result_x[b][x].append(xt)
                result_y[b][x].append(yt)
                x0 = xt
                y0 = yt

        x0 = rx
        y0 = ry
        for x in np.arange(a + 0.001, 0.7, 0.001):  # 0.1
            result_x[b][x] = []
            result_y[b][x] = []

            print(x, b)

            for _ in time_range:
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                x0 = xt
                y0 = yt
            for t in range(20):
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                result_x[b][x].append(xt)
                result_y[b][x].append(yt)
                x0 = xt
                y0 = yt

    res_x = dict()
    res_y = dict()
    for j in range(1, 15 + 1):
        res_x[j] = []
        res_y[j] = []
        for pair in list(zip(x2, y2)):
            a = pair[0]  # x
            b = pair[1]  # y

            data_x = result_x[b][a]
            data_y = result_y[b][a]
            for i in range(len(data_x)):
                data_x[i] = round(data_x[i], 5)
            for i in range(len(data_y)):
                data_y[i] = round(data_y[i], 5)
            # используй set
            di_x = Counter(data_x)
            di_y = Counter(data_y)
            # print(fk, sc, Counter(data))
            if len(di_x.keys()) == j and len(di_y.keys()) == j:
                res_x[j].append([b, a, di_x.keys()])
                res_y[j].append([b, a, di_y.keys()])
                # continue

            for x in np.arange(a - 0.001, 0, -0.001):  # 0.1
                data_x = result_x[b][x]
                data_y = result_y[b][x]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)
                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([b, x, di_x.keys()])
                    res_y[j].append([b, x, di_y.keys()])
                    continue

            for x in np.arange(a + 0.001, 0.7, 0.001):  # 0.1
                data_x = result_x[b][x]
                data_y = result_y[b][x]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)
                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([b, x, di_x.keys()])
                    res_y[j].append([b, x, di_y.keys()])
                    continue

    for j in res_x.keys():
        for i in res_x[j]:
            print(i[0], i[1], set(i[2]))
    for j in res_y.keys():
        for i in res_y[j]:
            print(i[0], i[1], set(i[2]))

    peq_x = open(file_path + "eqX2Gt2X1_x.txt", "w")
    peq1_x = open(file_path + "eqX2Lt2X1_x.txt", 'w')
    c2_x = open(file_path + 'cycle2_x.txt', 'w')
    c3_x = open(file_path + 'cycle3_x.txt', 'w')
    c4_x = open(file_path + 'cycle4_x.txt', 'w')
    c5_x = open(file_path + 'cycle5_x.txt', 'w')
    c6_x = open(file_path + 'cycle6_x.txt', 'w')
    c7_x = open(file_path + 'cycle7_x.txt', 'w')
    c8_x = open(file_path + 'cycle8_x.txt', 'w')
    c9_x = open(file_path + 'cycle9_x.txt', 'w')
    c11_x = open(file_path + 'cycle11_x.txt', 'w')
    c10_x = open(file_path + 'cycle10_x.txt', 'w')
    c12_x = open(file_path + 'cycle12_x.txt', 'w')
    c13_x = open(file_path + 'cycle13_x.txt', 'w')
    c14_x = open(file_path + 'cycle14_x.txt', 'w')
    c15_x = open(file_path + 'cycle15_x.txt', 'w')
    c16_x = open(file_path + 'cycle16_x.txt', 'w')

    peq_y = open(file_path + "eqX2Gt2X1_y.txt", "w")
    peq1_y = open(file_path + "eqX2Lt2X1_y.txt", 'w')
    c2_y = open(file_path + 'cycle2_y.txt', 'w')
    c3_y = open(file_path + 'cycle3_y.txt', 'w')
    c4_y = open(file_path + 'cycle4_y.txt', 'w')
    c5_y = open(file_path + 'cycle5_y.txt', 'w')
    c6_y = open(file_path + 'cycle6_y.txt', 'w')
    c7_y = open(file_path + 'cycle7_y.txt', 'w')
    c8_y = open(file_path + 'cycle8_y.txt', 'w')
    c9_y = open(file_path + 'cycle9_y.txt', 'w')
    c11_y = open(file_path + 'cycle11_y.txt', 'w')
    c10_y = open(file_path + 'cycle10_y.txt', 'w')
    c12_y = open(file_path + 'cycle12_y.txt', 'w')
    c13_y = open(file_path + 'cycle13_y.txt', 'w')
    c14_y = open(file_path + 'cycle14_y.txt', 'w')
    c15_y = open(file_path + 'cycle15_y.txt', 'w')
    c16_y = open(file_path + 'cycle16_y.txt', 'w')

    for j in range(1, 15 + 1):
        line = ""
        k = ""
        for item in res_x[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_x.write(k)
            peq_x.write(line)
        if j == 2:
            c2_x.write(line)
        if j == 3:
            c3_x.write(line)
        if j == 4:
            c4_x.write(line)
        if j == 5:
            c5_x.write(line)
        if j == 6:
            c6_x.write(line)
        if j == 7:
            c7_x.write(line)
        if j == 8:
            c8_x.write(line)
        if j == 9:
            c9_x.write(line)
        if j == 10:
            c10_x.write(line)
        if j == 11:
            c11_x.write(line)
        if j == 12:
            c12_x.write(line)
        if j == 13:
            c13_x.write(line)
        if j == 14:
            c14_x.write(line)
        if j == 15:
            c15_x.write(line)
        if j == 16:
            c16_x.write(line)

    for j in range(1, 15 + 1):
        line = ""
        k = ""
        for item in res_y[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_y.write(k)
            peq_y.write(line)
        if j == 2:
            c2_y.write(line)
        if j == 3:
            c3_y.write(line)
        if j == 4:
            c4_y.write(line)
        if j == 5:
            c5_y.write(line)
        if j == 6:
            c6_y.write(line)
        if j == 7:
            c7_y.write(line)
        if j == 8:
            c8_y.write(line)
        if j == 9:
            c9_y.write(line)
        if j == 10:
            c10_y.write(line)
        if j == 11:
            c11_y.write(line)
        if j == 12:
            c12_y.write(line)
        if j == 13:
            c13_y.write(line)
        if j == 14:
            c14_y.write(line)
        if j == 15:
            c15_y.write(line)
        if j == 16:
            c16_y.write(line)

    file.close()

    peq1_x.close()
    peq_x.close()
    c2_x.close()
    c3_x.close()
    c4_x.close()
    c5_x.close()
    c6_x.close()
    c7_x.close()
    c8_x.close()
    c9_x.close()
    c10_x.close()
    c11_x.close()
    c12_x.close()
    c13_x.close()
    c14_x.close()
    c15_x.close()
    c16_x.close()

    peq1_y.close()
    peq_y.close()
    c2_y.close()
    c3_y.close()
    c4_y.close()
    c5_y.close()
    c6_y.close()
    c7_y.close()
    c8_y.close()
    c9_y.close()
    c10_y.close()
    c11_y.close()
    c12_y.close()
    c13_y.close()
    c14_y.close()
    c15_y.close()
    c16_y.close()



def run4():
    α = 1
    x_start = 0.88
    y_start = 0.17
    time_range = range(0, 10000 + 1)
    f = lambda β, σ, x, y: function.__x(α, β, σ, x, y)
    g = lambda β, σ, x, y: function.__y(α, β, σ, x, y)
    # file_path = "C:\\users\\lkora\\desktop\\data12\\"
    file_path = "C:\\users\\lkora\\desktop\\data14\\"

    result_x = dict()
    result_y = dict()

    n = 400 # 400
    dx = (0.5773 - 0.42) / n
    dy = (0.9 - 0) / n

    sx = 0.42
    sy = 0

    x2 = [sx + i * dx for i in range(n + 1)]  # 11
    y2 = [sy + i * dy for i in range(n + 1)]  # 11

    file = open(file_path + "test.txt", 'w')

    rx = x_start
    ry = y_start
    for pair in list(zip(x2, y2)):
        a = pair[0]  # β
        b = pair[1]  # σ

        file.write(str(a) + " " + str(b) + "\n")

        result_x[b] = dict()
        result_y[b] = dict()

        result_x[b][a] = []
        result_y[b][a] = []

        print(a, b)

        x0 = rx
        y0 = ry
        for _ in time_range:
            xt = f(a, b, x0, y0)
            yt = g(a, b, x0, y0)
            if xt < 0 or yt < 0:
                break
            if xt > 1000 or yt > 1000:
                break
            x0 = xt
            y0 = yt
        for t in range(25):
            xt = f(a, b, x0, y0)
            yt = g(a, b, x0, y0)
            if xt < 0 or yt < 0:
                break
            if xt > 1000 or yt > 1000:
                break
            result_x[b][a].append(xt)
            result_y[b][a].append(yt)
            x0 = xt
            y0 = yt

        rx = x0
        ry = y0

        x0 = rx
        y0 = ry
        for x in np.arange(a - 0.0001, 0.3, -0.0001):  # 0.1
            result_x[b][x] = []
            result_y[b][x] = []

            print(x, b)

            for _ in time_range:
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                if xt < 0 or yt < 0:
                    break
                if xt > 1000 or yt > 1000:
                    break
                x0 = xt
                y0 = yt
            for t in range(25):
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                if xt < 0 or yt < 0:
                    break
                if xt > 1000 or yt > 1000:
                    break
                result_x[b][x].append(xt)
                result_y[b][x].append(yt)
                x0 = xt
                y0 = yt

        x0 = rx
        y0 = ry
        for x in np.arange(a + 0.0001, 0.6, 0.0001):  # 0.1
            result_x[b][x] = []
            result_y[b][x] = []

            print(x, b)

            for _ in time_range:
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                if xt < 0 or yt < 0:
                    break
                if xt > 1000 or yt > 1000:
                    break
                x0 = xt
                y0 = yt
            for t in range(25):
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                if xt < 0 or yt < 0:
                    break
                if xt > 1000 or yt > 1000:
                    break
                result_x[b][x].append(xt)
                result_y[b][x].append(yt)
                x0 = xt
                y0 = yt

    res_x = dict()
    res_y = dict()
    for j in range(1, 20 + 1):
        res_x[j] = []
        res_y[j] = []
        for pair in list(zip(x2, y2)):
            a = pair[0]  # x
            b = pair[1]  # y

            data_x = result_x[b][a]
            data_y = result_y[b][a]
            for i in range(len(data_x)):
                data_x[i] = round(data_x[i], 5)
            for i in range(len(data_y)):
                data_y[i] = round(data_y[i], 5)
            # используй set
            di_x = Counter(data_x)
            di_y = Counter(data_y)
            # print(fk, sc, Counter(data))
            if len(di_x.keys()) == j and len(di_y.keys()) == j:
                res_x[j].append([b, a, di_x.keys()])
                res_y[j].append([b, a, di_y.keys()])
                # continue

            for x in np.arange(a - 0.0001, 0.3, -0.0001):  # 0.1
                data_x = result_x[b][x]
                data_y = result_y[b][x]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)
                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([b, x, di_x.keys()])
                    res_y[j].append([b, x, di_y.keys()])
                    continue

            for x in np.arange(a + 0.0001, 0.6, 0.0001):  # 0.1
                data_x = result_x[b][x]
                data_y = result_y[b][x]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)
                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([b, x, di_x.keys()])
                    res_y[j].append([b, x, di_y.keys()])
                    continue

    for j in res_x.keys():
        for i in res_x[j]:
            print(i[0], i[1], set(i[2]))
    for j in res_y.keys():
        for i in res_y[j]:
            print(i[0], i[1], set(i[2]))

    peq_x = open(file_path + "eqX2Gt2X1_x.txt", "w")
    peq1_x = open(file_path + "eqX2Lt2X1_x.txt", 'w')
    c2_x = open(file_path + 'cycle2_x.txt', 'w')
    c2d_x = open(file_path + 'cycle2diagonal_x.txt', 'w')
    c3_x = open(file_path + 'cycle3_x.txt', 'w')
    c4_x = open(file_path + 'cycle4_x.txt', 'w')
    c5_x = open(file_path + 'cycle5_x.txt', 'w')
    c6_x = open(file_path + 'cycle6_x.txt', 'w')
    c7_x = open(file_path + 'cycle7_x.txt', 'w')
    c8_x = open(file_path + 'cycle8_x.txt', 'w')
    c9_x = open(file_path + 'cycle9_x.txt', 'w')
    c11_x = open(file_path + 'cycle11_x.txt', 'w')
    c10_x = open(file_path + 'cycle10_x.txt', 'w')
    c12_x = open(file_path + 'cycle12_x.txt', 'w')
    c13_x = open(file_path + 'cycle13_x.txt', 'w')
    c14_x = open(file_path + 'cycle14_x.txt', 'w')
    c15_x = open(file_path + 'cycle15_x.txt', 'w')
    c16_x = open(file_path + 'cycle16_x.txt', 'w')
    c17_x = open(file_path + 'cycle17_x.txt', 'w')
    c18_x = open(file_path + 'cycle18_x.txt', 'w')
    c19_x = open(file_path + 'cycle19_x.txt', 'w')
    c20_x = open(file_path + 'cycle20_x.txt', 'w')

    peq_y = open(file_path + "eqX2Gt2X1_y.txt", "w")
    peq1_y = open(file_path + "eqX2Lt2X1_y.txt", 'w')
    c2_y = open(file_path + 'cycle2_y.txt', 'w')
    c2d_y = open(file_path + 'cycle2diagonal_y.txt', 'w')
    c3_y = open(file_path + 'cycle3_y.txt', 'w')
    c4_y = open(file_path + 'cycle4_y.txt', 'w')
    c5_y = open(file_path + 'cycle5_y.txt', 'w')
    c6_y = open(file_path + 'cycle6_y.txt', 'w')
    c7_y = open(file_path + 'cycle7_y.txt', 'w')
    c8_y = open(file_path + 'cycle8_y.txt', 'w')
    c9_y = open(file_path + 'cycle9_y.txt', 'w')
    c11_y = open(file_path + 'cycle11_y.txt', 'w')
    c10_y = open(file_path + 'cycle10_y.txt', 'w')
    c12_y = open(file_path + 'cycle12_y.txt', 'w')
    c13_y = open(file_path + 'cycle13_y.txt', 'w')
    c14_y = open(file_path + 'cycle14_y.txt', 'w')
    c15_y = open(file_path + 'cycle15_y.txt', 'w')
    c16_y = open(file_path + 'cycle16_y.txt', 'w')
    c17_y = open(file_path + 'cycle17_y.txt', 'w')
    c18_y = open(file_path + 'cycle18_y.txt', 'w')
    c19_y = open(file_path + 'cycle19_y.txt', 'w')
    c20_y = open(file_path + 'cycle20_y.txt', 'w')

    for j in range(1, 20 + 1):
        line = ""
        k = ""

        for i in range(len(res_x[j])):
        # for item in res_x[j]:
            item = res_x[j][i]
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            if j == 2:
                x = list(res_x[j][i][2])
                y = list(res_y[j][i][2])
                if x == y:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_x.write(k)
            peq_x.write(line)
        if j == 2:
            c2_x.write(line)
            c2d_x.write(k)
        if j == 3:
            c3_x.write(line)
        if j == 4:
            c4_x.write(line)
        if j == 5:
            c5_x.write(line)
        if j == 6:
            c6_x.write(line)
        if j == 7:
            c7_x.write(line)
        if j == 8:
            c8_x.write(line)
        if j == 9:
            c9_x.write(line)
        if j == 10:
            c10_x.write(line)
        if j == 11:
            c11_x.write(line)
        if j == 12:
            c12_x.write(line)
        if j == 13:
            c13_x.write(line)
        if j == 14:
            c14_x.write(line)
        if j == 15:
            c15_x.write(line)
        if j == 16:
            c16_x.write(line)
        if j == 17:
            c17_x.write(line)
        if j == 18:
            c18_x.write(line)
        if j == 19:
            c19_x.write(line)
        if j == 20:
            c20_x.write(line)

    for j in range(1, 20 + 1):
        line = ""
        k = ""
        for item in res_y[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_y.write(k)
            peq_y.write(line)
        if j == 2:
            c2_y.write(line)
        if j == 3:
            c3_y.write(line)
        if j == 4:
            c4_y.write(line)
        if j == 5:
            c5_y.write(line)
        if j == 6:
            c6_y.write(line)
        if j == 7:
            c7_y.write(line)
        if j == 8:
            c8_y.write(line)
        if j == 9:
            c9_y.write(line)
        if j == 10:
            c10_y.write(line)
        if j == 11:
            c11_y.write(line)
        if j == 12:
            c12_y.write(line)
        if j == 13:
            c13_y.write(line)
        if j == 14:
            c14_y.write(line)
        if j == 15:
            c15_y.write(line)
        if j == 16:
            c16_y.write(line)
        if j == 17:
            c17_y.write(line)
        if j == 18:
            c18_y.write(line)
        if j == 19:
            c19_y.write(line)
        if j == 20:
            c20_y.write(line)

    file.close()

    peq1_x.close()
    peq_x.close()
    c2_x.close()
    c3_x.close()
    c4_x.close()
    c5_x.close()
    c6_x.close()
    c7_x.close()
    c8_x.close()
    c9_x.close()
    c10_x.close()
    c11_x.close()
    c12_x.close()
    c13_x.close()
    c14_x.close()
    c15_x.close()
    c16_x.close()
    c17_x.close()
    c18_x.close()
    c19_x.close()
    c20_x.close()

    peq1_y.close()
    peq_y.close()
    c2_y.close()
    c3_y.close()
    c4_y.close()
    c5_y.close()
    c6_y.close()
    c7_y.close()
    c8_y.close()
    c9_y.close()
    c10_y.close()
    c11_y.close()
    c12_y.close()
    c13_y.close()
    c14_y.close()
    c15_y.close()
    c16_y.close()
    c17_y.close()
    c18_y.close()
    c19_y.close()
    c20_y.close()


def run5():
    α = 1
    x_start = 0.88
    # y_start = 0.17
    y_start = 0.88
    time_range = range(0, 10000 + 1)
    f = lambda β, σ, x, y: function.__x(α, β, σ, x, y)
    g = lambda β, σ, x, y: function.__y(α, β, σ, x, y)
    # file_path = "C:\\users\\lkora\\desktop\\data13\\"
    file_path = "C:\\users\\lkora\\desktop\\data14\\"

    shift = 0.01

    result_x = dict()
    result_y = dict()

    n = 1000
    dx = (0.3962 - 0.3962) / n
    dy = (0.5 - 0) / n

    sx = 0.3962
    sy = 0

    x2 = [sx + i * dx for i in range(n + 1)]  # 11
    y2 = [sy + i * dy for i in range(n + 1)]  # 11

    file = open(file_path + "test.txt", 'w')

    rx = x_start + shift
    ry = y_start
    for pair in list(zip(x2, y2)):
        a = pair[0]  # β
        b = pair[1]  # σ

        file.write(str(a) + " " + str(b) + "\n")

        result_x[b] = dict()
        result_y[b] = dict()

        result_x[b][a] = []
        result_y[b][a] = []

        print(a, b)

        x0 = rx + shift
        y0 = ry
        for _ in time_range:
            xt = f(a, b, x0, y0)
            yt = g(a, b, x0, y0)
            if xt < 0 or yt < 0:
                break
            if xt > 1000 or yt > 1000:
                break
            x0 = xt
            y0 = yt
        for t in range(25):
            xt = f(a, b, x0, y0)
            yt = g(a, b, x0, y0)
            if xt < 0 or yt < 0:
                break
            if xt > 1000 or yt > 1000:
                break
            result_x[b][a].append(xt)
            result_y[b][a].append(yt)
            x0 = xt
            y0 = yt

        rx = x0
        ry = y0

        x0 = rx
        y0 = ry
        for x in np.arange(a - 0.001, 0.2, -0.001):  # 0.1
            result_x[b][x] = []
            result_y[b][x] = []

            print(x, b)

            x0 = x0 + shift
            for _ in time_range:
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                if xt < 0 or yt < 0:
                    break
                if xt > 1000 or yt > 1000:
                    break
                x0 = xt
                y0 = yt
            for t in range(25):
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)

                if xt < 0 or yt < 0:
                    break
                if xt > 1000 or yt > 1000:
                    break
                result_x[b][x].append(xt)
                result_y[b][x].append(yt)
                x0 = xt
                y0 = yt

        x0 = rx
        y0 = ry
        for x in np.arange(a + 0.001, 0.46, 0.001):  # 0.1
            result_x[b][x] = []
            result_y[b][x] = []

            print(x, b)

            x0 = x0 + shift
            for _ in time_range:
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)

                if xt < 0 or yt < 0:
                    break
                if xt > 1000 or yt > 1000:
                    break
                x0 = xt
                y0 = yt
            for t in range(25):
                xt = f(x, b, x0, y0)
                yt = g(x, b, x0, y0)
                if xt < 0 or yt < 0:
                    break
                if xt > 1000 or yt > 1000:
                    break
                result_x[b][x].append(xt)
                result_y[b][x].append(yt)
                x0 = xt
                y0 = yt

    res_x = dict()
    res_y = dict()
    for j in range(1, 20 + 1):
        res_x[j] = []
        res_y[j] = []
        for pair in list(zip(x2, y2)):
            a = pair[0]  # x
            b = pair[1]  # y

            data_x = result_x[b][a]
            data_y = result_y[b][a]
            for i in range(len(data_x)):
                data_x[i] = round(data_x[i], 5)
            for i in range(len(data_y)):
                data_y[i] = round(data_y[i], 5)
            # используй set
            di_x = Counter(data_x)
            di_y = Counter(data_y)
            # print(fk, sc, Counter(data))
            if len(di_x.keys()) == j and len(di_y.keys()) == j:
                res_x[j].append([b, a, di_x.keys()])
                res_y[j].append([b, a, di_y.keys()])
                # continue

            for x in np.arange(a - 0.001, 0.2, -0.001):  # 0.1
                data_x = result_x[b][x]
                data_y = result_y[b][x]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)
                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([b, x, di_x.keys()])
                    res_y[j].append([b, x, di_y.keys()])
                    continue

            for x in np.arange(a + 0.001, 0.46, 0.001):  # 0.1
                data_x = result_x[b][x]
                data_y = result_y[b][x]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], 5)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], 5)
                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    res_x[j].append([b, x, di_x.keys()])
                    res_y[j].append([b, x, di_y.keys()])
                    continue

    for j in res_x.keys():
        for i in res_x[j]:
            print(i[0], i[1], set(i[2]))
    for j in res_y.keys():
        for i in res_y[j]:
            print(i[0], i[1], set(i[2]))

    peq_x = open(file_path + "eqX2Gt2X1_x.txt", "w")
    peq1_x = open(file_path + "eqX2Lt2X1_x.txt", 'w')
    c2_x = open(file_path + 'cycle2_x.txt', 'w')
    c2d_x = open(file_path + 'cycle2diagonal_x.txt', 'w')
    c3_x = open(file_path + 'cycle3_x.txt', 'w')
    c4_x = open(file_path + 'cycle4_x.txt', 'w')
    c5_x = open(file_path + 'cycle5_x.txt', 'w')
    c6_x = open(file_path + 'cycle6_x.txt', 'w')
    c7_x = open(file_path + 'cycle7_x.txt', 'w')
    c8_x = open(file_path + 'cycle8_x.txt', 'w')
    c9_x = open(file_path + 'cycle9_x.txt', 'w')
    c11_x = open(file_path + 'cycle11_x.txt', 'w')
    c10_x = open(file_path + 'cycle10_x.txt', 'w')
    c12_x = open(file_path + 'cycle12_x.txt', 'w')
    c13_x = open(file_path + 'cycle13_x.txt', 'w')
    c14_x = open(file_path + 'cycle14_x.txt', 'w')
    c15_x = open(file_path + 'cycle15_x.txt', 'w')
    c16_x = open(file_path + 'cycle16_x.txt', 'w')
    c17_x = open(file_path + 'cycle17_x.txt', 'w')
    c18_x = open(file_path + 'cycle18_x.txt', 'w')
    c19_x = open(file_path + 'cycle19_x.txt', 'w')
    c20_x = open(file_path + 'cycle20_x.txt', 'w')

    peq_y = open(file_path + "eqX2Gt2X1_y.txt", "w")
    peq1_y = open(file_path + "eqX2Lt2X1_y.txt", 'w')
    c2_y = open(file_path + 'cycle2_y.txt', 'w')
    c2d_y = open(file_path + 'cycle2diagonal_y.txt', 'w')
    c3_y = open(file_path + 'cycle3_y.txt', 'w')
    c4_y = open(file_path + 'cycle4_y.txt', 'w')
    c5_y = open(file_path + 'cycle5_y.txt', 'w')
    c6_y = open(file_path + 'cycle6_y.txt', 'w')
    c7_y = open(file_path + 'cycle7_y.txt', 'w')
    c8_y = open(file_path + 'cycle8_y.txt', 'w')
    c9_y = open(file_path + 'cycle9_y.txt', 'w')
    c11_y = open(file_path + 'cycle11_y.txt', 'w')
    c10_y = open(file_path + 'cycle10_y.txt', 'w')
    c12_y = open(file_path + 'cycle12_y.txt', 'w')
    c13_y = open(file_path + 'cycle13_y.txt', 'w')
    c14_y = open(file_path + 'cycle14_y.txt', 'w')
    c15_y = open(file_path + 'cycle15_y.txt', 'w')
    c16_y = open(file_path + 'cycle16_y.txt', 'w')
    c17_y = open(file_path + 'cycle17_y.txt', 'w')
    c18_y = open(file_path + 'cycle18_y.txt', 'w')
    c19_y = open(file_path + 'cycle19_y.txt', 'w')
    c20_y = open(file_path + 'cycle20_y.txt', 'w')

    for j in range(1, 20 + 1):
        line = ""
        k = ""

        for i in range(len(res_x[j])):
        # for item in res_x[j]:
            item = res_x[j][i]
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            if j == 2:
                x = list(res_x[j][i][2])
                y = list(res_y[j][i][2])
                if x == y:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_x.write(k)
            peq_x.write(line)
        if j == 2:
            c2_x.write(line)
            c2d_x.write(k)
        if j == 3:
            c3_x.write(line)
        if j == 4:
            c4_x.write(line)
        if j == 5:
            c5_x.write(line)
        if j == 6:
            c6_x.write(line)
        if j == 7:
            c7_x.write(line)
        if j == 8:
            c8_x.write(line)
        if j == 9:
            c9_x.write(line)
        if j == 10:
            c10_x.write(line)
        if j == 11:
            c11_x.write(line)
        if j == 12:
            c12_x.write(line)
        if j == 13:
            c13_x.write(line)
        if j == 14:
            c14_x.write(line)
        if j == 15:
            c15_x.write(line)
        if j == 16:
            c16_x.write(line)
        if j == 17:
            c17_x.write(line)
        if j == 18:
            c18_x.write(line)
        if j == 19:
            c19_x.write(line)
        if j == 20:
            c20_x.write(line)

    for j in range(1, 20 + 1):
        line = ""
        k = ""
        for item in res_y[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1_y.write(k)
            peq_y.write(line)
        if j == 2:
            c2_y.write(line)
        if j == 3:
            c3_y.write(line)
        if j == 4:
            c4_y.write(line)
        if j == 5:
            c5_y.write(line)
        if j == 6:
            c6_y.write(line)
        if j == 7:
            c7_y.write(line)
        if j == 8:
            c8_y.write(line)
        if j == 9:
            c9_y.write(line)
        if j == 10:
            c10_y.write(line)
        if j == 11:
            c11_y.write(line)
        if j == 12:
            c12_y.write(line)
        if j == 13:
            c13_y.write(line)
        if j == 14:
            c14_y.write(line)
        if j == 15:
            c15_y.write(line)
        if j == 16:
            c16_y.write(line)
        if j == 17:
            c17_y.write(line)
        if j == 18:
            c18_y.write(line)
        if j == 19:
            c19_y.write(line)
        if j == 20:
            c20_y.write(line)

    file.close()

    peq1_x.close()
    peq_x.close()
    c2_x.close()
    c3_x.close()
    c4_x.close()
    c5_x.close()
    c6_x.close()
    c7_x.close()
    c8_x.close()
    c9_x.close()
    c10_x.close()
    c11_x.close()
    c12_x.close()
    c13_x.close()
    c14_x.close()
    c15_x.close()
    c16_x.close()
    c17_x.close()
    c18_x.close()
    c19_x.close()
    c20_x.close()

    peq1_y.close()
    peq_y.close()
    c2_y.close()
    c3_y.close()
    c4_y.close()
    c5_y.close()
    c6_y.close()
    c7_y.close()
    c8_y.close()
    c9_y.close()
    c10_y.close()
    c11_y.close()
    c12_y.close()
    c13_y.close()
    c14_y.close()
    c15_y.close()
    c16_y.close()
    c17_y.close()
    c18_y.close()
    c19_y.close()
    c20_y.close()