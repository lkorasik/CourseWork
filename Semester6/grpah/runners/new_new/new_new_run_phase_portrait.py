from core.algorithms.time_series import time_series
from models.new_new_model import function
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
    β = 0.44
    σ = 0.44

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 100000 + 1),
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
         .scatter(x, y, markers.point, colors.steel_blue)
         .show_last())