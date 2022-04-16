import numpy as np

import functions
from algorithms.absorbing_area import absorbing_area
from algorithms.bifurcation import bifurcation
from old.converter import convert_dict_to_lists
from old.cyclical_mean import cyclical_mean
from old.cyclical_variance import cyclical_variance
from old.mean import mean
from old.variance import variance
from old.bifurcation_with_equilibrium import bifurcation_with_equilibrium
from old.bifurcation_with_ssf import bifurcation_with_ssf
from old.equilibrium import equilibrium
from old.lamerei import lamerei
from algorithms.lyapunov import lyapunov
from old.m_b import m_b
from algorithms.time_series import time_series
from functions_pkg import functions_b_noise, base_functions, functions_a_noise, functions_additive_noise
from visual.plotter import Plotter


def run_time_series_without_chaos_1():
    source = time_series(
        time_range=range(1, 50 + 1),
        x_start=1.3,
        f=lambda x: functions.f(1, 0.56, x),
        skip=False
    )

    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series')
        .plot(source[0], source[1], '*', 'steelblue')
        .show_last())


def run_time_series_without_chaos_composition():
    time_range = range(1, 30 + 1)
    a = 1
    b = 0.56

    source = time_series(
        time_range=time_range,
        x_start=1.3,
        f=lambda x: functions.f(a, b, x),
        skip=False
    )

    plotter = (Plotter()
               .setup('t', 'x', 'linear', 'major', 'Time series')
               .plot(source[0], source[1], '*', 'darkviolet', '1.3'))

    source = time_series(
        time_range=time_range,
        x_start=0.3,
        f=lambda x: functions.f(a, b, x),
        skip=False
    )

    plotter.plot(source[0], source[1], '*', 'darkslateblue', '0.3')

    source = time_series(
        time_range=time_range,
        x_start=0.06,
        f=lambda x: functions.f(a, b, x),
        skip=False
    )

    plotter.plot(source[0], source[1], '*', 'blue', '0.06')

    source = time_series(
        time_range=time_range,
        x_start=0.04,
        f=lambda x: functions.f(a, b, x),
        skip=False
    )

    (plotter
     .plot(source[0], source[1], '*', 'royalblue', '0.04')
     .legend()
     .show_last())


def run_time_series_different_noises():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.04

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions.f(a, b, x),
        skip=skip
    )
    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series original')
        .plot(source[0], source[1], '.', 'steelblue')
        .show())

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions.f_pb(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series with $\\beta$-noise')
        .plot(source[0], source[1], '.', 'steelblue')
        .show())

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions.f_pa(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series with $\\alpha$-noise')
        .plot(source[0], source[1], '.', 'steelblue')
        .show())

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions.f_p(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series with additive noise')
        .plot(source[0], source[1], '.', 'steelblue')
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
        f=lambda x: functions.f(a, b, x),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions.f(a, b, x),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions.f(a, b, x),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions.f(a, b, x),
        skip=skip
    )
    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series original')
        .plot(source0[0], source0[1], '.', 'lightcoral')
        .plot(source1[0], source1[1], '.', 'darkolivegreen')
        .plot(source2[0], source2[1], '.', 'olive')
        .plot(source3[0], source3[1], '.', 'teal')
        .show())
    # .show_last())

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions.f_pb(a, b, x, epsilon),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions.f_pb(a, b, x, epsilon),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions.f_pb(a, b, x, epsilon),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions.f_pb(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series with $\\beta$-noise')
        .plot(source0[0], source0[1], '.', 'lightcoral')
        .plot(source1[0], source1[1], '.', 'darkolivegreen')
        .plot(source2[0], source2[1], '.', 'olive')
        .plot(source3[0], source3[1], '.', 'teal')
        .show())

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions.f_pa(a, b, x, epsilon),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions.f_pa(a, b, x, epsilon),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions.f_pa(a, b, x, epsilon),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions.f_pa(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series with $\\alpha$-noise')
        .plot(source0[0], source0[1], '.', 'lightcoral')
        .plot(source1[0], source1[1], '.', 'darkolivegreen')
        .plot(source2[0], source2[1], '.', 'olive')
        .plot(source3[0], source3[1], '.', 'teal')
        .show())

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions.f_p(a, b, x, epsilon),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions.f_p(a, b, x, epsilon),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions.f_p(a, b, x, epsilon),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions.f_p(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series with additive noise')
        .plot(source0[0], source0[1], '.', 'lightcoral')
        .plot(source1[0], source1[1], '.', 'darkolivegreen')
        .plot(source2[0], source2[1], '.', 'olive')
        .plot(source3[0], source3[1], '.', 'teal')
        # .show())
    .show_last())


