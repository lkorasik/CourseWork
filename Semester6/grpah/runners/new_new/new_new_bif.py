import numpy as np

from core.utils.convert_dict_to_lists import convert_dict_to_lists
from core.utils.is_out_of_bounds import is_out_of_bounds
from visual.plotter import Plotter
from visual.values import scale, grid, colors

from models.new_new_model import function, function_stoch


def run0():
    ltr_p_range = np.arange(0.0, 0.1135, 0.0001)
    rtl_p_range = np.arange(0.0, 0.0, 1.0)
    # rtl_p_range = np.arange(0.12, 0.0, -0.0001)
    time_range = range(10000)
    α = 1
    # β = 0.27
    # β = 0.3962
    β = 0.4
    # β = 0.1137
    # x_start = 0.41
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
    values_ltr_x = dict()
    values_ltr_y = dict()

    dx = 0
    dy = 0

    x_0 = x_start
    y_0 = y_start
    for p in ltr_p_range:
        values_ltr_x[p] = []
        values_ltr_y[p] = []

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
        for _ in range(500):
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
            values_ltr_x[p].append(x_t)
            values_ltr_y[p].append(y_t)

    # <-
    values_rtl_x = dict()
    values_rtl_y = dict()

    x_0 = x_start
    y_0 = y_start
    for p in rtl_p_range:
        values_rtl_x[p] = []
        values_rtl_y[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
        for _ in range(500):
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_rtl_x[p].append(x_t)
            values_rtl_y[p].append(y_t)

    source_ltr_x = convert_dict_to_lists(values_ltr_x)
    source_ltr_y = convert_dict_to_lists(values_ltr_y)
    source_rtl_x = convert_dict_to_lists(values_rtl_x)
    source_rtl_y = convert_dict_to_lists(values_rtl_y)

    k = list(zip(source_ltr_x[0], source_ltr_x[1]))
    file = open("C:\\users\\lkora\\desktop\\a.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()
    k = list(zip(source_rtl_x[0], source_rtl_x[1]))
    file = open("C:\\users\\lkora\\desktop\\b.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()

    (Plotter()
     .setup_x_label('$\\sigma')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_ltr_x[0], source_ltr_x[1], '.', colors.steel_blue)
     .scatter(source_rtl_x[0], source_rtl_x[1], '.', colors.orange)
     .show_last())

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear    )
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_y[0], source_ltr_y[1], '.', colors.steel_blue)
    #  # .scatter(source_rtl_y[0], source_rtl_y[1], '.', colors.green)
    #  .show_last())


