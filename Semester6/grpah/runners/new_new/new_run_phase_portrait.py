from core.algorithms.new.phase_portrait import phase_portrait
from models.new_new_model import function
from visual.plotter import Plotter
from visual.values import scale, grid, markers, colors


def run0():
    α = 1
    β = 0.5
    σ = 0

    line = phase_portrait(
        time_range=range(1, 100000 + 1),
        x_start=0.2,
        y_start=0.3,
        x=lambda x, y: function.__x(α, β, σ, x, y),
        y=lambda x, y: function.__y(α, β, σ, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run1_0():
    α = 1
    β = 0.5
    σ = 0.5

    line = phase_portrait(
        time_range=range(1, 100000 + 1),
        x_start=0.2,
        y_start=0.3,
        x=lambda x, y: function.__x(α, β, σ, x, y),
        y=lambda x, y: function.__y(α, β, σ, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(line.x, line.y, markers.point, colors.steel_blue)
         # .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run1_1():
    α = 1
    β = 0.5
    σ = 0.5

    line = phase_portrait(
        time_range=range(1, 100000 + 1),
        x_start=0.2,
        y_start=0.3,
        x=lambda x, y: function.__x(α, β, σ, x, y),
        y=lambda x, y: function.__y(α, β, σ, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         # .scatter(line.x, line.y, markers.point, colors.steel_blue)
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run2():
    α = 1
    β = 0.5
    σ = 0.4

    line = phase_portrait(
        time_range=range(1, 100000 + 1),
        x_start=0.2,
        y_start=0.3,
        x=lambda x, y: function.__x(α, β, σ, x, y),
        y=lambda x, y: function.__y(α, β, σ, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         # .scatter(line.x, line.y, markers.point, colors.steel_blue)
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run3_0():
    α = 1
    β = 0.5
    σ = 0.48

    line = phase_portrait(
        time_range=range(1, 100000 + 1),
        x_start=0.2,
        y_start=0.3,
        x=lambda x, y: function.__x(α, β, σ, x, y),
        y=lambda x, y: function.__y(α, β, σ, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         # .scatter(line.x, line.y, markers.point, colors.steel_blue)
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run3_1():
    α = 1
    β = 0.5
    σ = 0.48

    line = phase_portrait(
        time_range=range(1, 100000 + 1),
        x_start=0.2,
        y_start=0.3,
        x=lambda x, y: function.__x(α, β, σ, x, y),
        y=lambda x, y: function.__y(α, β, σ, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(line.x, line.y, markers.point, colors.steel_blue)
         # .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run4_0():
    α = 1
    β = 0.5
    σ = 0.625

    line = phase_portrait(
        time_range=range(1, 100000 + 1),
        x_start=0.2,
        y_start=0.3,
        x=lambda x, y: function.__x(α, β, σ, x, y),
        y=lambda x, y: function.__y(α, β, σ, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         # .scatter(line.x, line.y, markers.point, colors.steel_blue)
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run4_1():
    α = 1
    β = 0.5
    σ = 0.625

    line = phase_portrait(
        time_range=range(1, 100000 + 1),
        x_start=0.2,
        y_start=0.3,
        x=lambda x, y: function.__x(α, β, σ, x, y),
        y=lambda x, y: function.__y(α, β, σ, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(line.x, line.y, markers.point, colors.steel_blue)
         # .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run5():
    α = 1
    β = 0.5
    σ = 0.63077

    line = phase_portrait(
        time_range=range(1, 100000 + 1),
        x_start=0.2,
        y_start=0.3,
        x=lambda x, y: function.__x(α, β, σ, x, y),
        y=lambda x, y: function.__y(α, β, σ, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         # .scatter(line.x, line.y, markers.point, colors.steel_blue)
         .plot_line(line, markers.point, colors.steel_blue)
         .show())

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(line.x, line.y, markers.point, colors.steel_blue)
         # .plot_line(line, markers.point, colors.steel_blue)
         .show_last())