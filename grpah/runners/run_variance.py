import numpy as np

from algorithms.bifurcation import bifurcation
from algorithms.cyclical_variance import cyclical_variance
from algorithms.variance import variance
from functions_pkg import functions_b_noise, function
from visual.plotter import Plotter
from visual.values import colors, grid, scale


def single():
    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: function.f(1, b, x),
        down_border=None
    )
    source0 = variance(
        p_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.01),
        # f=lambda b, x: functions.f_pb(1, b, x, 0.01),
        down_border=None
    )
    source1 = variance(
        p_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.03),
        # f=lambda b, x: functions.f_pb(1, b, x, 0.03),
        down_border=None
    )
    source2 = variance(
        p_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.04),
        # f=lambda b, x: functions.f_pb(1, b, x, 0.04),
        down_border=None
    )
    source3 = variance(
        p_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    (Plotter()
     ._setup('b', 'x', 'linear', 'major', 'Variance')
     .plot_line(source0, '.', colors.steel_blue)
     .plot(source1.x, source1.y, '.', colors.red)
     .plot(source2.x, source2.y, '.', colors.green)
     .plot(source3.x, source3.y, '.', colors.black)
     .show_last())


def cyclic():
    source0 = cyclical_variance(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: function.f(1, b, x),
        count=1000
    )
    source1 = cyclical_variance(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.01),
        # f=lambda b, x: functions.f_pb(1, b, x, 0.01),
        count=1000
    )
    source2 = cyclical_variance(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.03),
        # f=lambda b, x: functions.f_pb(1, b, x, 0.03),
        count=1000
    )
    source3 = cyclical_variance(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.04),
        # f=lambda b, x: functions.f_pb(1, b, x, 0.04),
        count=1000
    )

    (Plotter()
     .adjust(left=0.125, right=0.9, top=0.92, bottom=0.15)
     .setup_x_label('$\\beta$', font_size=20)
     .setup_y_label('x', font_size=20, label_pad=10)
     .setup_y_ticks(font_size=15)
     .setup_x_ticks(font_size=15, ticks=np.arange(0.2, 0.6, 0.05))
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('Variance cyclic')
     .plot_line(source0, '.', colors.steel_blue, '$\\varepsilon = 0$')
     .plot_line(source1, '.', colors.red, '$\\varepsilon = 0.01$')
     .plot_line(source2, '.', colors.green, '$\\varepsilon = 0.03$')
     .plot_line(source3, '.', colors.black, '$\\varepsilon = 0.04$')
     .legend(font_size=15)
     .show_last())