def run_bifurcation():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: base_functions.f(1, b, x)
    )

    source = convert_dict_to_lists(source)

    (Plotter()
        .setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')
        .scatter(source[0], source[1], '.', 'steelblue', 'aa')
        .legend()
     .show())
        # .show_last())


def run_compare_chaos_bifurcation():
    time_range = range(1, 100 + 1)
    x_start = 0.2
    p_range = np.arange(0.22, 0.582355932, 0.001)

    a = 1
    epsilon = 0.01

    source = bifurcation(
        time_range=time_range,
        x_start=x_start,
        p_range=p_range,
        f=lambda b, x: functions.f(a, b, x)
    )
    source = convert_dict_to_lists(source)

    (Plotter()
        .setup('b', 'x', 'log', 'major', 'Bifurcation')
        .scatter(source[0], source[1], '.', 'steelblue')
        .show())

    source = bifurcation(
        time_range=time_range,
        x_start=x_start,
        p_range=p_range,
        f=lambda b, x: functions.f_pa(a, b, x, epsilon)
    )
    source = convert_dict_to_lists(source)

    (Plotter()
        .setup('b', 'x', 'log', 'major', 'Bifurcation alpha')
        .scatter(source[0], source[1], '.', 'steelblue')
        .show())

    source = bifurcation(
        time_range=time_range,
        x_start=x_start,
        p_range=p_range,
        f=lambda b, x: functions.f_pb(a, b, x, epsilon)
    )
    source = convert_dict_to_lists(source)

    (Plotter()
        .setup('b', 'x', 'log', 'major', 'Bifurcation beta')
        .scatter(source[0], source[1], '.', 'steelblue')
        .show())

    source = bifurcation(
        time_range=time_range,
        x_start=x_start,
        p_range=p_range,
        f=lambda b, x: functions.f_p(a, b, x, epsilon)
    )
    source = convert_dict_to_lists(source)

    (Plotter()
        .setup('b', 'x', 'log', 'major', 'Bifurcation addition')
        .scatter(source[0], source[1], '.', 'steelblue')
        .show_last())


def run_bifurcation_with_absorbing_area():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    a = 1

    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions.f(a, b, x)
    )
    draw_x, draw_y = convert_dict_to_lists(source)

    source = absorbing_area(
        p_range=p_range,
        left=0,
        right=1,
        step=0.0001,
        f=lambda b, x: functions.f(a, b, x),
    )

    (Plotter()
        .setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')
        .scatter(draw_x, draw_y, '.', 'steelblue')
        .plot(source[0], source[1], ',', 'red')
        .plot(source[0], source[2], ',', 'red')
        .show_last())


def run_lyapunov():
    source = lyapunov(
        epsilon=10 ** (-5),
        b_range=np.arange(0.22, 0.582355932, 0.001),
        x_start=0.2,
        time_range=range(1, 100 + 1),
        T=100,
        f=lambda b, x: functions.f(1, b, x),
        lambda_=functions.lambda_
    )

    (Plotter()
        .setup(r'$\beta$', '$\lambda$', 'linear', 'major', 'Lyapunov')
        .plot(source[0], source[1], ',', 'red')
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
        f=lambda x: functions.f(a, b, x)
    )
    source1 = lamerei(
        x_start=0.1,
        time_range=time_range,
        skip=skip,
        f=lambda x: functions.f(a, b, x),
    )
    source2 = lamerei(
        x_start=0.3,
        time_range=time_range,
        skip=skip,
        f=lambda x: functions.f(a, b, x),
    )

    plotter = Plotter().setup('$x_t$', '$x_{t+1}$', 'linear', 'major', 'Lamerei')

    for lst in [source0, source1, source2]:
        for i in lst:
            plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')

    (plotter
        .plot(x_range, functions.g(a, x_range), ',', 'steelblue')
        .plot(x_range, functions.f(a, b, x_range), ',', 'orange')
        .show_last())


def run_bifurcation_with_equilibrium():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.1164711,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
        down_border=None
    )

    source = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, 0.001),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: functions.h(1, b, x),
        d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: functions.f(1, b, x),
        sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values
    )

    values = convert_dict_to_lists(values)

    (Plotter()
        .setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium')
        .scatter(values[0], values[1], '.', 'steelblue')
        .plot(source[0], source[1], ',', 'red')
        .plot(source[2], source[3], ',', 'deeppink')
        .plot(source[4], source[5], ',', 'green')
        .show_last())


