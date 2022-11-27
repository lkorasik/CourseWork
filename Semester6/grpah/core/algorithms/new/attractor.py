from collections import Counter


def area_of_attractor(file_path, x_range, y_range, time_range, cycle, f, g, fc, gc, x_start, y_start):
    # result_x = dict()
    # result_y = dict()
    # for x in x_range:
    #     result_x[x] = dict()
    #     result_y[x] = dict()
    #     for y in y_range:
    #         result_x[x][y] = []
    #         result_y[x][y] = []
    #         x0 = x
    #         y0 = y
    #         for _ in time_range:
    #             xt = f(x0, y0)
    #             yt = g(x0, y0)
    #             x0 = xt
    #             y0 = yt
    #         for t in range(cycle):
    #             xt = f(x0, y0)
    #             yt = g(x0, y0)
    #             result_x[x][y].append(xt)
    #             result_y[x][y].append(yt)
    #             x0 = xt
    #             y0 = yt

    p = 0.14
    values_x = []
    values_y = []

    x_0 = x_start
    y_0 = y_start
    for _ in time_range:
        x_t = f(p, x_0, y_0)
        y_t = g(p, x_0, y_0)
        # if is_out_of_bounds(x_t, upper_bound, lower_bound):
        #     break
        # if is_out_of_bounds(x_t, upper_bound, lower_bound):
        #     break
        x_0 = x_t
        y_0 = y_t
    for _ in range(cycle):
        x_t = f(p, x_0, y_0)
        y_t = g(p, x_0, y_0)
        # if is_out_of_bounds(x_t, upper_bound, lower_bound):
        #     break
        # if is_out_of_bounds(x_t, upper_bound, lower_bound):
        #     break
        x_0 = x_t
        y_0 = y_t
        values_x.append(x_t)
        values_y.append(y_t)

    points = open(file_path + "points.txt", "w")
    line = ""
    for i in range(len(values_x)):
        line += str(values_x[i]) + " " + str(values_y[i]) + "\n"
    points.write(line)
    points.close()

    # print("data collected")
    #
    # res_x = dict()
    # res_y = dict()
    # for j in range(1, cycle + 1):
    #     res_x[j] = []
    #     res_y[j] = []
    #     for x in x_range:
    #         for y in y_range:
    #             data_x = result_x[x][y]
    #             data_y = result_y[x][y]
    #             for i in range(len(data_x)):
    #                 data_x[i] = round(data_x[i], 3)
    #             for i in range(len(data_y)):
    #                 data_y[i] = round(data_y[i], 3)
    #
    #             # используй set
    #             di_x = Counter(data_x)
    #             di_y = Counter(data_y)
    #             # print(fk, sc, Counter(data))
    #             # можно забить на это условие?
    #             if len(di_x.keys()) == j and len(di_y.keys()) == j:
    #                 res_x[j].append([x, y, di_x.keys()])
    #                 res_y[j].append([x, y, di_y.keys()])
    #                 continue
    #
    # for j in res_x.keys():
    #     for i in res_x[j]:
    #         print(i[0], i[1], set(i[2]))
    # for j in res_y.keys():
    #     for i in res_y[j]:
    #         print(i[0], i[1], set(i[2]))
    #
    # infty_x = open(file_path + "infty_y.txt", "w")
    # zero_x = open(file_path + "zero_y.txt", 'w')
    # others_x = open(file_path + 'others_y.txt', 'w')
    #
    # infty_y = open(file_path + "infty_x.txt", "w")
    # zero_y = open(file_path + "zero_x.txt", 'w')
    # others_y = open(file_path + 'others_x.txt', 'w')
    #
    # for j in range(1, cycle + 1):
    #     line = ""
    #     k = ""
    #     for item in res_x[j]:
    #         a = item[0]
    #         b = item[1]
    #
    #         if j == 1:
    #             if list(item[2]) == [0.0]:
    #                 k += str(a) + " " + str(b) + "\n"
    #             else:
    #                 line += str(a) + " " + str(b) + "\n"
    #         else:
    #             line += str(a) + " " + str(b) + "\n"
    #
    #     if j == 1:
    #         zero_x.write(k)
    #         infty_x.write(line)
    #     if j == cycle:
    #         others_x.write(line)
    #
    # for j in range(1, cycle + 1):
    #     line = ""
    #     k = ""
    #     for item in res_y[j]:
    #         a = item[0]
    #         b = item[1]
    #
    #         if j == 1:
    #             if list(item[2]) == [0.0]:
    #                 k += str(a) + " " + str(b) + "\n"
    #             else:
    #                 line += str(a) + " " + str(b) + "\n"
    #         else:
    #             line += str(a) + " " + str(b) + "\n"
    #
    #     if j == 1:
    #         zero_y.write(k)
    #         infty_y.write(line)
    #     if j == cycle:
    #         others_y.write(line)
    #
    # zero_x.close()
    # infty_x.close()
    # others_x.close()
    #
    # zero_y.close()
    # infty_y.close()
    # others_y.close()

# пропускаем
# делаем 2 или 3 итерации
# запоминаем 2 или 3 точки
# перебираем точки из плоскости, итерируемся и проверяем на ноль, двойку/тройку и бесконечноть
# Строим график x-y
