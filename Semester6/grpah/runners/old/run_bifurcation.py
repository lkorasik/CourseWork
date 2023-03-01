import numpy as np

from core.algorithms.old.absorbing_area import absorbing_area
from core.algorithms.old.bifurcation import bifurcation
from algorithms.bifurcation_with_equilibrium import bifurcation_with_equilibrium
from core.utils.convert_dict_to_lists import convert_dict_to_lists
from models.hassel import function, functions_additive_noise
from models.hassel import functions_b_noise, functions_a_noise
from visual.plotter import Plotter
from visual.values import colors, grid, scale, markers


def without_chaos():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x)
    )

    source = convert_dict_to_lists(source)

    (Plotter()
     .setup_x_label('$\\beta$', font_size=14)
     .setup_y_label('x', label_pad=5, font_size=14)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     # .setup_title('Bifurcation')
     .setup_y_ticks(font_size=14)
     .setup_x_ticks(font_size=14)
     .scatter(source[0], source[1], '.', colors.steel_blue)
     # .show())
     .show_last())


def compare_chaos_bifurcation():
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


def with_absorbing_area():
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
     .setup_x_label('$\\beta$', font_size=14)
     .setup_y_label('x', label_pad=5, font_size=14)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_y_ticks(font_size=14)
     .setup_x_ticks(font_size=14)
     # .setup_title("Bifurcation")
     # ._setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')
     .scatter(draw_x, draw_y, '.', colors.steel_blue)
     .plot_line(source[0], markers.nothing, colors.red)
     .plot_line(source[1], markers.nothing, colors.red)
     .show_last())


def with_equilibrium():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.1164711,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.f(1, b, x),
        lower_bound=None
    )

    source = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: function.h(1, b, x),
        d_function=lambda b, x: function.h_dx(1, b, x),
        # d_function=lambda b, x: hassel.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: hassel.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: hassel.df(1, b, x),
        bifurcation=values
    )

    values = convert_dict_to_lists(values)

    (Plotter()
     .setup_x_label("$\\beta$", font_size=14)
     .setup_y_label('x', font_size=14)
     .setup_y_scale(scale.log)
     .setup_y_ticks(font_size=14)
     .setup_x_ticks(font_size=14)
     .setup_grid(grid.major)
     .setup_title('Bifurcation with equilibrium')
     .scatter(values[0], values[1], '.', colors.steel_blue)
     .plot_line(source[0], ',', colors.red)
     .plot_line(source[1], ',', colors.deep_pink)
     .plot_line(source[2], ',', colors.green)
     # .show())
     .show_last())
