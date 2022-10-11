from core.algorithms.old.time_series import time_series
from models.new_model import function
from visual.line import Line
from visual.plotter import Plotter
from visual.values import scale, grid, markers, colors


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

    y = source.y

    y1 = Line()
    y2 = Line()
    y1.x = source.x
    y2.x = source.x
    for item in y:
        y1.add_y(item[0])
        y2.add_y(item[1])

    y3 = Line()
    y3.x = y1.y
    y3.y = y2.y

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot_line(y1, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot_line(y2, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter_line(y3, markers.point, colors.steel_blue).show_last())
     # .plot_line(y3, markers.point, colors.steel_blue).show_last())


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

    y = source.y

    y1 = Line()
    y2 = Line()
    y1.x = source.x
    y2.x = source.x
    for item in y:
        y1.add_y(item[0])
        y2.add_y(item[1])

    y3 = Line()
    y3.x = y1.y
    y3.y = y2.y

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot_line(y1, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot_line(y2, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter_line(y3, markers.point, colors.steel_blue).show_last())
     # .plot_line(y3, markers.point, colors.steel_blue).show_last())


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

    y = source.y

    y1 = Line()
    y2 = Line()
    y1.x = source.x
    y2.x = source.x
    for item in y:
        y1.add_y(item[0])
        y2.add_y(item[1])

    y3 = Line()
    y3.x = y1.y
    y3.y = y2.y

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot_line(y1, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot_line(y2, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter_line(y3, markers.point, colors.steel_blue).show_last())
     # .plot_line(y3, markers.point, colors.steel_blue).show_last())


def run_2_cycle_3():
    α = 1
    β = 0.4
    γ = 0.7

    time_range = range(1, 100 + 1)

    source = time_series(
        skip_range=range(1, 10000 + 1),
        time_range=range(1, 10000 + 1),
        x_start=[0.2, 0.2],
        f=lambda x: function.f(α, β, γ, x[0], x[1]),
        skip=True
    )

    y = source.y

    y1 = Line()
    y2 = Line()
    y1.x = source.x
    y2.x = source.x
    for item in y:
        y1.add_y(item[0])
        y2.add_y(item[1])

    y3 = Line()
    y3.x = y1.y
    y3.y = y2.y

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot_line(y1, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot_line(y2, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter_line(y3, markers.point, colors.steel_blue).show_last())
     # .plot_line(y3, markers.point, colors.steel_blue).show_last())


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

    y = source.y

    y1 = Line()
    y2 = Line()
    y1.x = source.x
    y2.x = source.x
    for item in y:
        y1.add_y(item[0])
        y2.add_y(item[1])

    y3 = Line()
    y3.x = y1.y
    y3.y = y2.y

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-t')
     .plot_line(y1, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series y-t')
     .plot_line(y2, markers.point, colors.steel_blue).show())

    (Plotter()
     .setup_x_label('x')
     .setup_y_label('y')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series x-y')
     .scatter_line(y3, markers.point, colors.steel_blue).show_last())
     # .plot_line(y3, markers.point, colors.steel_blue).show_last())

