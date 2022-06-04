import numpy as np
from matplotlib import patches, pyplot as plt

import functions
from algorithms.absorbing_area import absorbing_area
from algorithms.bifurcation import bifurcation
from algorithms.bifurcation_with_equilibrium import bifurcation_with_equilibrium
from algorithms.bifurcation_with_ssf import bifurcation_with_ssf
from algorithms.convert_dict_to_lists import convert_dict_to_lists
from algorithms.convert_line_to_dict import convert_line_to_dict
from algorithms.cyclical_mean import cyclical_mean
from algorithms.cyclical_variance import cyclical_variance
from algorithms.equilibrium import equilibrium
from algorithms.lamerei import lamerei
from algorithms.lyapunov import lyapunov
from algorithms.m_b import m_b
from algorithms.mean import mean
from algorithms.regime_map import regime_map
from algorithms.time_series import time_series
from algorithms.variance import variance
from functions_pkg import functions_b_noise, function, functions_a_noise, functions_additive_noise, others
from visual.values import colors, grid, markers, scale
from visual.line import Line
from visual.plotter import Plotter


def run_time_series_without_chaos():
    source = time_series(
        time_range=range(1, 50 + 1),
        x_start=1.3,
        f=lambda x: function.f(1, 0.56, x),
        skip=False
    )

    (Plotter()
        .setup_x_label('x')
        .setup_y_label('t')
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        .setup_title('Time series')
        .plot(source[0], source[1], markers.star, colors.steel_blue)
        .show_last())


def run_time_series_without_chaos_composition():
    time_range = range(1, 30 + 1)
    a = 1
    b = 0.56

    source0 = time_series(
        time_range=time_range,
        x_start=1.3,
        f=lambda x: function.f(a, b, x),
        skip=False
    )
    source1 = time_series(
        time_range=time_range,
        x_start=0.3,
        f=lambda x: function.f(a, b, x),
        skip=False
    )
    source2 = time_series(
        time_range=time_range,
        x_start=0.06,
        f=lambda x: function.f(a, b, x),
        skip=False
    )
    source3 = time_series(
        time_range=time_range,
        x_start=0.04,
        f=lambda x: function.f(a, b, x),
        skip=False
    )

    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x', label_pad=10)
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        # .setup_title('Time series')
        .plot(source0[0], source0[1], markers.star, colors.dark_violet, '1.3')
        .plot(source1[0], source1[1], markers.star, colors.dark_slate_blue, '0.3')
        .plot(source2[0], source2[1], markers.star, colors.blue, '0.06')
        .plot(source3[0], source3[1], markers.star, colors.royal_blue, '0.04')
        .legend()
        .show_last())


def run_time_series_different_noises():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.004

    source0 = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x')
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        .setup_title('Time series original')
        .plot(source0[0], source0[1], markers.point, colors.steel_blue)
        .show())

    source1 = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x')
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        .setup_title('Time series with $\\beta$-noise')
        .plot(source1[0], source1[1], markers.point, colors.steel_blue)
        .show())

    source2 = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x')
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        .setup_title('Time series with $\\alpha$-noise')
        .plot(source2[0], source2[1], markers.point, colors.steel_blue)
        .show())

    source3 = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x')
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        .setup_title('Time series with additive noise')
        .plot(source3[0], source3[1], markers.point, colors.steel_blue)
        .show_last())


def run_time_series_no_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    (Plotter()
        .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
        .setup_x_label('t', font_size=25, label_pad=0)
        .setup_x_ticks(font_size=20)
        .setup_y_label('x', font_size=25, label_pad=12)
        .setup_y_ticks(font_size=20)
        .setup_grid(grid.major)
        # .setup_title('Time series original')
        .plot(source[0], source[1], '.', colors.steel_blue)
        .show_last())


def run_time_series_beta_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
        .setup_x_label('t', font_size=25, label_pad=0)
        .setup_x_ticks(font_size=20)
        .setup_y_label('x', font_size=25, label_pad=12)
        .setup_y_ticks(font_size=20)
        .setup_grid(grid.major)
        # .setup_title('Time series $\beta$-noise')
        .plot(source[0], source[1], '.', colors.steel_blue)
        .show_last())


def run_time_series_beta_noise_can_drop():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.04

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
        .setup_x_label('t', font_size=25, label_pad=0)
        .setup_x_ticks(font_size=20)
        .setup_y_label('x', font_size=25, label_pad=12)
        .setup_y_ticks(font_size=20)
        .setup_grid(grid.major)
        # .setup_title('Time series $\beta$-noise')
        .plot(source[0], source[1], '.', colors.steel_blue)
        .show_last())


def run_time_series_alpha_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
        .setup_x_label('t', font_size=25, label_pad=0)
        .setup_x_ticks(font_size=20)
        .setup_y_label('x', font_size=25, label_pad=12)
        .setup_y_ticks(font_size=20)
        .setup_grid(grid.major)
        # .setup_title('Time series $\alpha$-noise')
        .plot(source[0], source[1], '.', colors.steel_blue)
        .show_last())


def run_time_series_additive_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
        .setup_x_label('t', font_size=25, label_pad=0)
        .setup_x_ticks(font_size=20)
        .setup_y_label('x', font_size=25, label_pad=12)
        .setup_y_ticks(font_size=20)
        .setup_grid(grid.major)
        # .setup_title('Time series additive-noise')
        .plot(source[0], source[1], '.', colors.steel_blue)
        .show_last())


def run_time_series_compare_noise():
    time_range = range(1, 30 + 1)
    x_start0 = 0.04
    x_start1 = 0.06
    x_start2 = 0.3
    x_start3 = 1.3
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.01

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )

    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x')
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        .setup_title('Time series original')
        .plot(source0[0], source0[1], markers.point, colors.light_coral)
        .plot(source1[0], source1[1], markers.point, colors.dark_olive_green)
        .plot(source2[0], source2[1], markers.point, colors.olive)
        .plot(source3[0], source3[1], markers.point, colors.teal)
        .show())
    # .show_last())

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x')
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        .setup_title('Time series with $\\beta$-noise')
        .plot(source0[0], source0[1], markers.point, colors.light_coral)
        .plot(source1[0], source1[1], markers.point, colors.dark_olive_green)
        .plot(source2[0], source2[1], markers.point, colors.olive)
        .plot(source3[0], source3[1], markers.point, colors.teal)
        .show())

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x')
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        .setup_title('Time series with $\\alpha$-noise')
        .plot(source0[0], source0[1], markers.point, colors.light_coral)
        .plot(source1[0], source1[1], markers.point, colors.dark_olive_green)
        .plot(source2[0], source2[1], markers.point, colors.olive)
        .plot(source3[0], source3[1], markers.point, colors.teal)
        .show())

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x')
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        .setup_title('Time series with additive noise')
        .plot(source0[0], source0[1], markers.point, colors.light_coral)
        .plot(source1[0], source1[1], markers.point, colors.dark_olive_green)
        .plot(source2[0], source2[1], markers.point, colors.olive)
        .plot(source3[0], source3[1], markers.point, colors.teal)
        # .show())
        .show_last())


