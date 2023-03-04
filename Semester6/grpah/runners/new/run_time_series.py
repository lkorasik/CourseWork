from models.new_model import function
from visual.plotter import Plotter
from visual.values import scale, grid, markers, colors
from core.algorithms.new.time_series import time_series


def run_2_cycle_0():
    α = 1
    β = 0.4
    γ = 0.1

    time_range = range(1, 100 + 1)
    source = time_series(
        skip_range=range(1, 10000 + 1),
        time_range=time_range,
        x_start=[0.2, 0.2],
        f=lambda x: function.f(α, β, γ, x[0], x[1]),
        skip=False
    )

    time = list(map(lambda x: x[0], source))
    values0 = list(map(lambda x: x[1][0], source))
    values1 = list(map(lambda x: x[1][1], source))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot(time, values0, markers.point, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot(time, values1, markers.point, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter(values0, values1, markers.point, colors.steel_blue)
     .show_last())


def run_2_cycle_1():
    α = 1
    β = 0.4
    γ = 0.2

    time_range = range(1, 100 + 1)
    source = time_series(
        skip_range=range(1, 10000 + 1),
        time_range=time_range,
        x_start=[0.2, 0.2],
        f=lambda x: function.f(α, β, γ, x[0], x[1]),
        skip=False
    )

    time = list(map(lambda x: x[0], source))
    values0 = list(map(lambda x: x[1][0], source))
    values1 = list(map(lambda x: x[1][1], source))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot(time, values0, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot(time, values1, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter(values0, values1, markers.point, colors.steel_blue)
     .show_last())


def run_2_cycle_2():
    α = 1
    β = 0.4
    γ = 0.25

    time_range = range(1, 100 + 1)
    source = time_series(
        skip_range=range(1, 10000 + 1),
        time_range=time_range,
        x_start=[0.2, 0.2],
        f=lambda x: function.f(α, β, γ, x[0], x[1]),
        skip=True
    )

    time = list(map(lambda x: x[0], source))
    values0 = list(map(lambda x: x[1][0], source))
    values1 = list(map(lambda x: x[1][1], source))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot(time, values0, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot(time, values1, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter(values0, values1, markers.point, colors.steel_blue)
     .show_last())


def run_2_cycle_3():
    α = 1
    β = 0.4
    γ = 0.7

    source = time_series(
        skip_range=range(1, 10000 + 1),
        time_range=range(1, 10000 + 1),
        x_start=[0.2, 0.2],
        f=lambda x: function.f(α, β, γ, x[0], x[1]),
        skip=True
    )

    time = list(map(lambda x: x[0], source))
    values0 = list(map(lambda x: x[1][0], source))
    values1 = list(map(lambda x: x[1][1], source))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot(time, values0, markers.point, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot(time, values1, markers.point, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter(values0, values1, markers.point, colors.steel_blue)
     .show_last())


def run_2_cycle_4():
    α = 1
    β = 0.4
    γ = 0.805

    time_range = range(1, 100 + 1)
    source = time_series(
        skip_range=time_range,
        time_range=time_range,
        x_start=[0.2, 0.2],
        f=lambda x: function.f(α, β, γ, x[0], x[1]),
        skip=False
    )

    time = list(map(lambda x: x[0], source))
    values0 = list(map(lambda x: x[1][0], source))
    values1 = list(map(lambda x: x[1][1], source))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot(time, values0, markers.point, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot(time, values1, markers.point, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter(values0, values1, markers.point, colors.steel_blue)
     .show_last())
