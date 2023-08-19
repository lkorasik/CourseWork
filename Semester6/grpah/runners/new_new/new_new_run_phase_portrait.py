import numpy as np

from core.algorithms.time_series import time_series
from core.utils.new_is_out_of_bounds import new_is_out_of_bounds
from models.new_new_model import function, function_stoch
from visual.plotter import Plotter
from visual.values import scale, grid, markers, colors


def run0():
    α = 1
    # β = 0.5
    β = 0.5
    # σ = 0
    σ = 0.3

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 100000 + 1),
        # x_start=[0.2, 0.3],
        x_start=[0.88, 0.17],
        f=lambda x: function.f(α, β, σ, x[0], x[1]),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.star, colors.steel_blue)
         .show_last())


def run1():
    α = 1
    β = 0.5
    σ = 0.5

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 100000 + 1),
        x_start=[0.2, 0.3],
        f=lambda x: function.f(α, β, σ, x[0], x[1]),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())


def run2():
    α = 1
    β = 0.5
    σ = 0.4

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 100000 + 1),
        x_start=[0.2, 0.3],
        f=lambda x: function.f(α, β, σ, x[0], x[1]),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())


def run3():
    α = 1
    β = 0.5
    σ = 0.48

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 100000 + 1),
        x_start=[0.2, 0.3],
        f=lambda x: function.f(α, β, σ, x[0], x[1]),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())


def run4():
    α = 1
    β = 0.5
    σ = 0.625

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 100000 + 1),
        x_start=[0.2, 0.3],
        f=lambda x: function.f(α, β, σ, x[0], x[1]),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))


    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())


def run6():
    α = 1
    β = 0.38
    σ = 0.25

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 100000 + 1),
        x_start=[1.0, 0.85],
        f=lambda x: function.f(α, β, σ, x[0], x[1]),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())


def run7():
    α = 1
    β = 0.4
    σ = 0.4

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 100000 + 1),
        x_start=[0.3, 0.2],
        f=lambda x: function.f(α, β, σ, x[0], x[1]),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())


def run8():
    α = 1
    β = 0.4
    σ = 0.2715

    line = time_series(
        skip_range=range(20000),
        time_range=range(1, 6 + 1),
        # x_start=[0.2, 0.5725],
        x_start=[0.88, 0.17],
        f=lambda x: function.f(α, β, σ, x[0], x[1]),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    print(x)
    print(y)

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())


def run9():
    α = 1
    # β = 0.4
    β = 0.445
    # σ = 0.0966
    σ = 0.27

    line = time_series(
        skip_range=range(20000),
        time_range=range(1, 11),
        x_start=[0.502, 0.709],
        # x_start=[0.322473, 0.571993],
        f=lambda x: function.f(α, β, σ, x[0], x[1]),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=0
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    print(x)
    print(y)

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())


