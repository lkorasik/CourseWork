import numpy as np

from new.builder import functions
from new.builder.lyapunov import lyapunov
from new.algorithms.bifurcation import bifurcation
from new.builder.bifurcation_with_equilibrium import bifurcation_with_equilibrium
from new.builder.bifurcation_with_absorbing_area import bifurcation_with_absorbing_area
from new.builder.bifurcation_with_ssf import bifurcation_with_ssf
from new.builder.converter import convert_dict_to_lists
from new.builder.cyclical_mean import cyclical_mean
from new.builder.cyclical_variance import cyclical_variance
from new.builder.equilibrium import equilibrium
from new.builder.lamerei import lamerei
from new.builder.m_b import m_b
from new.builder.mean import mean
from new.builder.time_series import time_series
from new.builder.variance import variance
from plotter import Plotter


def run_time_series():
    source = time_series(
        time_range=range(1, 50 + 1),
        x_start=1.3,
        f=lambda x: functions.f(1, 0.56, x),
        skip=False
    )

    Plotter()\
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


def run_time_series_3():
    source = time_series(
        time_range=range(1, 250 + 1),
        x_start=0.06,
        f=lambda x: functions.f(1, 0.56, x),
        skip=False
    )
    Plotter() \
        .setup('t', 'x', 'linear', 'major', 'Time series original') \
        .plot(source[0], source[1], '.', 'steelblue') \
        .show()

    source = time_series(
        time_range=range(1, 250 + 1),
        x_start=0.06,
        f=lambda x: functions.f_pb(1, 0.56, x, 0.004),
        skip=False
    )
    Plotter() \
        .setup('t', 'x', 'linear', 'major', 'Time series alpha') \
        .plot(source[0], source[1], '.', 'steelblue') \
        .show()

    source = time_series(
        time_range=range(1, 250 + 1),
        x_start=0.06,
        f=lambda x: functions.f_pa(1, 0.56, x, 0.004),
        skip=False
    )
    Plotter() \
        .setup('t', 'x', 'linear', 'major', 'Time series beta') \
        .plot(source[0], source[1], '.', 'steelblue') \
        .show()

    source = time_series(
        time_range=range(1, 250 + 1),
        x_start=0.06,
        f=lambda x: functions.f_pa(1, 0.56, x, 0.004),
        skip=False
    )
    Plotter() \
        .setup('t', 'x', 'linear', 'major', 'Time series addition') \
        .plot(source[0], source[1], '.', 'steelblue') \
        .show_last()


def run_bifurcation():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
    )

    source = convert_dict_to_lists(source)

    Plotter() \
        .setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation') \
        .scatter(source[0], source[1], '.', 'steelblue') \
        .show_last()


def run_bifurcation_2():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x)
    )
    source = convert_dict_to_lists(source)

    Plotter() \
        .setup('b', 'x', 'log', 'major', 'Bifurcation') \
        .scatter(source[0], source[1], '.', 'steelblue') \
        .show()

    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f_pa(1, b, x, 0.01)
    )
    source = convert_dict_to_lists(source)

    Plotter() \
        .setup('b', 'x', 'log', 'major', 'Bifurcation alpha') \
        .scatter(source[0], source[1], '.', 'steelblue') \
        .show()

    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f_pb(1, b, x, 0.03)
    )
    source = convert_dict_to_lists(source)

    Plotter() \
        .setup('b', 'x', 'log', 'major', 'Bifurcation beta') \
        .scatter(source[0], source[1], '.', 'steelblue') \
        .show()

    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f_p(1, b, x, 0.01)
    )
    source = convert_dict_to_lists(source)

    Plotter() \
        .setup('b', 'x', 'log', 'major', 'Bifurcation addition') \
        .scatter(source[0], source[1], '.', 'steelblue') \
        .show_last()


def run_bifurcation_with_absorbing_area():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
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
        p_range=np.arange(0.22, 0.582355932, 0.001),
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


