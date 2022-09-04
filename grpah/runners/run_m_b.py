import numpy as np

from algorithms.bifurcation import bifurcation
from algorithms.m_b import m_b
from functions_pkg import functions_b_noise, function, functions_a_noise, functions_additive_noise
from visual.plotter import Plotter


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