def run_time_series_2_cycle():
    time_range = range(1, 100 + 1)
    x_start = 0.1
    skip = False

    a = 1
    b = 0.4

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )

    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x', label_pad=10)
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        # .setup_title('Time series')
        .plot(source[0], source[1], markers.star, colors.steel_blue)
        .show_last())


def run_time_series_chaos():
    time_range = range(1, 100 + 1)
    x_start = 0.1
    skip = False

    a = 1
    b = 0.25

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )

    (Plotter()
        .setup_x_label('t')
        .setup_y_label('x', label_pad=10)
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        # .setup_title('Time series')
        .plot(source[0], source[1], markers.star, colors.steel_blue)
        .show_last())


def run_bifurcation():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x)
    )

    source = convert_dict_to_lists(source)

    (Plotter()
        .setup_x_label('$\\beta$')
        .setup_y_label('x', label_pad=5)
        .setup_y_scale(scale.log)
        .setup_grid(grid.major)
        # .setup_title('Bifurcation')
        .scatter(source[0], source[1], '.', colors.steel_blue)
     # .show())
        .show_last())


def run_compare_chaos_bifurcation():
    time_range = range(1, 100 + 1)
    x_start = 0.2
    p_range = np.arange(0.22, 0.582355932, 0.001)

    a = 1
    epsilon = 0.01

    source0 = bifurcation(
        time_range=time_range,
        x_start=x_start,
        p_range=p_range,
        f=lambda b, x: function.f(a, b, x)
    )
    source0 = convert_dict_to_lists(source0)

    (Plotter()
        .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
        .setup_x_label('$\\beta$', font_size=25, label_pad=0)
        .setup_x_ticks(font_size=15, ticks=np.arange(0.2, 0.6, 0.05))
        .setup_y_label('x', font_size=25, label_pad=12)
        .setup_y_ticks(font_size=15)
        .setup_y_scale(scale.log)
        .setup_grid(grid.major)
        # .setup_title('Bifurcation')
        .scatter(source0[0], source0[1], '.', colors.steel_blue)
        .show())

    source1 = bifurcation(
        time_range=time_range,
        x_start=x_start,
        p_range=p_range,
        f=lambda b, x: functions_a_noise.f(a, b, x, epsilon)
    )
    source1 = convert_dict_to_lists(source1)

    (Plotter()
        .adjust(top=0.92, bottom=0.165, left=0.175, right=0.95)
        .setup_x_label('$\\beta$', font_size=25, label_pad=0)
        .setup_y_label('x', font_size=25, label_pad=12)
        .setup_x_ticks(font_size=15)
        .setup_y_ticks(font_size=15)
        .setup_y_scale(scale.log)
        .setup_grid(grid.major)
        .setup_title('Bifurcation alpha')
        .scatter(source1[0], source1[1], '.', colors.steel_blue)
        .show())

    source2 = bifurcation(
        time_range=time_range,
        x_start=x_start,
        p_range=p_range,
        f=lambda b, x: functions_b_noise.f(a, b, x, epsilon)
    )
    source2 = convert_dict_to_lists(source2)

    (Plotter()
        .adjust(top=0.92, bottom=0.165, left=0.175, right=0.95)
        .setup_x_label('$\\beta$', font_size=25, label_pad=0)
        .setup_y_label('x', font_size=25, label_pad=12)
        .setup_x_ticks(font_size=15)
        .setup_y_ticks(font_size=15)
        .setup_y_scale(scale.log)
        .setup_grid(grid.major)
        .setup_title('Bifurcation beta')
        .scatter(source2[0], source2[1], '.', colors.steel_blue)
        .show())

    source3 = bifurcation(
        time_range=time_range,
        x_start=x_start,
        p_range=p_range,
        f=lambda b, x: functions_additive_noise.f(a, b, x, epsilon)
    )
    source3 = convert_dict_to_lists(source3)

    (Plotter()
        .adjust(top=0.92, bottom=0.165, left=0.175, right=0.95)
        .setup_x_label('$\\beta$', font_size=25, label_pad=0)
        .setup_y_label('x', font_size=25, label_pad=12)
        .setup_x_ticks(font_size=15)
        .setup_y_ticks(font_size=15)
        .setup_y_scale(scale.log)
        .setup_grid(grid.major)
        .setup_title('Bifurcation addition')
        .scatter(source3[0], source3[1], '.', colors.steel_blue)
        .show_last())


def run_bifurcation_with_absorbing_area():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    a = 1

    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(a, b, x)
    )
    draw_x, draw_y = convert_dict_to_lists(source)

    source = absorbing_area(
        p_range=p_range,
        left=0,
        right=1,
        step=0.0001,
        f=lambda b, x: function.f(a, b, x),
    )

    (Plotter()
        .setup_x_label('$\\beta$')
        .setup_y_label('x', label_pad=5)
        .setup_y_scale(scale.log)
        .setup_grid(grid.major)
        # .setup_title("Bifurcation")
        # ._setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')
        .scatter(draw_x, draw_y, '.', colors.steel_blue)
        .plot(source[0], source[1], ',', colors.red)
        .plot(source[0], source[2], ',', colors.red)
        .show_last())


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


def run_bifurcation_with_equilibrium():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.1164711,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
        down_border=None
    )

    source = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values
    )

    values = convert_dict_to_lists(values)

    (Plotter()
        ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium')
        .scatter(values[0], values[1], '.', colors.steel_blue)
        .plot_line(source[0], ',', colors.red)
        .plot_line(source[1], ',', colors.deep_pink)
        .plot_line(source[2], ',', colors.green)
     # .show())
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
        .setup_y_ticks(font_size=20)
        .setup_x_ticks(font_size=20, ticks=np.arange(0.2, 0.6, 0.1))
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
        .setup_x_label('$\\beta$')
        .setup_y_label('x')
        .setup_y_scale(scale.log)
        .setup_grid(grid.major)
        # .setup_title('Variance cyclic')
        .plot_line(source0, '.', colors.steel_blue, '$\\varepsilon = 0$')
        .plot_line(source1, '.', colors.red, '$\\varepsilon = 0.01$')
        .plot_line(source2, '.', colors.green, '$\\varepsilon = 0.03$')
        .plot_line(source3, '.', colors.black, '$\\varepsilon = 0.04$')
        .legend()
        .show_last())