def run10():
    α = 1.0
    β = 0.445
    σ = 0.27
    ε = 0.001
    # ε = 0.0005
    # ε = 0.0002
    # additive
    δ1 = 0
    δ2 = 1
    # parametric
    # δ1 = 1
    # δ2 = 0

    # x = [0.420583, 0.420583]

    # x = [0.179239, 0.857367]
    # x = [0.179239, 0.857367]
    # y = [0.179239, 0.857367]
    # y = [0.857367, 0.179239]

    # 6.1
    x = [0.5719927893810252, 0.22834498152534183, 0.6533768799336029, 0.12037751048988818, 0.5941670677042235, 0.14120570444488975]
    y = [0.32247291303079295, 0.5762418829073082, 0.19877809003468694, 0.6777760394303515, 0.07880744084981842, 0.43982704889612767]

    # 6.2
    # x = [0.6777760394303517, 0.07880744084981736, 0.4398270488961216, 0.3224729130307987, 0.5762418829073052, 0.1987780900346871]
    # y = [0.120377510489885, 0.5941670677042156, 0.1412057044448971, 0.5719927893810377, 0.22834498152533095, 0.653376879933606]

    # 10
    # x = [0.6363902563591886, 0.10844281002339379, 0.5221381325173345, 0.2506827382623543, 0.6599765764088453, 0.10006111821309613, 0.5266295824777721, 0.2167039349062764, 0.641904368425501, 0.1442853518016976]
    # y = [0.1000611182130943, 0.5266295824777656, 0.21670393490628337, 0.6419043684255001, 0.14428535180169838, 0.6363902563591907, 0.10844281002339257, 0.5221381325173328, 0.25068273826235443, 0.6599765764088449]

    # skip_range=range(20000)
    skip_range=range(1)
    time_range=range(1, 5000 + 1)
    x_start=[x[0], y[0]]
    # x_start=[0.22, 0.525]
    f=lambda x: function_stoch.f(α, β, β, σ, x[0], x[1], ε, δ1, δ2)
    check_bounds=False
    upper_bounds=10_000
    lower_bounds=0

    line = []

    x_i = x_start
    for _ in skip_range:
        x_t = f(x_i)
        if x_t[0] > 1000 or x_t[1] > 1000:
            break
        if x_t[0] <= 0:
            x_t[0] = 0
        if x_t[1] <= 0:
            x_t[1] = 0
        x_i = x_t
    for t in time_range:
        x_t = f(x_i)
        if x_t[0] > 1000 or x_t[1] > 1000:
            break
        if x_t[0] <= 0:
            x_t[0] = 0
        if x_t[1] <= 0:
            x_t[1] = 0
        x_i = x_t
        line.append([t, x_i])

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    file = open("C:\\users\\lkora\\desktop\\dd\\a.txt", 'w')
    for i in range(len(x)):
        file.write(str(x[i]) + " " + str(y[i]) + "\n")
    file.close()

    print(x)
    print(y)

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())

def run11():
    α = 1.0
    β = 0.445
    σ = 0.02
    # ε = 0.057877868652343754
    # additive
    δ1 = 0
    δ2 = 1
    # parametric
    # δ1 = 1
    # δ2 = 0

    result = dict()
    for ε in np.arange(0, 0.1, 0.001):
        print(ε)

        x = [0.420583, 0.420583]

        x = [0.588023, 0.250809]
        y = [0.250809, 0.588023]

        skip_range=range(10000)
        time_range=range(1, 5000 + 1)
        x_start=[0.85604, 0.158732]
        # x_start=[0.420583, 0.420583]
        f=lambda x: function_stoch.f(α, β, β, σ, x[0], x[1], ε, δ1, δ2)
        check_bounds=False
        upper_bounds=10_000
        lower_bounds=0

        for i in range(100):
            line = []

            x_i = x_start
            for _ in skip_range:
                x_t = f(x_i)
                if x_t[0] > 1000 or x_t[1] > 1000:
                    break
                if x_t[0] <= 0:
                    x_t[0] = 0
                if x_t[1] <= 0:
                    x_t[1] = 0
                x_i = x_t
            for t in time_range:
                x_t = f(x_i)
                if x_t[0] > 1000 or x_t[1] > 1000:
                    break
                if x_t[0] <= 0:
                    x_t[0] = 0
                if x_t[1] <= 0:
                    x_t[1] = 0
                x_i = x_t
                line.append([t, x_i])

            x = list(map(lambda x: x[1][0], line))
            y = list(map(lambda x: x[1][1], line))

            if ε in result.keys():
                result[ε].append((x, y))
            else:
                result[ε] = [(x, y)]

    r = dict()
    for ε in result.keys():
        common = len(result[ε])
        out_x = 0
        out_y = 0

        values = result[ε]
        for pair in values:
            x = pair[0]
            y = pair[1]

            if 0 in x:
                out_x += 1
            if 0 in y:
                out_y += 1

        r[ε] = (out_x / common, out_y / common)

    print("S")

    with open("C:\\users\\lkora\\desktop\\pro.txt", 'w') as file:
        line = ""
        for k in r.keys():
            line += str(k) + " " + str(r[k][0]) + " " + str(r[k][1]) + "\n"

        file.write(line)


        # file = open("C:\\users\\lkora\\desktop\\t\\a" + str(ε) + ".txt", 'w')
        # for i in range(len(x)):
        #     file.write(str(x[i]) + " " + str(y[i]) + "\n")
        # file.close()

        # print(x)
        # print(y)
