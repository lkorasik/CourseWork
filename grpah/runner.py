import numpy as np

import functions
from new.builder.bifurcation import bifurcation
from new.builder.bifurcation_with_c import bifurcation_with_c
from new.builder.converter import convert_dict_to_lists
from new.builder.time_series import time_series
from plotter import Plotter


def run_time_series():
    source = time_series(
        time_range=range(1, 50 + 1),
        x_start=1.3,
        f=lambda x: functions.f(1, 0.56, x),
        skip=False
    )

    Plotter()\
        .setup('t', 'x', 'linear', 'major', 'Time series')\
        .plot(source[0], source[1], '*', 'steelblue')\
        .show_last()


def run_bifurcation():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
    )

    source = convert_dict_to_lists(source)

    Plotter()\
        .setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')\
        .scatter(source[0], source[1], '.', 'steelblue')\
        .show_last()


def run_bifurcation_with_c():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x)
    )

    draw_x, draw_y = convert_dict_to_lists(source)

    source = bifurcation_with_c(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        left=0,
        right=1,
        step=0.0001,
        f=lambda b, x: functions.f(1, b, x),
        draw_x=draw_x,
        draw_y=draw_y
    )

    Plotter()\
        .setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')\
        .scatter(source[0][0], source[0][1], '.', 'steelblue')\
        .plot(source[1][0], source[1][1], ',', 'red')\
        .plot(source[2][0], source[2][1], ',', 'red')\
        .show_last()
