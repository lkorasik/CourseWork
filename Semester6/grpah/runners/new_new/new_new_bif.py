import numpy as np

from core.utils.convert_dict_to_lists import convert_dict_to_lists
from core.utils.is_out_of_bounds import is_out_of_bounds
from visual.plotter import Plotter
from visual.values import scale, grid, colors

from models.new_new_model import function

def run0():
    ltr_p_range = np.arange(0.2, 0.3, 0.0001)
    # ltr_p_range = np.arange(0.3, 0.27, 0.0001)
    rtl_p_range = np.arange(0.3, 0.2, -0.0001)
    time_range = range(10000)
    α = 1
    # β = 0.27
    # β = 0.3962
    β = 0.445
    # β = 0.1137
    # x_start = 0.41
    x_start = 0.41
    # x_start = 0.096
    # y_start = 0.4
    y_start = 0.4
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
     # .scatter(source_rtl_x[0], source_rtl_x[1], '.', colors.green)
     .show())

    # (Plotter()
    #  .setup_x_label('$\\sigma')
    #  .setup_y_label('x')
    #  .setup_y_scale(scale.linear    )
    #  .setup_grid(grid.major)
    #  .setup_title('Bifurcation')
    #  .scatter(source_ltr_y[0], source_ltr_y[1], '.', colors.steel_blue)
    #  # .scatter(source_rtl_y[0], source_rtl_y[1], '.', colors.green)
    #  .show_last())