def run_equilibrium():
    source = equilibrium(
        x12=0.12,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        precision=0.0000001,
        function=lambda b, x: functions.h(1, b, x),
        d_function=lambda b, x: functions.dh(1, b, x),
        d=lambda b, x: functions.df(1, b, x)
    )

    (Plotter()
        .setup('b', 'x', 'linear', 'major', 'Bifurcation with equilibrium')
        .plot(source[0], source[1], ',', 'red')
        .plot(source[2], source[3], ',', 'deeppink')
        .plot(source[4], source[5], ',', 'green')
        .plot(source[6], source[7], ',', 'black')
        .plot(source[8], source[9], ',', 'black')
        .show_last())


def run_mean():
    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f(1, b, x),
        up_border=10_000,
        down_border=None
    )
    source0 = mean(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.01),
        up_border=10_000,
        down_border=None
    )
    source1 = mean(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.03),
        up_border=10_000,
        down_border=None
    )
    source2 = mean(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.04),
        up_border=10_000,
        down_border=None
    )
    source3 = mean(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    (Plotter()
        .setup('b', 'x', 'linear', 'major', 'EV')
        .plot(source0[0], source0[1], '.', 'steelblue')
        .plot(source1[0], source1[1], '.', 'red')
        .plot(source2[0], source2[1], '.', 'green')
        .plot(source3[0], source3[1], '.', 'black')
        .show_last())


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

    (Plotter()
        .setup('b', 'x', 'linear', 'major', 'EV cyclic')
        .plot(source0[0], source0[1], '.', 'steelblue')
        .plot(source1[0], source1[1], '.', 'red')
        .plot(source2[0], source2[1], '.', 'green')
        .plot(source3[0], source3[1], '.', 'black')
        .show_last())


def run_variance():
    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f(1, b, x),
        down_border=None
    )
    source0 = variance(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.01),
        down_border=None
    )
    source1 = variance(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.03),
        down_border=None
    )
    source2 = variance(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    values = bifurcation(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.01),
        f=lambda b, x: functions.f_pb(1, b, x, 0.04),
        down_border=None
    )
    source3 = variance(
        b_range=np.arange(0.22, 0.582355932, 0.01),
        values=values
    )

    (Plotter()
        .setup('b', 'x', 'linear', 'major', 'Variance')
        .plot(source0[0], source0[1], '.', 'steelblue')
        .plot(source1[0], source1[1], '.', 'red')
        .plot(source2[0], source2[1], '.', 'green')
        .plot(source3[0], source3[1], '.', 'black')
        .show_last())


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

    (Plotter()
        .setup('b', 'x', 'linear', 'major', 'Variance cyclic')
        .plot(source0[0], source0[1], '.', 'steelblue')
        .plot(source1[0], source1[1], '.', 'red')
        .plot(source2[0], source2[1], '.', 'green')
        .plot(source3[0], source3[1], '.', 'black')
        .show_last())


