import numpy as np

import functions
from lyapunov import lyapunov
from new.builder.bifurcation import bifurcation
from new.builder.bifurcation_with_equilibrium import bifurcation_with_equilibrium
from new.builder.bifurcation_with_absorbing_area import bifurcation_with_absorbing_area
from new.builder.converter import convert_dict_to_lists
from new.builder.equilibrium import equilibrium
from new.builder.lamerei import lamerei
from new.builder.time_series import time_series
from plotter import Plotter


def run_time_series():
    source = time_series(
        time_range=range(1, 50 + 1),
        x_start=1.3,
        f=lambda x: functions.f(1, 0.56, x),
        skip=False
    )

    Plotter() \
        .setup('t', 'x', 'linear', 'major', 'Time series') \
        .plot(source[0], source[1], '*', 'steelblue') \
        .show_last()


def run_time_series_2():
    source = time_series(
        time_range=range(1, 50 + 1),
        x_start=2.1,
        f=lambda x: functions.f(1, 0.48, x),
        skip=False
    )

    Plotter() \
        .setup('t', 'x', 'linear', 'major', 'Time series') \
        .plot(source[0], source[1], '*', 'steelblue') \
        .show_last()


def run_bifurcation():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
    )

    source = convert_dict_to_lists(source)

    Plotter() \
        .setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation') \
        .scatter(source[0], source[1], '.', 'steelblue') \
        .show_last()


def run_bifurcation_with_absorbing_area():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x)
    )

    draw_x, draw_y = convert_dict_to_lists(source)

    source = bifurcation_with_absorbing_area(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        left=0,
        right=1,
        step=0.0001,
        f=lambda b, x: functions.f(1, b, x),
        draw_x=draw_x,
        draw_y=draw_y
    )

    Plotter() \
        .setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation') \
        .scatter(source[0][0], source[0][1], '.', 'steelblue') \
        .plot(source[1][0], source[1][1], ',', 'red') \
        .plot(source[2][0], source[2][1], ',', 'red') \
        .show_last()


def run_lyapunov():
    source = lyapunov(
        epsilon=10 ** (-5),
        b_range=np.arange(0.22, 0.582355932, 0.001),
        x_0=0.2,
        time_range=range(1, 100 + 1),
        T=100,
        f=lambda b, x: functions.f(1, b, x),
        lambda_=functions.lambda_
    )

    Plotter() \
        .setup(r'$\beta$', '$\lambda$', 'linear', 'major', 'Lyapunov') \
        .plot(source[0], source[1], ',', 'red') \
        .show_last()


def run_lamerei():
    source0 = lamerei(
        a=1,
        x_start=0.03,
        b=0.56,
        time_range=range(1, 100 + 1),
        skip=False,
        xmin=0.0,
        xmax=0.34,
        f=functions.f,
        g=functions.g
    )
    source1 = lamerei(
        a=1,
        x_start=0.1,
        b=0.56,
        time_range=range(1, 100 + 1),
        skip=False,
        xmin=0.0,
        xmax=0.34,
        f=functions.f,
        g=functions.g
    )
    source2 = lamerei(
        a=1,
        x_start=0.3,
        b=0.56,
        time_range=range(1, 100 + 1),
        skip=False,
        xmin=0.0,
        xmax=0.34,
        f=functions.f,
        g=functions.g
    )

    plotter = Plotter() \
        .setup('$x_t$', '$x_{t+1}$', 'linear', 'major', 'Lamerei')

    for i in source0[0]:
        plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')

    for i in source1[0]:
        plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')

    for i in source2[0]:
        plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')

    plotter \
        .plot(source0[1][0], source0[1][1], ',', 'steelblue') \
        .plot(source0[2][0], source0[2][1], ',', 'orange') \
        .show_last()


def run_bifurcation_with_equilibrium():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.1164711,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
    )

    source = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: functions.h(1, b, x),
        d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: functions.f(1, b, x),
        sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: functions.dsf(1, b, x),
        bifurcation=values
    )

    Plotter() \
        .setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium') \
        .scatter(source[0][0], source[0][1], '.', 'steelblue') \
        .plot(source[1][0], source[1][1], ',', 'red') \
        .plot(source[2][0], source[2][1], ',', 'deeppink') \
        .plot(source[3][0], source[3][1], ',', 'green') \
        .show_last()


def run_equilibrium():
    source = equilibrium(
        x12=0.12,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        precision=0.0000001,
        function=lambda b, x: functions.h(1, b, x),
        d_function=lambda b, x: functions.dh(1, b, x),
        d=lambda b, x: functions.df(1, b, x)
    )

    Plotter() \
        .setup('b', 'x', 'linear', 'major', 'Bifurcation with equilibrium') \
        .plot(source[0][0], source[0][1], ',', 'red') \
        .plot(source[1][0], source[1][1], ',', 'deeppink') \
        .plot(source[2][0], source[2][1], ',', 'green') \
        .plot(source[3][0], source[3][1], ',', 'black') \
        .plot(source[4][0], source[4][1], ',', 'black') \
        .show_last()