def run_stochastic_sensitivity_b_noise():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    epsilon = 0.001

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
        m=lambda a, b, x: functions_b_noise.m(a, b, x, epsilon),
        epsilon=epsilon,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_b_noise.s(1, b, x, epsilon),
        q=lambda b, x: functions_b_noise.q(1, b, x, epsilon),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions_b_noise.f(1, b, x, epsilon)
        # f=lambda b, x: functions.f_pb(1, b, x, epsilon)
    )
    chaos = convert_dict_to_lists(chaos)

    # .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
    # .setup_x_label('t', font_size=25, label_pad=0)
    # .setup_x_ticks(font_size=20)
    # .setup_y_label('x', font_size=25, label_pad=12)
    # .setup_y_ticks(font_size=20)

    # Create a Rectangle patch
    # rect = patches.Rectangle((50, 100), 40, 30, linewidth=1, edgecolor='r', facecolor='none')

    plotter = (Plotter()
                # ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\beta$-noise')
                .setup_x_label('$\\beta$', font_size=13, label_pad=2)
                .setup_y_label('x', font_size=13, label_pad=6)
                .setup_x_ticks(font_size=13)
                .setup_y_ticks(font_size=13)
                .setup_y_scale(scale.log)
                .setup_grid(grid.major)
                # .setup_title('Bifurcation with $\\beta$-noise')
                .scatter(chaos[0], chaos[1], '.', colors.steel_blue))

    for line in source:
        plotter.plot(line.x, line.y, ',', colors.red)

    (plotter
        .add_rectangle(0.451, 0.275, 0.025, 0.3)
        .add_rectangle(0.352, 0.7, 0.035, 0.9)
        .add_rectangle(0.24, 0.0003, 0.03, 0.0017)
        .add_rectangle(0.252, 2, 0.03, 7.4))

    plotter.show_last()
    # plotter.show()


