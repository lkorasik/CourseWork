import numpy as np

from core.algorithms.lamerei import lamerei
from functions_pkg import function, others
from visual.plotter import Plotter
from visual.values import colors, grid, scale, markers


def default():
    a = 1
    b = 0.56
    time_range = range(1, 100 + 1)
    skip = False
    x_range = np.arange(0, 0.34, 0.01)

    source0 = lamerei(
        x_start=0.03,
        time_range=time_range,
        skip=skip,
        f=lambda x: function.f(a, b, x)
    )
    source1 = lamerei(
        x_start=0.1,
        time_range=time_range,
        skip=skip,
        f=lambda x: function.f(a, b, x),
    )
    source2 = lamerei(
        x_start=0.3,
        time_range=time_range,
        skip=skip,
        f=lambda x: function.f(a, b, x),
    )

    plotter = (Plotter()
               # .setup_title("Lamerei")
               .setup_x_label('$x_t$')
               .setup_y_label('$x_{t + 1}$')
               .setup_grid(grid.major)
               .setup_y_scale(scale.linear))

    for line in source0 + source1 + source2:
        plotter.plot_line(line, markers.nothing, colors.red)

    (plotter
     .plot(x_range, others.g(a, x_range), ',', colors.steel_blue)
     .plot(x_range, function.f(a, b, x_range), ',', colors.orange)
     .show_last())


def fast_zero():
    a = 1
    b = 0.56
    time_range = range(1, 100 + 1)
    skip = False
    x_range = np.arange(0, 1.4, 0.01)

    source = lamerei(
        x_start=1.3,
        time_range=time_range,
        skip=skip,
        f=lambda x: function.f(a, b, x)
    )

    plotter = (Plotter()
               # .setup_title("Lamerei")
               .setup_x_label('$x_t$')
               .setup_y_label('$x_{t + 1}$', label_pad=15)
               .setup_grid(grid.major)
               .setup_y_scale(scale.linear))

    for line in source:
        plotter.plot_line(line, markers.nothing, colors.red)

    plotter.add_rectangle(-0.0035, -0.0035, 0.0835, 0.0835)

    (plotter
     .plot(x_range, others.g(a, x_range), ',', colors.steel_blue)
     .plot(x_range, function.f(a, b, x_range), ',', colors.orange)
     .show_last())


def fast_zero_segment():
    a = 1
    b = 0.56
    time_range = range(1, 100 + 1)
    skip = False
    x_range = np.arange(0, 0.1, 0.01)

    source = lamerei(
        x_start=1.3,
        time_range=time_range,
        skip=skip,
        f=lambda x: function.f(a, b, x)
    )

    plotter = (Plotter()
               # .setup_title("Lamerei")
               .setup_x_label('$x_t$')
               .setup_y_label('$x_{t + 1}$', label_pad=15)
               .setup_grid(grid.major)
               .setup_y_scale(scale.linear))

    for line in source:
        plotter.plot_line(line, markers.nothing, colors.red)

    plotter.add_rectangle(-0.0035, -0.0035, 0.0835, 0.0835)

    (plotter
     .plot(x_range, others.g(a, x_range), ',', colors.steel_blue)
     .plot(x_range, function.f(a, b, x_range), ',', colors.orange)
     .show_last())
