from collections import Counter


def new_regime_map(x_start, y_start, a_range, ra_range, b_range, time_range, f, g, file_path):
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