def run_stochastic_sensitivity_b_noise_1():
    p_range = np.arange(0.451, 0.476, 0.0001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
        m=lambda a, b, x: functions_b_noise.m(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_b_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q(1, b, x, 0.001),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.001)
        # f=lambda b, x: functions.f_pb(1, b, x, 0.001)
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
                .setup_x_limit(0.451, 0.476)
                .setup_y_limit(0.275, 0.575)
                # ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\beta$-noise')
                .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
                .setup_x_label('$\\beta$', font_size=25, label_pad=0)
                .setup_x_ticks(font_size=20)
                .setup_y_label('x', font_size=25, label_pad=12)
                .setup_y_ticks(font_size=20)
                .setup_grid(grid.major)
                .scatter(chaos[0], chaos[1], '.', 'steelblue'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()
    # plotter.show()


def run_stochastic_sensitivity_b_noise_2():
    p_range = np.arange(0.352, 0.387, 0.0001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
        m=lambda a, b, x: functions_b_noise.m(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_b_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q(1, b, x, 0.001),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.001)
        # f=lambda b, x: functions.f_pb(1, b, x, 0.001)
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
                .setup_x_limit(0.352, 0.387)
                .setup_y_limit(0.7, 1.6)
                .setup_grid(grid.major)
                .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
                .setup_x_label('$\\beta$', font_size=25, label_pad=0)
                .setup_x_ticks(ticks=np.arange(0.352, 0.387, 0.01), font_size=20)
                .setup_y_label('x', font_size=25, label_pad=12)
                .setup_y_ticks(font_size=20)
               # ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\beta$-noise')
               .scatter(chaos[0], chaos[1], '.', 'steelblue'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()
    # plotter.show()


def run_stochastic_sensitivity_b_noise_3():
    p_range = np.arange(0.24, 0.27, 0.0001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
        m=lambda a, b, x: functions_b_noise.m(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_b_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q(1, b, x, 0.001),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.001)
        # f=lambda b, x: functions.f_pb(1, b, x, 0.001)
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
                .setup_x_limit(0.24, 0.27)
                .setup_y_limit(0.0003, 0.002)
                .setup_y_scale(scale.log)
                .setup_grid(grid.major)
                .setup_x_label('$\\beta$', font_size=25, label_pad=0)
                .setup_y_label('x', font_size=25, label_pad=12)
                .setup_x_ticks(ticks=np.arange(0.24, 0.27, 0.01), font_size=20)
                .setup_y_ticks(font_size=15)
                .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
               # ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\beta$-noise')
               .scatter(chaos[0], chaos[1], '.', 'steelblue'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()
    # plotter.show()


def run_stochastic_sensitivity_b_noise_4():
    p_range = np.arange(0.252, 0.282, 0.0001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
        m=lambda a, b, x: functions_b_noise.m(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_b_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q(1, b, x, 0.001),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions_b_noise.f(1, b, x, 0.001)
        # f=lambda b, x: functions.f_pb(1, b, x, 0.001)
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
                .setup_x_limit(0.252, 0.282)
                .setup_y_limit(2, 9.4)
                .setup_y_scale(scale.log)
                .setup_grid(grid.major)
                .setup_x_label('$\\beta$', font_size=25, label_pad=0)
                .setup_y_label('x', font_size=25, label_pad=12)
                .setup_x_ticks(ticks=np.arange(0.252, 0.282, 0.01), font_size=20)
                .setup_y_ticks(font_size=15)
                .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
               # ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\beta$-noise')
               .scatter(chaos[0], chaos[1], '.', 'steelblue'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()
    # plotter.show()


def run_stochastic_sensitivity_a_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
        m=lambda a, b, x: functions_a_noise.m(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_a_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_a_noise.q(1, b, x, 0.001),
        q_=functions_a_noise._q,
        s_=functions_a_noise._s
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions_a_noise.f(1, b, x, 0.001)
        # f=lambda b, x: functions.f_pa(1, b, x, 0.001),
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
               ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\alpha$-noise')
               .scatter(chaos[0], chaos[1], '.', colors.steel_blue))

    for line in source:
        plotter.plot(line.x, line.y, ',', colors.red)

    plotter.show_last()
    # plotter.show()


def run_stochastic_sensitivity_additive_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
        m=lambda a, b, x: functions_additive_noise.m(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_additive_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_additive_noise.q(1, b, x, 0.001),
        q_=functions_additive_noise._q,
        s_=functions_additive_noise._s
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions_additive_noise.f(1, b, x, 0.001)
        # f=lambda b, x: functions.f_p(1, b, x, 0.001),
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
               ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with additive noise')
               .scatter(chaos[0], chaos[1], '.', colors.steel_blue))

    for line in source:
        plotter.plot(line.x, line.y, ',', colors.red)

    plotter.show_last()


def run_m_b_beta_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
    )
    source = m_b(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_b_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_b_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q(1, b, x, 0.001),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Stochastic sensetivity $\\beta$-noise'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.plot(source[0].x, source[0].y, ',', 'orange')
    plotter.plot(source[2].x, source[2].y, ',', 'orange')
    plotter.plot(source[4].x, source[4].y, ',', 'orange')
    plotter.plot(source[7].x, source[7].y, ',', 'orange')

    plotter.show_last()
    # plotter.show()


def run_m_b_alpha_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
    )
    source = m_b(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_a_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_a_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_a_noise.q(1, b, x, 0.001),
        q_=functions_a_noise._q,
        s_=functions_a_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Stochastic sensetivity $\\alpha$-noise'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()
    # plotter.show()


def run_m_b_additive_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
    )
    source = m_b(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_additive_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_additive_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_additive_noise.q(1, b, x, 0.001),
        q_=functions_additive_noise._q,
        s_=functions_additive_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Stochastic sensetivity additive-noise'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()


def run_machalanobis_beta_noise():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x)
    )

    equilibrium = bifurcation_with_equilibrium(
        b_range=p_range,
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values,
        save_all=True
    )

    m_beta = m_b(
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_b_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_b_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q(1, b, x, 0.001),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    # Проверь, что используется в хаосе и в циклах. Похоже где-то перепутал местами

    stable_equilibrium = equilibrium[1]
    unstable_equilibrium = equilibrium[0]
    prototype_equilibrium = equilibrium[2]

    stable_equilibrium = convert_line_to_dict(stable_equilibrium)
    unstable_equilibrium = convert_line_to_dict(unstable_equilibrium)
    prototype_equilibrium = convert_line_to_dict(prototype_equilibrium)

    line0 = convert_line_to_dict(m_beta[0])
    line1 = convert_line_to_dict(m_beta[2])
    line2 = convert_line_to_dict(m_beta[4])
    line3 = convert_line_to_dict(m_beta[7])
    lines = [line0, line1, line2, line3]

    mahalanobis0 = Line()
    for b in stable_equilibrium.keys():
        y_s = stable_equilibrium[b]
        y_n = unstable_equilibrium[b]

        for line in lines:
            m = None
            if b in line.keys():
                m = line[b]

            metrics = None
            if m is not None:
                metrics = abs(y_s - y_n) / np.sqrt(m)
                # metrics = abs(y_s - y_n)

            if metrics is not None:
                mahalanobis0.add_x(b).add_y(metrics)

    line0 = convert_line_to_dict(m_beta[0])
    line1 = convert_line_to_dict(m_beta[1])
    line2 = convert_line_to_dict(m_beta[5])
    line3 = convert_line_to_dict(m_beta[8])
    lines = [line0, line1, line2, line3]

    mahalanobis1 = Line()
    for b in stable_equilibrium.keys():
        y_s = stable_equilibrium[b]
        y_p = prototype_equilibrium[b]

        for line in lines:
            m = None
            if b in line.keys():
                m = line[b]

            metrics = None
            if m is not None:
                metrics = abs(y_s - y_p) / np.sqrt(m)
                # metrics = abs(y_s - y_p)

            if metrics is not None:
                mahalanobis1.add_x(b).add_y(metrics)

    plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Mahalanobis metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    # plotter.show_last()
    plotter.show()


def run_machalanobis_alpha_noise():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x)
    )

    equilibrium = bifurcation_with_equilibrium(
        b_range=p_range,
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values,
        save_all=True
    )

    m_beta = m_b(
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_a_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_a_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_a_noise.q(1, b, x, 0.001),
        q_=functions_a_noise._q,
        s_=functions_a_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    stable_equilibrium = equilibrium[1]
    unstable_equilibrium = equilibrium[0]
    prototype_equilibrium = equilibrium[2]

    stable_equilibrium = convert_line_to_dict(stable_equilibrium)
    unstable_equilibrium = convert_line_to_dict(unstable_equilibrium)
    prototype_equilibrium = convert_line_to_dict(prototype_equilibrium)

    # Что-то намудрил с m

    line0 = convert_line_to_dict(m_beta[0])
    line1 = convert_line_to_dict(m_beta[2])
    line2 = convert_line_to_dict(m_beta[4])
    line3 = convert_line_to_dict(m_beta[7])
    lines = [line0, line1, line2, line3]

    result = dict()
    for b in stable_equilibrium.keys():
        result[b] = 0

    mahalanobis0 = Line()
    mahalanobis1 = Line()
    for b in result.keys():
        y_s = None
        if b in stable_equilibrium.keys():
            y_s = stable_equilibrium[b]

        y_n = None
        if b in unstable_equilibrium.keys():
            y_n = unstable_equilibrium[b]

        y_p = None
        if b in prototype_equilibrium.keys():
            y_p = prototype_equilibrium[b]

        for line in lines:
            m = None
            if b in line.keys():
                m = line[b]

            metrics0 = None
            if y_s is not None and y_n is not None and m is not None:
                metrics0 = abs(y_s - y_n) / np.sqrt(m)

            metrics1 = None
            if y_s is not None and y_p is not None and m is not None:
                metrics1 = abs(y_s - y_p) / np.sqrt(m)

            if metrics0 is not None:
                mahalanobis0.add_x(b).add_y(metrics0)

            if metrics1 is not None:
                mahalanobis1.add_x(b).add_y(metrics1)

    plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Mahalanobis metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    # plotter.show_last()
    plotter.show()


def run_machalanobis_additive_noise():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x)
    )

    equilibrium = bifurcation_with_equilibrium(
        b_range=p_range,
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values,
        save_all=True
    )

    m_beta = m_b(
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_additive_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_additive_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_additive_noise.q(1, b, x, 0.001),
        q_=functions_additive_noise._q,
        s_=functions_additive_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    stable_equilibrium = equilibrium[1]
    unstable_equilibrium = equilibrium[0]
    prototype_equilibrium = equilibrium[2]

    stable_equilibrium = convert_line_to_dict(stable_equilibrium)
    unstable_equilibrium = convert_line_to_dict(unstable_equilibrium)
    prototype_equilibrium = convert_line_to_dict(prototype_equilibrium)

    line0 = convert_line_to_dict(m_beta[0])
    line1 = convert_line_to_dict(m_beta[2])
    line2 = convert_line_to_dict(m_beta[4])
    line3 = convert_line_to_dict(m_beta[7])
    lines = [line0, line1, line2, line3]

    result = dict()
    for b in stable_equilibrium.keys():
        result[b] = 0

    mahalanobis0 = Line()
    mahalanobis1 = Line()
    for b in result.keys():
        y_s = None
        if b in stable_equilibrium.keys():
            y_s = stable_equilibrium[b]

        y_n = None
        if b in unstable_equilibrium.keys():
            y_n = unstable_equilibrium[b]

        y_p = None
        if b in prototype_equilibrium.keys():
            y_p = prototype_equilibrium[b]

        for line in lines:
            m = None
            if b in line.keys():
                m = line[b]

            metrics0 = None
            if y_s is not None and y_n is not None and m is not None:
                metrics0 = abs(y_s - y_n) / np.sqrt(m)

            metrics1 = None
            if y_s is not None and y_p is not None and m is not None:
                metrics1 = abs(y_s - y_p) / np.sqrt(m)

            if metrics0 is not None:
                mahalanobis0.add_x(b).add_y(metrics0)

            if metrics1 is not None:
                mahalanobis1.add_x(b).add_y(metrics1)

    plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Mahalanobis metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    # plotter.show_last()
    plotter.show()


def run_euclid_beta_noise():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x)
    )

    equilibrium = bifurcation_with_equilibrium(
        b_range=p_range,
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values,
        save_all=True
    )

    m_beta = m_b(
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_b_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_b_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q(1, b, x, 0.001),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    # Проверь, что используется в хаосе и в циклах. Похоже где-то перепутал местами

    stable_equilibrium = equilibrium[1]
    unstable_equilibrium = equilibrium[0]
    prototype_equilibrium = equilibrium[2]

    stable_equilibrium = convert_line_to_dict(stable_equilibrium)
    unstable_equilibrium = convert_line_to_dict(unstable_equilibrium)
    prototype_equilibrium = convert_line_to_dict(prototype_equilibrium)

    line0 = convert_line_to_dict(m_beta[0])
    line1 = convert_line_to_dict(m_beta[2])
    line2 = convert_line_to_dict(m_beta[4])
    line3 = convert_line_to_dict(m_beta[7])
    lines = [line0, line1, line2, line3]

    mahalanobis0 = Line()
    for b in stable_equilibrium.keys():
        y_s = stable_equilibrium[b]
        y_n = unstable_equilibrium[b]

        for line in lines:
            m = None
            if b in line.keys():
                m = line[b]

            metrics = None
            if m is not None:
                # metrics = abs(y_s - y_n) / np.sqrt(m)
                metrics = abs(y_s - y_n)

            if metrics is not None:
                mahalanobis0.add_x(b).add_y(metrics)

    line0 = convert_line_to_dict(m_beta[0])
    line1 = convert_line_to_dict(m_beta[1])
    line2 = convert_line_to_dict(m_beta[5])
    line3 = convert_line_to_dict(m_beta[8])
    lines = [line0, line1, line2, line3]

    mahalanobis1 = Line()
    for b in stable_equilibrium.keys():
        y_s = stable_equilibrium[b]
        y_p = prototype_equilibrium[b]

        for line in lines:
            m = None
            if b in line.keys():
                m = line[b]

            metrics = None
            if m is not None:
                # metrics = abs(y_s - y_p) / np.sqrt(m)
                metrics = abs(y_s - y_p)

            if metrics is not None:
                mahalanobis1.add_x(b).add_y(metrics)

    plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Euclid metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    plotter.show_last()


def run_euclid_alpha_noise():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x)
    )

    equilibrium = bifurcation_with_equilibrium(
        b_range=p_range,
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values,
        save_all=True
    )

    m_beta = m_b(
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_a_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_a_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_a_noise.q(1, b, x, 0.001),
        q_=functions_a_noise._q,
        s_=functions_a_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    stable_equilibrium = equilibrium[1]
    unstable_equilibrium = equilibrium[0]
    prototype_equilibrium = equilibrium[2]

    stable_equilibrium = convert_line_to_dict(stable_equilibrium)
    unstable_equilibrium = convert_line_to_dict(unstable_equilibrium)
    prototype_equilibrium = convert_line_to_dict(prototype_equilibrium)

    # Что-то намудрил с m

    line0 = convert_line_to_dict(m_beta[0])
    line1 = convert_line_to_dict(m_beta[2])
    line2 = convert_line_to_dict(m_beta[4])
    line3 = convert_line_to_dict(m_beta[7])
    lines = [line0, line1, line2, line3]

    result = dict()
    for b in stable_equilibrium.keys():
        result[b] = 0

    mahalanobis0 = Line()
    mahalanobis1 = Line()
    for b in result.keys():
        y_s = None
        if b in stable_equilibrium.keys():
            y_s = stable_equilibrium[b]

        y_n = None
        if b in unstable_equilibrium.keys():
            y_n = unstable_equilibrium[b]

        y_p = None
        if b in prototype_equilibrium.keys():
            y_p = prototype_equilibrium[b]

        for line in lines:
            m = None
            if b in line.keys():
                m = line[b]

            metrics0 = None
            if y_s is not None and y_n is not None and m is not None:
                metrics0 = abs(y_s - y_n)

            metrics1 = None
            if y_s is not None and y_p is not None and m is not None:
                metrics1 = abs(y_s - y_p)

            if metrics0 is not None:
                mahalanobis0.add_x(b).add_y(metrics0)

            if metrics1 is not None:
                mahalanobis1.add_x(b).add_y(metrics1)

    plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Euclid metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    plotter.show_last()


def run_euclid_additive_noise():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x)
    )

    equilibrium = bifurcation_with_equilibrium(
        b_range=p_range,
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values,
        save_all=True
    )

    m_beta = m_b(
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_additive_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_additive_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_additive_noise.q(1, b, x, 0.001),
        q_=functions_additive_noise._q,
        s_=functions_additive_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    stable_equilibrium = equilibrium[1]
    unstable_equilibrium = equilibrium[0]
    prototype_equilibrium = equilibrium[2]

    stable_equilibrium = convert_line_to_dict(stable_equilibrium)
    unstable_equilibrium = convert_line_to_dict(unstable_equilibrium)
    prototype_equilibrium = convert_line_to_dict(prototype_equilibrium)

    line0 = convert_line_to_dict(m_beta[0])
    line1 = convert_line_to_dict(m_beta[2])
    line2 = convert_line_to_dict(m_beta[4])
    line3 = convert_line_to_dict(m_beta[7])
    lines = [line0, line1, line2, line3]

    result = dict()
    for b in stable_equilibrium.keys():
        result[b] = 0

    mahalanobis0 = Line()
    mahalanobis1 = Line()
    for b in result.keys():
        y_s = None
        if b in stable_equilibrium.keys():
            y_s = stable_equilibrium[b]

        y_n = None
        if b in unstable_equilibrium.keys():
            y_n = unstable_equilibrium[b]

        y_p = None
        if b in prototype_equilibrium.keys():
            y_p = prototype_equilibrium[b]

        for line in lines:
            m = None
            if b in line.keys():
                m = line[b]

            metrics0 = None
            if y_s is not None and y_n is not None and m is not None:
                metrics0 = abs(y_s - y_n)

            metrics1 = None
            if y_s is not None and y_p is not None and m is not None:
                metrics1 = abs(y_s - y_p)

            if metrics0 is not None:
                mahalanobis0.add_x(b).add_y(metrics0)

            if metrics1 is not None:
                mahalanobis1.add_x(b).add_y(metrics1)

    plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Euclid metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    plotter.show_last()


def critical_intensity_beta_noise():
    step = 0.001
    p_range = np.arange(0.22, 0.582355932, step)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )

    epsilon_ = 0.005

    source1 = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, step),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        dsf=lambda b, x: function.f_dx(1, b, x),
        bifurcation=values
    )

    source2 = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.375], [0.22, 0.34]],
        m=lambda a, b, x: functions_b_noise.m(a, b, x, epsilon_),
        epsilon=epsilon_,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_b_noise.s(1, b, x, epsilon_),
        q=lambda b, x: functions_b_noise.q(1, b, x, epsilon_),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s
    )

    R = []
    S = []
    for epsilon in np.arange(0.001, 0.21, step):
        print("Epsilon = ", epsilon)
        source0 = bifurcation_with_ssf(
            values=values,
            b_range=p_range,
            a=1,
            borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
            m=lambda a, b, x: functions_b_noise.m(a, b, x, epsilon),
            epsilon=epsilon,
            f=lambda b, x: function.f(1, b, x),
            s=lambda b, x: functions_b_noise.s(1, b, x, epsilon),
            q=lambda b, x: functions_b_noise.q(1, b, x, epsilon),
            q_=functions_b_noise._q,
            s_=functions_b_noise._s
        )

        equilibrium_ = []
        for line in source1:
            equilibrium_.append(convert_line_to_dict(line))

        fss_ = []
        for line in source0:
            fss_.append(convert_line_to_dict(line))

        is_upper0 = []
        is_upper1 = []
        is_upper2 = []
        is_upper3 = []

        is_under0 = []
        is_under1 = []
        is_under2 = []
        is_under3 = []

        eq = equilibrium_[0]
        proto = equilibrium_[2]

        fss0 = fss_[0]
        fss1 = fss_[3]
        fss2 = fss_[7]
        fss3 = fss_[14]

        fss4 = fss_[1]
        fss5 = fss_[4]
        fss6 = fss_[10]
        fss7 = fss_[15]

        for key in eq.keys():
            eq_v = eq[key]
            fss0_v = None
            if key in fss0.keys():
                fss0_v = fss0[key]
            fss1_v = None
            if key in fss1.keys():
                fss1_v = fss1[key]
            fss2_v = None
            if key in fss2.keys():
                fss2_v = fss2[key]
            fss3_v = None
            if key in fss3.keys():
                fss3_v = fss3[key]

            if fss0_v is None and fss1_v is None and fss2_v is None and fss3_v is None:
                continue

            if fss0_v is not None:
                is_upper0.append([fss0_v > eq_v, key, epsilon])
            if fss1_v is not None:
                is_upper1.append([fss1_v > eq_v, key, epsilon])
            if fss2_v is not None:
                is_upper2.append([fss2_v > eq_v, key, epsilon])
            if fss3_v is not None:
                is_upper3.append([fss3_v > eq_v, key, epsilon])

        for key in proto.keys():
            proto_v = proto[key]
            fss4_v = None
            if key in fss4.keys():
                fss4_v = fss4[key]
            fss5_v = None
            if key in fss5.keys():
                fss5_v = fss5[key]
            fss6_v = None
            if key in fss6.keys():
                fss6_v = fss6[key]
            fss7_v = None
            if key in fss7.keys():
                fss7_v = fss7[key]

            if fss4_v is None and fss5_v is None and fss6_v is None and fss7_v is None:
                continue

            if fss4_v is not None:
                is_under0.append([fss4_v < proto_v, key, epsilon])
            if fss5_v is not None:
                is_under1.append([fss5_v < proto_v, key, epsilon])
            if fss6_v is not None:
                is_under2.append([fss6_v < proto_v, key, epsilon])
            if fss7_v is not None:
                is_under3.append([fss7_v < proto_v, key, epsilon])

        for i in range(len(is_upper0) - 1):
            if is_upper0[i][0] != is_upper0[i + 1][0]:
                R.append(is_upper0[i])

        for i in range(len(is_upper1) - 1):
            if is_upper1[i][0] != is_upper1[i + 1][0]:
                R.append(is_upper1[i])

        for i in range(len(is_upper2) - 1):
            if is_upper2[i][0] != is_upper2[i + 1][0]:
                R.append(is_upper2[i])

        for i in range(len(is_upper3) - 1):
            if is_upper3[i][0] != is_upper3[i + 1][0]:
                R.append(is_upper3[i])

        for i in range(len(is_under0) - 1):
            if is_under0[i][0] != is_under0[i + 1][0]:
                S.append(is_under0[i])

        for i in range(len(is_under1) - 1):
            if is_under1[i][0] != is_under1[i + 1][0]:
                S.append(is_under1[i])

        for i in range(len(is_under2) - 1):
            if is_under2[i][0] != is_under2[i + 1][0]:
                S.append(is_under2[i])

        for i in range(len(is_under3) - 1):
            if is_under3[i][0] != is_under3[i + 1][0]:
                S.append(is_under3[i])

    values = convert_dict_to_lists(values)

    xR = list(map(lambda x: x[1], R))
    yR = list(map(lambda x: x[2], R))
    xS = list(map(lambda x: x[1], S))
    yS = list(map(lambda x: x[2], S))

    (Plotter()
        .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
        .setup_x_label('$\\beta$', font_size=20, label_pad=0)
        .setup_x_ticks(font_size=15)
        .setup_y_label('$\\varepsilon^*$', font_size=20, label_pad=12)
        .setup_y_ticks(font_size=15)
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        # .setup_title('Epsilon for $\\beta$-noise')
        # ._setup("$\\beta$", '$\\varepsilon^*$', 'linear', 'major', 'Epsilon for $\\beta$-noise')
        .scatter(xR, yR, '.', 'red')
        .scatter(xS, yS, '.', 'navy')
        .show())

    plotter = (Plotter()
               ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium')
               .scatter(values[0], values[1], ',', 'steelblue')
               .plot_line(source1[0], ',', 'red')
               .plot_line(source1[1], ',', 'deeppink')
               .plot_line(source1[2], ',', 'green'))

    for line in source2:
        plotter.plot_line(line, ',', 'orange')

    plotter.show_last()


