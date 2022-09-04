import numpy as np

import functions
from algorithms.bifurcation import bifurcation
from algorithms.cyclical_mean import cyclical_mean
from algorithms.cyclical_variance import cyclical_variance
from algorithms.equilibrium import equilibrium
from algorithms.lamerei import lamerei
from algorithms.lyapunov import lyapunov
from algorithms.mean import mean
from algorithms.regime_map import regime_map
from algorithms.variance import variance
from functions_pkg import functions_b_noise, function, others
from visual.plotter import Plotter
from visual.values import colors, grid, markers, scale


def run_lyapunov():
    source = lyapunov(
        epsilon=10 ** (-5),
        b_range=np.arange(0.22, 0.582355932, 0.001),
        x_start=0.2,
        time_range=range(1, 100 + 1),
        T=100,
        f=lambda b, x: function.f(1, b, x),
        lambda_=functions.lambda_
    )

    (Plotter()
     .setup_x_label('$\\beta$')
     .setup_y_label('$\\lambda$', label_pad=5)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title("Lyapunov")
     # ._setup(r'$\beta$', '$\lambda$', 'linear', 'major', 'Lyapunov')
     .plot(source[0], source[1], ',', colors.red)
     .show_last())


def run_lamerei():
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

    for lst in [source0, source1, source2]:
        for i in lst:
            plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')

    (plotter
     .plot(x_range, others.g(a, x_range), ',', colors.steel_blue)
     .plot(x_range, function.f(a, b, x_range), ',', colors.orange)
     .show_last())


def run_lamerei_fast_zero():
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

    for i in source:
        plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')

    plotter.add_rectangle(-0.0035, -0.0035, 0.0835, 0.0835)

    (plotter
     .plot(x_range, others.g(a, x_range), ',', colors.steel_blue)
     .plot(x_range, function.f(a, b, x_range), ',', colors.orange)
     .show_last())


def run_lamerei_fast_zero_segment():
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

    for i in source:
        plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')

    plotter.add_rectangle(-0.0035, -0.0035, 0.0835, 0.0835)

    (plotter
     .plot(x_range, others.g(a, x_range), ',', colors.steel_blue)
     .plot(x_range, function.f(a, b, x_range), ',', colors.orange)
     .show_last())


def run_equilibrium():
    source = equilibrium(
        x12=0.12,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        d=lambda b, x: function.f_dx(1, b, x)
        # d=lambda b, x: functions.df(1, b, x)
    )

    plotter = Plotter()._setup('b', 'x', 'linear', 'major', 'Bifurcation with equilibrium')

    colors_ = [colors.red, colors.deep_pink, colors.green, colors.black, colors.black]

    for i in range(len(source)):
        plotter.plot_line(source[i], ',', colors_[i])

    plotter.show_last()


def run_regime_map():
    regime_map(
        x_start=0.2,
        a_range=np.arange(0.01, 2, 0.001),
        b_range=np.arange(0.01, 0.6, 0.001),
        time_range=range(1, 10000 + 1),
        f=function.f,
        file_path="C:\\Users\\lkora\\Desktop\\data\\"
    )


def run_mean():
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


def run_cyclic_mean():
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


def run_variance():
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


def run_cyclic_variance():
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