def run_stochastic_sensitivity_b_noise():
    p_range = np.arange(0.22, 0.582355932, 0.001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.22,
        right3=0.34,
        left4=0.36,
        right4=0.37,
        m=lambda a, b, x: functions_b_noise.m_chaos_b(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: base_functions.f(1, b, x),
        s=lambda b, x: functions_b_noise.s_chaos_b(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q_chaos_b(1, b, x, 0.001),
        q_=functions_b_noise._q_bn,
        s_=functions_b_noise._s_bn
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions.f_pb(1, b, x, 0.001)
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
               .setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\beta$-noise')
               .scatter(chaos[0], chaos[1], '.', 'steelblue'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    # plotter.show_last()
    plotter.show()


def run_stochastic_sensitivity_b_noise_1():
    p_range = np.arange(0.35, 0.385, 0.0001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.22,
        right3=0.34,
        left4=0.36,
        right4=0.37,
        m=lambda a, b, x: functions_b_noise.m_chaos_b(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: base_functions.f(1, b, x),
        s=lambda b, x: functions_b_noise.s_chaos_b(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q_chaos_b(1, b, x, 0.001),
        q_=functions_b_noise._q_bn,
        s_=functions_b_noise._s_bn
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions.f_pb(1, b, x, 0.001)
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
               .setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\beta$-noise')
               .scatter(chaos[0], chaos[1], '.', 'steelblue'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    # plotter.show_last()
    plotter.show()


def run_stochastic_sensitivity_b_noise_2():
    p_range = np.arange(0.4, 0.6, 0.0001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.22,
        right3=0.34,
        left4=0.36,
        right4=0.37,
        m=lambda a, b, x: functions_b_noise.m_chaos_b(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: base_functions.f(1, b, x),
        s=lambda b, x: functions_b_noise.s_chaos_b(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q_chaos_b(1, b, x, 0.001),
        q_=functions_b_noise._q_bn,
        s_=functions_b_noise._s_bn
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions.f_pb(1, b, x, 0.001)
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
               .setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\beta$-noise')
               .scatter(chaos[0], chaos[1], '.', 'steelblue'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()
    # plotter.show()


def run_stochastic_sensitivity_b_noise_3():
    p_range = np.arange(0.22, 0.3, 0.0001)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.22,
        right3=0.34,
        left4=0.36,
        right4=0.37,
        m=lambda a, b, x: functions_b_noise.m_chaos_b(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: base_functions.f(1, b, x),
        s=lambda b, x: functions_b_noise.s_chaos_b(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q_chaos_b(1, b, x, 0.001),
        q_=functions_b_noise._q_bn,
        s_=functions_b_noise._s_bn
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: functions.f_pb(1, b, x, 0.001)
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
               .setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\beta$-noise')
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
        f=lambda b, x: functions.f(1, b, x),
    )
    source = bifurcation_with_ssf(
        values=values,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1,
        left1=0.44,
        right1=0.582355932,
        left2=0.379,
        right2=0.435,
        left3=0.22,
        right3=0.34,
        left4=0.36,
        right4=0.37,
        m=lambda a, b, x: functions_a_noise.m_chaos_a(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: base_functions.f(1, b, x),
        s=lambda b, x: functions_a_noise.s_chaos_a(1, b, x, 0.001),
        q=lambda b, x: functions_a_noise.q_chaos_a(1, b, x, 0.001),
        q_=functions_a_noise._q_ca,
        s_=functions_a_noise._s_ca
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f_pa(1, b, x, 0.001),
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
               .setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with $\\alpha$-noise')
               .scatter(chaos[0], chaos[1], '.', 'steelblue'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    # plotter.show_last()
    plotter.show()


def run_stochastic_sensitivity_additive_noise():
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
        right2=0.435,
        left3=0.22,
        right3=0.34,
        left4=0.36,
        right4=0.37,
        m=lambda a, b, x: functions_additive_noise.m_chaos(a, b, x, 0.001),
        epsilon=0.001,
        f=lambda b, x: base_functions.f(1, b, x),
        s=lambda b, x: functions_additive_noise.s_chaos(1, b, x, 0.001),
        q=lambda b, x: functions_additive_noise.q_chaos(1, b, x, 0.001),
        q_=functions_additive_noise._q_c,
        s_=functions_additive_noise._s_c
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f_p(1, b, x, 0.001),
    )
    chaos = convert_dict_to_lists(chaos)

    plotter = (Plotter()
               .setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with additive noise')
               .scatter(chaos[0], chaos[1], '.', 'steelblue'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()


def run_m_b_beta_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
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
        m=lambda a, b, x: functions_b_noise.m_chaos_b(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_b_noise.s_chaos_b(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q_chaos_b(1, b, x, 0.001),
        q_=functions_b_noise._q_bn,
        s_=functions_b_noise._s_bn,
        f=lambda b, x: base_functions.f(1, b, x)
    )

    plotter = (Plotter().setup('$\\beta$', 'M', 'linear', 'major', 'Stochastic sensetivity $\\beta$-noise'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    # plotter.show_last()
    plotter.show()


def run_m_b_alpha_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
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
        m=lambda a, b, x: functions_a_noise.m_chaos_a(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_a_noise.s_chaos_a(1, b, x, 0.001),
        q=lambda b, x: functions_a_noise.q_chaos_a(1, b, x, 0.001),
        q_=functions_a_noise._q_ca,
        s_=functions_a_noise._s_ca,
        f=lambda b, x: base_functions.f(1, b, x)
    )

    plotter = (Plotter().setup('$\\beta$', 'M', 'linear', 'major', 'Stochastic sensetivity $\\alpha$-noise'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    # plotter.show_last()
    plotter.show()


def run_m_b_additive_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
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
        m=lambda a, b, x: functions_additive_noise.m_chaos(a, b, x, 0),
        values=values,
        s=lambda b, x: functions_additive_noise.s_chaos(1, b, x, 0.001),
        q=lambda b, x: functions_additive_noise.q_chaos(1, b, x, 0.001),
        q_=functions_additive_noise._q_c,
        s_=functions_additive_noise._s_c,
        f=lambda b, x: base_functions.f(1, b, x)
    )

    plotter = (Plotter().setup('$\\beta$', 'M', 'linear', 'major', 'Stochastic sensetivity additive-noise'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()