def critical_intensity_alpha_noise():
    step = 0.001
    p_range = np.arange(0.22, 0.582355932, step)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )

    epsilon_ = 0.005

    source1 = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, step),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values
    )

    source2 = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
        m=lambda a, b, x: functions_a_noise.m(a, b, x, epsilon_),
        epsilon=epsilon_,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_a_noise.s(1, b, x, epsilon_),
        q=lambda b, x: functions_a_noise.q(1, b, x, epsilon_),
        q_=functions_a_noise._q,
        s_=functions_a_noise._s
    )

    R = []
    S = []
    for epsilon in np.arange(0.001, 1.5, step):
        print("Epsilon = ", epsilon)
        source0 = bifurcation_with_ssf(
            values=values,
            b_range=p_range,
            a=1,
            borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
            m=lambda a, b, x: functions_a_noise.m(a, b, x, epsilon),
            epsilon=epsilon,
            f=lambda b, x: function.f(1, b, x),
            s=lambda b, x: functions_a_noise.s(1, b, x, epsilon),
            q=lambda b, x: functions_a_noise.q(1, b, x, epsilon),
            q_=functions_a_noise._q,
            s_=functions_a_noise._s
        )

        equilibrium_ = []
        for line in source1:
            equilibrium_.append(convert_line_to_dict(line))

        fss_ = []
        for line in source0:
            fss_.append(convert_line_to_dict(line))

        is_upper0 = []
        is_upper1 = []
        is_upper2 = []
        is_upper3 = []

        is_under0 = []
        is_under1 = []
        is_under2 = []
        is_under3 = []

        eq = equilibrium_[0]
        proto = equilibrium_[2]

        fss0 = fss_[0]
        fss1 = fss_[3]
        fss2 = fss_[7]
        fss3 = fss_[14]

        fss4 = fss_[1]
        fss5 = fss_[4]
        fss6 = fss_[10]
        fss7 = fss_[15]

        for key in eq.keys():
            eq_v = eq[key]
            fss0_v = None
            if key in fss0.keys():
                fss0_v = fss0[key]
            fss1_v = None
            if key in fss1.keys():
                fss1_v = fss1[key]
            fss2_v = None
            if key in fss2.keys():
                fss2_v = fss2[key]
            fss3_v = None
            if key in fss3.keys():
                fss3_v = fss3[key]

            if fss0_v is None and fss1_v is None and fss2_v is None and fss3_v is None:
                continue

            if fss0_v is not None:
                is_upper0.append([fss0_v > eq_v, key, epsilon])
            if fss1_v is not None:
                is_upper1.append([fss1_v > eq_v, key, epsilon])
            if fss2_v is not None:
                is_upper2.append([fss2_v > eq_v, key, epsilon])
            if fss3_v is not None:
                is_upper3.append([fss3_v > eq_v, key, epsilon])

        for key in proto.keys():
            proto_v = proto[key]
            fss4_v = None
            if key in fss4.keys():
                fss4_v = fss4[key]
            fss5_v = None
            if key in fss5.keys():
                fss5_v = fss5[key]
            fss6_v = None
            if key in fss6.keys():
                fss6_v = fss6[key]
            fss7_v = None
            if key in fss7.keys():
                fss7_v = fss7[key]

            if fss4_v is None and fss5_v is None and fss6_v is None and fss7_v is None:
                continue

            if fss4_v is not None:
                is_under0.append([fss4_v < proto_v, key, epsilon])
            if fss5_v is not None:
                is_under1.append([fss5_v < proto_v, key, epsilon])
            if fss6_v is not None:
                is_under2.append([fss6_v < proto_v, key, epsilon])
            if fss7_v is not None:
                is_under3.append([fss7_v < proto_v, key, epsilon])

        for i in range(len(is_upper0) - 1):
            if is_upper0[i][0] != is_upper0[i + 1][0]:
                R.append(is_upper0[i])

        for i in range(len(is_upper1) - 1):
            if is_upper1[i][0] != is_upper1[i + 1][0]:
                R.append(is_upper1[i])

        for i in range(len(is_upper2) - 1):
            if is_upper2[i][0] != is_upper2[i + 1][0]:
                R.append(is_upper2[i])

        for i in range(len(is_upper3) - 1):
            if is_upper3[i][0] != is_upper3[i + 1][0]:
                R.append(is_upper3[i])

        for i in range(len(is_under0) - 1):
            if is_under0[i][0] != is_under0[i + 1][0]:
                S.append(is_under0[i])

        for i in range(len(is_under1) - 1):
            if is_under1[i][0] != is_under1[i + 1][0]:
                S.append(is_under1[i])

        for i in range(len(is_under2) - 1):
            if is_under2[i][0] != is_under2[i + 1][0]:
                S.append(is_under2[i])

        for i in range(len(is_under3) - 1):
            if is_under3[i][0] != is_under3[i + 1][0]:
                S.append(is_under3[i])

    values = convert_dict_to_lists(values)

    xR = list(map(lambda x: x[1], R))
    yR = list(map(lambda x: x[2], R))
    xS = list(map(lambda x: x[1], S))
    yS = list(map(lambda x: x[2], S))

    (Plotter()
        .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
        .setup_x_label('$\\beta$', font_size=20, label_pad=0)
        .setup_x_ticks(font_size=15)
        .setup_y_label('$\\varepsilon^*$', font_size=20, label_pad=12)
        .setup_y_ticks(font_size=15)
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        # .setup_title('Epsilon for $\\alpha$-noise')
        # ._setup("$\\beta$", '$\\varepsilon^*$', 'linear', 'major', 'Epsilon for $\\alpha$-noise')
        .scatter(xR, yR, '.', 'red')
        .scatter(xS, yS, '.', 'navy')
        .show())

    plotter = (Plotter()
               ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium')
               .scatter(values[0], values[1], ',', 'steelblue')
               .plot_line(source1[0], ',', 'red')
               .plot_line(source1[1], ',', 'deeppink')
               .plot_line(source1[2], ',', 'green'))

    for line in source2:
        plotter.plot_line(line, ',', 'orange')

    plotter.show()
    # plotter.show_last()