def run_mean():
    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f(1, b, x)
    )
    source0 = mean(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.01)
    )
    source1 = mean(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.03)
    )
    source2 = mean(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.04)
    )
    source3 = mean(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    Plotter() \
        .setup('b', 'x', 'linear', 'major', 'EV') \
        .plot(source0[0], source0[1], '.', 'steelblue') \
        .plot(source1[0], source1[1], '.', 'red') \
        .plot(source2[0], source2[1], '.', 'green') \
        .plot(source3[0], source3[1], '.', 'black') \
        .show_last()


def run_cyclic_mean():
    source0 = cyclical_mean(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f(1, b, x),
        count=100
    )
    source1 = cyclical_mean(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.01),
        count=100
    )
    source2 = cyclical_mean(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.03),
        count=100
    )
    source3 = cyclical_mean(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.04),
        count=100
    )

    Plotter() \
        .setup('b', 'x', 'linear', 'major', 'EV cyclic') \
        .plot(source0[0], source0[1], '.', 'steelblue') \
        .plot(source1[0], source1[1], '.', 'red') \
        .plot(source2[0], source2[1], '.', 'green') \
        .plot(source3[0], source3[1], '.', 'black') \
        .show_last()


def run_variance():
    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f(1, b, x)
    )
    source0 = variance(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.01)
    )
    source1 = variance(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.03)
    )
    source2 = variance(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.04)
    )
    source3 = variance(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    Plotter() \
        .setup('b', 'x', 'linear', 'major', 'Variance') \
        .plot(source0[0], source0[1], '.', 'steelblue') \
        .plot(source1[0], source1[1], '.', 'red') \
        .plot(source2[0], source2[1], '.', 'green') \
        .plot(source3[0], source3[1], '.', 'black') \
        .show_last()


def run_cyclic_variance():
    source0 = cyclical_variance(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f(1, b, x),
        count=100
    )
    source1 = cyclical_variance(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.01),
        count=100
    )
    source2 = cyclical_variance(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.03),
        count=100
    )
    source3 = cyclical_variance(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.04),
        count=100
    )

    Plotter() \
        .setup('b', 'x', 'linear', 'major', 'Variance cyclic') \
        .plot(source0[0], source0[1], '.', 'steelblue') \
        .plot(source1[0], source1[1], '.', 'red') \
        .plot(source2[0], source2[1], '.', 'green') \
        .plot(source3[0], source3[1], '.', 'black') \
        .show_last()


def run_stochastoc_sensetivity():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.43,
        left3=0.22,
        right3=0.33,
        m=functions.m,
        m1=functions.m1,
        m2=functions.m2,
        epsilon=0.001,
        f=lambda b, x: functions.f(1, b, x),
        dfx=lambda b, x: functions.dfx2(1, b, x),
        s=lambda b, x: functions.s(1, b, x),
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f_pb(1, b, x, 0.001),
    )
    chaos = convert_dict_to_lists(chaos)

    Plotter()\
        .setup('b', 'x', 'log', 'major', 'Bifurcation')\
        .scatter(chaos[0], chaos[1], '.', 'steelblue')\
        .plot(source[0], source[1], '.', 'red')\
        .plot(source[0], source[2], '.', 'red')\
        .plot(source[3], source[4], '.', 'red')\
        .plot(source[3], source[5], '.', 'red')\
        .plot(source[3], source[6], '.', 'red')\
        .plot(source[3], source[7], '.', 'red')\
        .plot(source[8], source[9], '.', 'red')\
        .plot(source[8], source[10], '.', 'red')\
        .show_last()


def run_m_b():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.37, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
    )
    source = m_b(
        b_range=np.arange(0.37, 0.582355932, 0.001),
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.43,
        m=functions.m,
        m1=functions.m1,
        m2=functions.m2,
        values=values
    )

    Plotter()\
        .setup('b', 'M', 'linear', 'major', 'Stochastic sensetivity')\
        .scatter(source[0], source[1], '.', 'red')\
        .scatter(source[2], source[3], '.', 'red')\
        .scatter(source[4], source[5], '.', 'red')\
        .scatter(source[6], source[7], '.', 'red')\
        .show_last()