def run1():
    # p_range0 = np.arange(0.0, 0.27, 0.0001)
    p_range0 = np.arange(0.25, 0.27, 0.00001)
    # p_range1 = np.arange(0.27, 0.331, 0.0001)
    p_range1 = np.arange(0.27, 0.28, 0.00001)
    p_range2 = np.arange(0.27, 0.26, -0.00001)
    # p_range1 = np.arange(0.2, 0.331, 0.001)
    p_range3 = np.arange(0.27, 0.28, 0.00001)
    # p_range3 = np.arange(0.27, 0.331, 0.0001)
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

    # <-
    values_x1 = dict()
    values_y1 = dict()

    dx = 0
    dy = 0

    # x_0 = x_start
    # y_0 = y_start
    for p in p_range1:
        values_x1[p] = []
        values_y1[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
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
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_x1[p].append(x_t)
            values_y1[p].append(y_t)


    values_x2 = dict()
    values_y2 = dict()

    dx = 0
    dy = 0

    # x_0 = x_start
    # y_0 = y_start
    for p in p_range2:
        values_x2[p] = []
        values_y2[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
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
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_x2[p].append(x_t)
            values_y2[p].append(y_t)


    values_x3 = dict()
    values_y3 = dict()

    dx = 0
    dy = 0

    # x_0 = x_start
    # y_0 = y_start
    for p in p_range3:
        values_x3[p] = []
        values_y3[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
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
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_x3[p].append(x_t)
            values_y3[p].append(y_t)


    source_x0 = convert_dict_to_lists(values_x0)
    source_x1 = convert_dict_to_lists(values_x1)
    source_x2 = convert_dict_to_lists(values_x2)
    source_x3 = convert_dict_to_lists(values_x3)

    k = list(zip(source_x0[0], source_x0[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x0.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()
    k = list(zip(source_x1[0], source_x1[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x1.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()
    k = list(zip(source_x2[0], source_x2[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x2.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()
    k = list(zip(source_x3[0], source_x3[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x3.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear)
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_x[0], source_ltr_x[1], '.', colors.steel_blue)
    #  .scatter(source_rtl_x[0], source_rtl_x[1], '.', colors.orange)
    #  .show_last())

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear    )
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_y[0], source_ltr_y[1], '.', colors.steel_blue)
    #  # .scatter(source_rtl_y[0], source_rtl_y[1], '.', colors.green)
    #  .show_last())

def run2():
    p_range0 = np.arange(0.27, 0.27382, 0.00001)
    p_range1 = np.arange(0.27, 0.26684, -0.00001)
    time_range = range(20000)
    build_range = range(500)
    α = 1
    β = 0.445
    x_start = 0.1412
    # x_start = 0.096
    # y_start = 0.4
    y_start = 0.4398
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

    # <-
    values_x1 = dict()
    values_y1 = dict()

    dx = 0
    dy = 0

    x_0 = x_start
    y_0 = y_start
    for p in p_range1:
        values_x1[p] = []
        values_y1[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
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
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_x1[p].append(x_t)
            values_y1[p].append(y_t)

    source_x0 = convert_dict_to_lists(values_x0)
    source_x1 = convert_dict_to_lists(values_x1)

    k = list(zip(source_x0[0], source_x0[1]))
    file = open("C:\\users\\lkora\\desktop\\data3\\x0.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()
    k = list(zip(source_x1[0], source_x1[1]))
    file = open("C:\\users\\lkora\\desktop\\data3\\x1.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear)
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_x[0], source_ltr_x[1], '.', colors.steel_blue)
    #  .scatter(source_rtl_x[0], source_rtl_x[1], '.', colors.orange)
    #  .show_last())

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear    )
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_y[0], source_ltr_y[1], '.', colors.steel_blue)
    #  # .scatter(source_rtl_y[0], source_rtl_y[1], '.', colors.green)
    #  .show_last())

def run3():
    p_range0 = np.arange(0.27, 0.26682, -0.00001) # хвост 6-ки
    # p_range1 = np.arange(0.27, 0.331, 0.0001)
    p_range1 = np.arange(0.27, 0.27382, 0.00001) # каскад 6-ки
    p_range2 = np.arange(0.27, 0.26, -0.0001)
    p_range3 = np.arange(0.27, 0.331, 0.0001)
    time_range = range(20000)
    build_range = range(500)
    α = 1
    β = 0.445
    x_start = 0.88
    # x_start = 0.141206 # 6_1
    # x_start = 0.594167 # 6_2
    y_start = 0.17
    # x_start = 0.474
    # y_start = 0.0788074 # 6_1
    # y_start = 0.274
    f = lambda p, x, y: function.__x(α, β, p, x, y)
    g = lambda p, x, y: function.__y(α, β, p, x, y)

    upper_bound = 1000
    lower_bound = None

    # ->
    values_x0 = dict()
    values_y0 = dict()

    # dx = 0.02
    # dy = 0.03
    dx = 0.0
    dy = 0.0

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

    # <-
    values_x1 = dict()
    values_y1 = dict()

    dx = 0
    dy = 0

    # x_0 = x_start
    # y_0 = y_start
    for p in p_range1:
        values_x1[p] = []
        values_y1[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
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
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_x1[p].append(x_t)
            values_y1[p].append(y_t)


    values_x2 = dict()
    values_y2 = dict()

    dx = 0
    dy = 0

    # x_0 = x_start
    # y_0 = y_start
    for p in p_range2:
        values_x2[p] = []
        values_y2[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
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
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_x2[p].append(x_t)
            values_y2[p].append(y_t)


    values_x3 = dict()
    values_y3 = dict()

    dx = 0
    dy = 0

    # x_0 = x_start
    # y_0 = y_start
    for p in p_range3:
        values_x3[p] = []
        values_y3[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
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
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_x3[p].append(x_t)
            values_y3[p].append(y_t)


    source_x0 = convert_dict_to_lists(values_x0)
    source_x1 = convert_dict_to_lists(values_x1)
    source_x2 = convert_dict_to_lists(values_x2)
    source_x3 = convert_dict_to_lists(values_x3)

    k = list(zip(source_x0[0], source_x0[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x0.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()
    k = list(zip(source_x1[0], source_x1[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x1.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()
    k = list(zip(source_x2[0], source_x2[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x2.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()
    k = list(zip(source_x3[0], source_x3[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x3.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear)
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_x[0], source_ltr_x[1], '.', colors.steel_blue)
    #  .scatter(source_rtl_x[0], source_rtl_x[1], '.', colors.orange)
    #  .show_last())

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear    )
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_y[0], source_ltr_y[1], '.', colors.steel_blue)
    #  # .scatter(source_rtl_y[0], source_rtl_y[1], '.', colors.green)
    #  .show_last())

def run4():
    p_range0 = np.arange(0.27, 0.26682, -0.0001)
    p_range1 = np.arange(0.27, 0.27381, 0.0001)
    time_range = range(20000)
    build_range = range(500)
    α = 1
    β = 0.445
    # x_start = 0.88
    x_start = 0.26798
    # y_start = 0.17
    y_start = 0.323688
    ε = 0.0001
    δ1 = 0
    δ2 = 1
    f = lambda p, x, y, ξ, ξ1t, ξ2t: function_stoch.__x(α, β, p, x, y, ε, δ1, δ2, ξ, ξ1t, ξ2t)
    g = lambda p, x, y, ξ, ξ1t, ξ2t: function_stoch.__y(α, β, p, x, y, ε, δ1, δ2, ξ, ξ1t, ξ2t)

    upper_bound = 1000
    lower_bound = None

    # ->
    values_x0 = dict()
    values_y0 = dict()

    # dx = 0.02
    # dy = 0.03
    dx = 0.0
    dy = 0.0

    x_0 = x_start
    y_0 = y_start
    for p in p_range0:
        values_x0[p] = []
        values_y0[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            ξ = np.random.normal(0, 1)
            ξ1t = np.random.normal(0, 1)
            ξ2t = np.random.normal(0, 1)
            x_t = f(p, x_0, y_0, ξ, ξ1t, ξ2t)
            y_t = g(p, x_0, y_0, ξ, ξ1t, ξ2t)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out high", p)
                break
            x_0 = x_t
            y_0 = y_t
        for _ in build_range:
            ξ = np.random.normal(0, 1)
            ξ1t = np.random.normal(0, 1)
            ξ2t = np.random.normal(0, 1)
            x_t = f(p, x_0, y_0, ξ, ξ1t, ξ2t)
            y_t = g(p, x_0, y_0, ξ, ξ1t, ξ2t)
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

    # <-
    values_x1 = dict()
    values_y1 = dict()

    dx = 0
    dy = 0

    for p in p_range1:
        values_x1[p] = []
        values_y1[p] = []

        x_0 = x_0 + dx
        y_0 = y_0 + dy

        for _ in time_range:
            ξ = np.random.normal(0, 1)
            ξ1t = np.random.normal(0, 1)
            ξ2t = np.random.normal(0, 1)
            x_t = f(p, x_0, y_0, ξ, ξ1t, ξ2t)
            y_t = g(p, x_0, y_0, ξ, ξ1t, ξ2t)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
        for _ in build_range:
            ξ = np.random.normal(0, 1)
            ξ1t = np.random.normal(0, 1)
            ξ2t = np.random.normal(0, 1)
            x_t = f(p, x_0, y_0, ξ, ξ1t, ξ2t)
            y_t = g(p, x_0, y_0, ξ, ξ1t, ξ2t)
            if x_t < 0 or y_t < 0:
                print("out low", p)
                break
            if x_t > 1000 or y_t > 1000:
                print("out hight", p)
                break
            x_0 = x_t
            y_0 = y_t
            values_x1[p].append(x_t)
            values_y1[p].append(y_t)

    source_x0 = convert_dict_to_lists(values_x0)
    source_x1 = convert_dict_to_lists(values_x1)

    k = list(zip(source_x0[0], source_x0[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x0.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()
    k = list(zip(source_x1[0], source_x1[1]))
    file = open("C:\\users\\lkora\\desktop\\data2\\x1.txt", "w")
    for item in k:
        line = str(item[0]) + " " + str(item[1]) + "\n"
        file.write(line)
    file.close()

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear)
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_x[0], source_ltr_x[1], '.', colors.steel_blue)
    #  .scatter(source_rtl_x[0], source_rtl_x[1], '.', colors.orange)
    #  .show_last())

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear    )
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_y[0], source_ltr_y[1], '.', colors.steel_blue)
    #  # .scatter(source_rtl_y[0], source_rtl_y[1], '.', colors.green)
    #  .show_last())