def critical_intensity_additive_noise():
    step = 0.001
    p_range = np.arange(0.22, 0.582355932, step)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )

    epsilon_ = 0.005

    source1 = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, step),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values
    )

    source2 = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
        m=lambda a, b, x: functions_additive_noise.m(a, b, x, epsilon_),
        epsilon=epsilon_,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_additive_noise.s(1, b, x, epsilon_),
        q=lambda b, x: functions_additive_noise.q(1, b, x, epsilon_),
        q_=functions_additive_noise._q,
        s_=functions_additive_noise._s
    )

    R = []
    S = []
    for epsilon in np.arange(0.001, 1, step):
        print("Epsilon = ", epsilon)
        source0 = bifurcation_with_ssf(
            values=values,
            b_range=p_range,
            a=1,
            borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.37], [0.22, 0.34]],
            m=lambda a, b, x: functions_additive_noise.m(a, b, x, epsilon),
            epsilon=epsilon,
            f=lambda b, x: function.f(1, b, x),
            s=lambda b, x: functions_additive_noise.s(1, b, x, epsilon),
            q=lambda b, x: functions_additive_noise.q(1, b, x, epsilon),
            q_=functions_additive_noise._q,
            s_=functions_additive_noise._s
        )

        equilibrium_ = []
        for line in source1:
            equilibrium_.append(convert_line_to_dict(line))

        fss_ = []
        for line in source0:
            fss_.append(convert_line_to_dict(line))

        is_upper0 = []
        is_upper1 = []
        is_upper2 = []
        is_upper3 = []

        is_under0 = []
        is_under1 = []
        is_under2 = []
        is_under3 = []

        eq = equilibrium_[0]
        proto = equilibrium_[2]

        fss0 = fss_[0]
        fss1 = fss_[3]
        fss2 = fss_[7]
        fss3 = fss_[14]

        fss4 = fss_[1]
        fss5 = fss_[4]
        fss6 = fss_[10]
        fss7 = fss_[15]

        for key in eq.keys():
            eq_v = eq[key]
            fss0_v = None
            if key in fss0.keys():
                fss0_v = fss0[key]
            fss1_v = None
            if key in fss1.keys():
                fss1_v = fss1[key]
            fss2_v = None
            if key in fss2.keys():
                fss2_v = fss2[key]
            fss3_v = None
            if key in fss3.keys():
                fss3_v = fss3[key]

            if fss0_v is None and fss1_v is None and fss2_v is None and fss3_v is None:
                continue

            if fss0_v is not None:
                is_upper0.append([fss0_v > eq_v, key, epsilon])
            if fss1_v is not None:
                is_upper1.append([fss1_v > eq_v, key, epsilon])
            if fss2_v is not None:
                is_upper2.append([fss2_v > eq_v, key, epsilon])
            if fss3_v is not None:
                is_upper3.append([fss3_v > eq_v, key, epsilon])

        for key in proto.keys():
            proto_v = proto[key]
            fss4_v = None
            if key in fss4.keys():
                fss4_v = fss4[key]
            fss5_v = None
            if key in fss5.keys():
                fss5_v = fss5[key]
            fss6_v = None
            if key in fss6.keys():
                fss6_v = fss6[key]
            fss7_v = None
            if key in fss7.keys():
                fss7_v = fss7[key]

            if fss4_v is None and fss5_v is None and fss6_v is None and fss7_v is None:
                continue

            if fss4_v is not None:
                is_under0.append([fss4_v < proto_v, key, epsilon])
            if fss5_v is not None:
                is_under1.append([fss5_v < proto_v, key, epsilon])
            if fss6_v is not None:
                is_under2.append([fss6_v < proto_v, key, epsilon])
            if fss7_v is not None:
                is_under3.append([fss7_v < proto_v, key, epsilon])

        for i in range(len(is_upper0) - 1):
            if is_upper0[i][0] != is_upper0[i + 1][0]:
                R.append(is_upper0[i])

        for i in range(len(is_upper1) - 1):
            if is_upper1[i][0] != is_upper1[i + 1][0]:
                R.append(is_upper1[i])

        for i in range(len(is_upper2) - 1):
            if is_upper2[i][0] != is_upper2[i + 1][0]:
                R.append(is_upper2[i])

        for i in range(len(is_upper3) - 1):
            if is_upper3[i][0] != is_upper3[i + 1][0]:
                R.append(is_upper3[i])

        for i in range(len(is_under0) - 1):
            if is_under0[i][0] != is_under0[i + 1][0]:
                S.append(is_under0[i])

        for i in range(len(is_under1) - 1):
            if is_under1[i][0] != is_under1[i + 1][0]:
                S.append(is_under1[i])

        for i in range(len(is_under2) - 1):
            if is_under2[i][0] != is_under2[i + 1][0]:
                S.append(is_under2[i])

        for i in range(len(is_under3) - 1):
            if is_under3[i][0] != is_under3[i + 1][0]:
                S.append(is_under3[i])

    values = convert_dict_to_lists(values)

    xR = list(map(lambda x: x[1], R))
    yR = list(map(lambda x: x[2], R))
    xS = list(map(lambda x: x[1], S))
    yS = list(map(lambda x: x[2], S))

    (Plotter()
        .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
        .setup_x_label('$\\beta$', font_size=20, label_pad=0)
        .setup_x_ticks(font_size=15)
        .setup_y_label('$\\varepsilon^*$', font_size=20, label_pad=12)
        .setup_y_ticks(font_size=15)
        .setup_y_scale(scale.linear)
        .setup_grid(grid.major)
        # .setup_title('Epsilon for additive noise')
        # ._setup("$\\beta$", '$\\varepsilon^*$', 'linear', 'major', 'Epsilon for additive noise')
        .scatter(xR, yR, '.', 'red')
        .scatter(xS, yS, '.', 'navy')
        .show())

    plotter = (Plotter()
               ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium')
               .scatter(values[0], values[1], ',', 'steelblue')
               .plot_line(source1[0], ',', 'red')
               .plot_line(source1[1], ',', 'deeppink')
               .plot_line(source1[2], ',', 'green'))

    for line in source2:
        plotter.plot_line(line, ',', 'orange')

    plotter.show_last()


