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
from plotter import Plotter


def run_time_series():
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


def run_time_series_2():
    source = time_series(
        time_range=range(1, 50 + 1),
        x_start=2.1,
        f=lambda x: functions.f(1, 0.48, x),
        skip=False
    )

    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series')
        .plot(source[0], source[1], '*', 'steelblue')
        .show_last())


def run_time_series_3():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.004

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
        .setup('t', 'x', 'linear', 'major', 'Time series with beta noise')
        .plot(source[0], source[1], '.', 'steelblue')
        .show())

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions.f_pa(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
        .setup('t', 'x', 'linear', 'major', 'Time series with alpha noise')
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
        .scatter(source[0], source[1], '.', 'steelblue')
        .show_last())


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
        m=lambda a, b, x: functions_b_noise.m_chaos_b(a, b, x, 0.001),
        m1=lambda a, b, x1, x2: functions_b_noise.m1_chaos_b(a, b, x1, x2, 0.001),
        m2=lambda a, b, x1, x2: functions_b_noise.m2_chaos_b(a, b, x1, x2, 0.001),
        epsilon=0.001,
        f=lambda b, x: base_functions.f(1, b, x),
        s=lambda b, x: functions_b_noise.s_chaos_b(1, b, x, 0.001),
        q=lambda b, x: functions_b_noise.q_chaos_b(1, b, x, 0.001)
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f_pb(1, b, x, 0.001)
    )
    chaos = convert_dict_to_lists(chaos)

    (Plotter()
        .setup('b', 'x', 'log', 'major', 'Bifurcation, beta-noise')
        .scatter(chaos[0], chaos[1], '.', 'steelblue')
        .plot(source[0], source[1], ',', 'red')
        .plot(source[0], source[2], ',', 'red')
        .plot(source[3], source[4], ',', 'red')
        .plot(source[3], source[5], ',', 'red')
        .plot(source[3], source[6], ',', 'red')
        .plot(source[3], source[7], ',', 'red')
        .plot(source[8], source[9], ',', 'red')
        .plot(source[8], source[10], ',', 'red')
        .plot(source[8], source[11], ',', 'red')
        .plot(source[8], source[12], ',', 'red')
        .plot(source[8], source[13], ',', 'red')
        .plot(source[8], source[14], ',', 'red')
        .plot(source[8], source[15], ',', 'red')
        .plot(source[8], source[16], ',', 'red')
     # .show())
        .show_last())


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
        m1=lambda a, b, x1, x2: functions_a_noise.m1_chaos_a(a, b, x1, x2, 0.001),
        m2=lambda a, b, x1, x2: functions_a_noise.m2_chaos_a(a, b, x1, x2, 0.001),
        epsilon=0.001,
        f=lambda b, x: base_functions.f(1, b, x),
        s=lambda b, x: functions_a_noise.s_chaos_a(1, b, x, 0.001),
        q=lambda b, x: functions_a_noise.q_chaos_a(1, b, x, 0.001)
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f_pa(1, b, x, 0.001),
    )
    chaos = convert_dict_to_lists(chaos)

    (Plotter()
        .setup('b', 'x', 'log', 'major', 'Bifurcation, alpha-noise')
        .scatter(chaos[0], chaos[1], '.', 'steelblue')
        .plot(source[0], source[1], ',', 'red')
        .plot(source[0], source[2], ',', 'red')
        .plot(source[3], source[4], ',', 'red')
        .plot(source[3], source[5], ',', 'red')
        .plot(source[3], source[6], ',', 'red')
        .plot(source[3], source[7], ',', 'red')
        .plot(source[8], source[9], ',', 'red')
        .plot(source[8], source[10], ',', 'red')
     .show())
        # .show_last())


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
        m1=lambda a, b, x1, x2: functions_additive_noise.m1_chaos_b(a, b, x1, x2, 0.001),
        m2=lambda a, b, x1, x2: functions_additive_noise.m2_chaos_b(a, b, x1, x2, 0.001),
        epsilon=0.001,
        f=lambda b, x: base_functions.f(1, b, x),
        s=lambda b, x: functions_additive_noise.s_chaos(1, b, x, 0.001),
        q=lambda b, x: functions_additive_noise.q_chaos(1, b, x, 0.001)
    )
    chaos = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f_p(1, b, x, 0.001),
    )
    chaos = convert_dict_to_lists(chaos)

    (Plotter()
        .setup('b', 'x', 'log', 'major', 'Bifurcation, additive noise')
        .scatter(chaos[0], chaos[1], '.', 'steelblue')
        .plot(source[0], source[1], ',', 'red')
        .plot(source[0], source[2], ',', 'red')
        .plot(source[3], source[4], ',', 'red')
        .plot(source[3], source[5], ',', 'red')
        .plot(source[3], source[6], ',', 'red')
        .plot(source[3], source[7], ',', 'red')
        .plot(source[8], source[9], ',', 'red')
        .plot(source[8], source[10], ',', 'red')
        .show_last())


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
        right2=0.435,
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
