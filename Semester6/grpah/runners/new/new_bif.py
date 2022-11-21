import numpy as np

from algorithms.bifurcation_with_equilibrium import bifurcation_with_equilibrium
from core.algorithms.old.single_newton import single_newton
from core.utils.convert_dict_to_lists import convert_dict_to_lists
from core.utils.is_out_of_bounds import is_out_of_bounds
from models.new_model import function
from visual.line import Line
from visual.plotter import Plotter
from visual.values import grid, scale, colors, markers


def run1():
    skip_range = range(1, 10000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.2
    y_start = 0.2
    α = 1
    β = 0.4
    p_range = np.arange(0, 1.3, 0.001)

    f = lambda p, x, y: function.__x(α, β, p, x, y)
    g = lambda p, x, y: function.__y(α, β, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = 1e-5

    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        x_0 = x_start
        y_0 = y_start
        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\2x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\2y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run2():
    skip_range = range(1, 10000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.2
    y_start = 0.2
    a = 1
    b = 0.4
    p_range = np.arange(0, 1.3, 0.001)

    f = lambda p, x, y: function.__x(a, b, p, x, y)
    g = lambda p, x, y: function.__y(a, b, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = 1e-5

    x_0 = x_start
    y_0 = y_start
    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\4x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\4y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run3():
    skip_range = range(1, 10000 + 1)
    time_range = range(1, 10000 + 1)
    x_start = 0.2
    y_start = 0.2
    a = 1
    b = 0.4
    p_range = np.arange(0, 1, 0.001)

    f = lambda p, x, y: function.__x(a, b, p, x, y)
    g = lambda p, x, y: function.__y(a, b, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = 1e-5

    x_0 = x_start
    y_0 = y_start
    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\4x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\4y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run_la():
    skip_range = range(1, 10000 + 1)
    time_range = range(1, 1000 + 1)
    # x_start = 0.193434
    x_start = 0.2
    # y_start = 0.267755
    y_start = 0.2
    a = 1
    b = 0.4
    p_range = np.arange(0.826, 1, 0.0001)
    rp_range = np.arange(0.826, 0.6, -0.0001)

    f = lambda p, x, y: function.__x(a, b, p, x, y)
    g = lambda p, x, y: function.__y(a, b, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = -1e-5

    x_0 = x_start
    y_0 = y_start
    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

        x_0 = x_start
        y_0 = y_start
    for p in rp_range:
        values_x[p] = []
        values_y[p] = []

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\2x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\2y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run4():
    skip_range = range(1, 10000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.2
    y_start = 0.2
    α = 1
    β = 0.4
    p_range = np.arange(0, 1.3, 0.001)

    f = lambda p, x, y: function.__x(α, β, p, x, y)
    g = lambda p, x, y: function.__y(α, β, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = 1e-5

    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        x_0 = x_start
        y_0 = y_start
        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(y_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(y_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\2x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\2y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run_combine():
    skip_range = range(1, 10000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.2
    y_start = 0.2
    a = 1
    b = 0.4
    p_range1 = np.arange(0, 0.6, 0.001)
    p_range2 = np.arange(0.6, 1, 0.0001)
    p_range3 = np.arange(1, 1.3, 0.001)

    f = lambda p, x, y: function.__x(a, b, p, x, y)
    g = lambda p, x, y: function.__y(a, b, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = -1e-5

    # x_0 = x_start
    # y_0 = y_start
    for p in p_range1:
        values_x[p] = []
        values_y[p] = []

        x_0 = x_start
        y_0 = y_start

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    for p in p_range2:
        values_x[p] = []
        values_y[p] = []

        x_0 = x_start
        y_0 = y_start

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    for p in p_range3:
        values_x[p] = []
        values_y[p] = []

        x_0 = x_start
        y_0 = y_start

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\2x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\2y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run_bif_with_equilibrium():
    skip_range = range(1, 1000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.2
    y_start = 0.2
    a = 1
    b = 0.4
    p_range1 = np.arange(0, 1.3, 0.001)

    f = lambda p, x, y: function.__x(a, b, p, x, y)
    g = lambda p, x, y: function.__y(a, b, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = -1e-5

    # x_0 = x_start
    # y_0 = y_start
    for p in p_range1:
        values_x[p] = []
        values_y[p] = []

        x_0 = x_start
        y_0 = y_start

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            # if is_out_of_bounds(x_t, upper_bound, lower_bound):
            #     break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\2x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\2y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    line1 = Line()
    x = 0.1
    for g in p_range1:
        x = single_newton(x, 0.0001, lambda x_: (g * x + 1) * (b + x) ** 6 - a * x, lambda x_: -a + g * (b + x) ** 6 + 6 * (b + x) ** 5 * (1 + g * x))
        line1.add(b, x)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .plot_line(line1, ',', colors.red)
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())
