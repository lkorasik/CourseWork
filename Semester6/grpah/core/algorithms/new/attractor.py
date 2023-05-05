from collections import Counter


def basin_of_attractor(file_path, x_range, y_range, time_range, f, g, R):
    result_x = dict()
    result_y = dict()

    neg_x = list()
    neg_y = list()
    over_x = list()
    over_y = list()

    cycle6_variants = []

    for x in x_range:
        x = round(x, R)
        result_x[x] = dict()
        result_y[x] = dict()
        for y in y_range:
            y = round(y, R)
            print(x, y)
            result_x[x][y] = []
            result_y[x][y] = []

            x0 = x
            y0 = y
            for _ in time_range:
                xt = f(x0, y0)
                yt = g(x0, y0)
                if xt < 0 or yt < 0:
                    print("low1")
                    break
                if xt > 1000 or yt > 1000:
                    print("high1")
                    break
                x0 = xt
                y0 = yt
            for t in range(20):
                xt = f(x0, y0)
                yt = g(x0, y0)
                if xt < 0 or yt < 0:
                    print("low2")
                    neg_x.append(x)
                    neg_y.append(y)
                    break
                if xt > 1000 or yt > 1000:
                    print("high2")
                    over_x.append(x)
                    over_y.append(y)
                    break
                result_x[x][y].append(xt)
                result_y[x][y].append(yt)
                x0 = xt
                y0 = yt

    print("data collected")

    res_x = dict()
    res_y = dict()
    for j in range(1, 10 + 1):
        res_x[j] = []
        res_y[j] = []
        for x in x_range:
            x = round(x, R)
            for y in y_range:
                y = round(y, R)
                print(j, x, y)
                data_x = result_x[x][y]
                data_y = result_y[x][y]
                for i in range(len(data_x)):
                    data_x[i] = round(data_x[i], R)
                for i in range(len(data_y)):
                    data_y[i] = round(data_y[i], R)

                # используй set
                di_x = Counter(data_x)
                di_y = Counter(data_y)
                # print(fk, sc, Counter(data))
                if len(di_x.keys()) == j and len(di_y.keys()) == j:
                    if j == 6:
                        values = list(zip(list(di_x.keys()), list(di_y.keys())))
                        if values not in cycle6_variants:
                            # todo: запутить просчет
                            result_temp = []
                            x0 = list(di_x.keys())[0]
                            y0 = list(di_y.keys())[0]
                            for _ in time_range:
                                xt = f(x0, y0)
                                yt = g(x0, y0)
                                if xt < 0 or yt < 0:
                                    break
                                if xt > 1000 or yt > 1000:
                                    break
                                x0 = xt
                                y0 = yt
                            for t in range(20):
                                xt = f(x0, y0)
                                yt = g(x0, y0)
                                if xt < 0 or yt < 0:
                                    break
                                if xt > 1000 or yt > 1000:
                                    break
                                result_temp.append((round(xt, R), round(yt, R)))
                                x0 = xt
                                y0 = yt
                            result_temp = list(set(result_temp))
                            cycle6_variants.append(result_temp)
                    res_x[j].append([x, y, di_x.keys()])
                    res_y[j].append([x, y, di_y.keys()])
                    continue

    s = []
    for item in cycle6_variants:
        if item not in s:
            s.append(item)
    cycle6_variants = s

    other = open(file_path + "others_x.txt", 'w')
    for x in x_range:
        x = round(x, R)
        for y in y_range:
            y = round(y, R)
            data_x = result_x[x][y]
            data_y = result_y[x][y]
            for i in range(len(data_x)):
                data_x[i] = round(data_x[i], R)
            for i in range(len(data_y)):
                data_y[i] = round(data_y[i], R)

            # используй set
            di_x = Counter(data_x)
            di_y = Counter(data_y)
            # print(fk, sc, Counter(data))
            if len(di_x.keys()) > 10 or len(di_y.keys()) > 10:
                other.write(str(x) + " " + str(y) + "\n")
    other.close()

    # todo: надо разделить двойки

    for j in res_x.keys():
        for i in res_x[j]:
            print(i[0], i[1], set(i[2]))
    for j in res_y.keys():
        for i in res_y[j]:
            print(i[0], i[1], set(i[2]))

    infinity_x = open(file_path + "infty_x.txt", 'w')
    zero_x = open(file_path + "zero_x.txt", 'w')
    eq_x = open(file_path + "eq_x.txt", 'w')
    cycle2_x = open(file_path + "cycle2_x.txt", 'w')
    cycle2d_x = open(file_path + "cycle2d_x.txt", 'w')
    cycle3_x = open(file_path + 'cycle3_x.txt', 'w')
    cycle4_x = open(file_path + 'cycle4_x.txt', 'w')
    cycle5_x = open(file_path + 'cycle5_x.txt', 'w')
    # cycle6_x = open(file_path + 'cycle6_x.txt', 'w')
    cycle6_1_x = open(file_path + 'cycle6_1_x.txt', 'w')
    cycle6_2_x = open(file_path + 'cycle6_2_x.txt', 'w')
    cycle6 = [cycle6_1_x, cycle6_2_x]
    cycle7_x = open(file_path + 'cycle7_x.txt', 'w')
    cycle8_x = open(file_path + 'cycle8_x.txt', 'w')
    cycle9_x = open(file_path + "cycle9_x.txt", 'w')
    cycle10_x = open(file_path + "cycle10_x.txt", 'w')
    # others_x = open(file_path + "others_x.txt", 'w')
    negative_x = open(file_path + "negative.txt", 'w')
    overload_x = open(file_path + "overload.txt", 'w')

    infinity_y = open(file_path + "infty_y.txt", 'w')
    zero_y = open(file_path + "zero_y.txt", 'w')
    others_y = open(file_path + "others_y.txt", 'w')

    line = ""
    for i in range(len(neg_x)):
        line += str(neg_x[i]) + " " + str(neg_y[i]) + "\n"
    negative_x.write(line)

    line = ""
    for i in range(len(over_x)):
        line += str(over_x[i]) + " " + str(over_y[i]) + "\n"
    overload_x.write(line)

    for j in range(1, 10 + 1):
        zero = ""
        line = ""
        diag = ""
        c6_1 = ""
        c6_2 = ""
        c6 = [c6_1, c6_2]
        for i in range(len(res_x[j])):
            item = res_x[j][i]
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    zero += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            elif j == 2:
                lst_x = list(item[2])
                lst_y = list(res_y[j][i][2])
                if lst_x[0] == lst_y[0]:
                    diag += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            elif j == 6:
                print("AAA")
                cycle = list(zip(list(item[2]), list(res_y[j][i][2])))
                index = cycle6_variants.index(cycle)
                line = c6[index]
                line += str(a) + " " + str(b) + "\n"
                c6[index] = line
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            zero_x.write(zero)
            eq_x.write(line)
        if j == 2:
            cycle2d_x.write(diag)
            cycle2_x.write(line)
        if j == 3:
            cycle3_x.write(line)
        if j == 4:
            cycle4_x.write(line)
        if j == 5:
            cycle5_x.write(line)
        if j == 6:
            cycle6_1_x.write(c6[0])
            cycle6_2_x.write(c6[1])
            # cycle6_x.write(line)
        if j == 7:
            cycle7_x.write(line)
        if j == 8:
            cycle8_x.write(line)
        if j == 9:
            cycle9_x.write(line)
        if j == 10:
            cycle10_x.write(line)

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
            zero_y.write(k)

    infinity_x.close()
    zero_x.close()
    # others_x.close()

    cycle2_x.close()
    cycle3_x.close()
    cycle4_x.close()
    cycle5_x.close()
    # cycle6_x.close()
    cycle6_1_x.close()
    cycle6_2_x.close()
    cycle7_x.close()
    cycle8_x.close()
    cycle9_x.close()
    cycle10_x.close()
    negative_x.close()
    overload_x.close()

    infinity_y.close()
    zero_y.close()
    others_y.close()

# пропускаем
# делаем 2 или 3 итерации
# запоминаем 2 или 3 точки
# перебираем точки из плоскости, итерируемся и проверяем на ноль, двойку/тройку и бесконечноть
# Строим график x-y
