import numpy as np

from algorithms.bifurcation import bifurcation
from algorithms.cyclical_mean import cyclical_mean
from algorithms.mean import mean
from functions_pkg import functions_b_noise, function
from visual.plotter import Plotter
from visual.values import colors, grid, markers, scale


def single():
    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: function.f(1, b, x),
        up_border=10_000,
        down_border=None
    )
    source0 = mean(
        p_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.01),
        # f=lambda b, x: functions.f_pb(1, b, x, 0.01),
        up_border=10_000,
        down_border=None
    )
    source1 = mean(
        p_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.03),
        # f=lambda b, x: functions.f_pb(1, b, x, 0.03),
        up_border=10_000,
        down_border=None
    )
    source2 = mean(
        p_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.04),
        # f=lambda b, x: functions.f_pb(1, b, x, 0.04),
        up_border=10_000,
        down_border=None
    )
    source3 = mean(
        p_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    (Plotter()
     ._setup('b', 'x', 'linear', 'major', 'EV')
     .plot_line(source0, '.', colors.steel_blue, 'original')
     .plot_line(source1, '.', colors.red, '$\\varepsilon = 0.01$')
     .plot_line(source2, '.', colors.green, '$\\varepsilon = 0.03$')
     .plot_line(source3, '.', colors.black, '$\\varepsilon = 0.04$')
     .legend()
     .show_last())


def cyclic():
    source0 = cyclical_mean(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: function.f(1, b, x),
        count=100
    )
    source1 = cyclical_mean(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.01),
        count=100
    )
    source2 = cyclical_mean(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.03),
        count=100
    )
    source3 = cyclical_mean(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.04),
        count=100
    )

    (Plotter()
     .adjust(left=0.125, right=0.9, top=0.92, bottom=0.15)
     .setup_x_label('$\\beta$', font_size=20)
     .setup_y_label('x', font_size=20, label_pad=10)
     .setup_y_ticks(font_size=15)
     .setup_x_ticks(font_size=15, ticks=np.arange(0.2, 0.6, 0.05))
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('EV cyclic')
     .plot_line(source0, markers.point, colors.steel_blue, '$\\varepsilon = 0$')
     .plot_line(source1, markers.point, colors.red, '$\\varepsilon = 0.01$')
     .plot_line(source2, markers.point, colors.green, '$\\varepsilon = 0.03$')
     .plot_line(source3, markers.point, colors.black, '$\\varepsilon = 0.04$')
     .legend(font_size=15)
     .show_last())