def run_stochastic_sensitivity_b_noise_to_file():
    base_path = "C:\\Users\\lkora\\Desktop\\data\\b_noise\\"

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
    )
    source = m_b(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_b_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_b_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q(1, b, x, 0.001),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    prefix = "line"

    for i in range(len(source)):
        line = source[i]
        name = prefix + str(i) + ".txt"

        with open(base_path + name, 'w') as file:
            for j in range(len(line.x)):
                x = str(line.x[j])
                y = str(line.y[j])

                txt = str(x) + " " + str(y) + "\n"

                file.write(txt)


def run_stochastic_sensitivity_a_noise_to_file():
    base_path = "C:\\Users\\lkora\\Desktop\\data\\a_noise\\"

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
    )
    source = m_b(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_a_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_a_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_a_noise.q(1, b, x, 0.001),
        q_=functions_a_noise._q,
        s_=functions_a_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    prefix = "line"

    for i in range(len(source)):
        line = source[i]
        name = prefix + str(i) + ".txt"

        with open(base_path + name, 'w') as file:
            for j in range(len(line.x)):
                x = str(line.x[j])
                y = str(line.y[j])

                txt = str(x) + " " + str(y) + "\n"

                file.write(txt)


def run_stochastic_sensitivity_additive_noise_to_file():
    base_path = "C:\\Users\\lkora\\Desktop\\data\\additive_noise\\"

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
    )
    source = m_b(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.36,
        right3=0.37,
        left4=0.22,
        right4=0.34,
        m=lambda a, b, x: functions_additive_noise.m(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_additive_noise.s(1, b, x, 0.001),
        q=lambda b, x: functions_additive_noise.q(1, b, x, 0.001),
        q_=functions_additive_noise._q,
        s_=functions_additive_noise._s,
        f=lambda b, x: function.f(1, b, x)
    )

    prefix = "line"

    for i in range(len(source)):
        line = source[i]
        name = prefix + str(i) + ".txt"

        with open(base_path + name, 'w') as file:
            for j in range(len(line.x)):
                x = str(line.x[j])
                y = str(line.y[j])

                txt = str(x) + " " + str(y) + "\n"

                file.write(txt)
