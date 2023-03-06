import numpy as np

from core.algorithms.old.bifurcation import bifurcation
from algorithms.m_b import m_b
from models.hassel import function, functions_additive_noise
from models.hassel import functions_b_noise, functions_a_noise
from visual.plotter import Plotter
from visual.values import scale, grid


def beta_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.__f(1, b, x),
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
        f=lambda b, x: function.__f(1, b, x)
    )

    plotter = (Plotter()
               .setup_x_label("$\\beta$")
               .setup_y_label("M")
               .setup_y_scale(scale.linear)
               .setup_grid(grid.major)
               .setup_title('Stochastic sensetivity $\\beta$-noise'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.plot(source[0].x, source[0].y, ',', 'orange')
    plotter.plot(source[2].x, source[2].y, ',', 'orange')
    plotter.plot(source[4].x, source[4].y, ',', 'orange')
    plotter.plot(source[7].x, source[7].y, ',', 'orange')

    plotter.show_last()
    # plotter.show()


def alpha_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.__f(1, b, x),
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
        f=lambda b, x: function.__f(1, b, x)
    )

    plotter = (Plotter()
               .setup_x_label("$\\beta$")
               .setup_y_label("M")
               .setup_y_scale(scale.linear)
               .setup_grid(grid.major)
               .setup_title('Stochastic sensetivity $\\alpha$-noise'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()
    # plotter.show()


def additive_noise():
    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: function.__f(1, b, x),
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
        f=lambda b, x: function.__f(1, b, x)
    )

    plotter = (Plotter()
               .setup_x_label("$\\beta$")
               .setup_y_label("M")
               .setup_y_scale(scale.linear)
               .setup_grid(grid.major)
               .setup_title('Stochastic sensetivity additive-noise'))

    for line in source:
        plotter.plot(line.x, line.y, ',', 'red')

    plotter.show_last()
