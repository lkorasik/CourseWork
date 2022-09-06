import numpy as np

from core.algorithms.bifurcation import bifurcation
from algorithms.bifurcation_with_ssf import bifurcation_with_ssf
from core.utils.convert_dict_to_lists import convert_dict_to_lists
from functions import function, functions_a_noise, functions_additive_noise, functions_b_noise
from visual.plotter import Plotter
from visual.values import colors, grid, scale
from algorithms.m_b import m_b


def b_noise():
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
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.373], [0.22, 0.34]],
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


def b_noise_1():
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


def b_noise_2():
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
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.373], [0.22, 0.34]],
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


def b_noise_3():
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


def b_noise_4():
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


def a_noise():
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
               .setup_x_label("$\\beta$")
               .setup_y_label("x")
               .setup_y_scale(scale.log)
               .setup_grid(grid.major)
               .setup_title('Bifurcation with $\\alpha$-noise')
               .scatter(chaos[0], chaos[1], '.', colors.steel_blue))

    for line in source:
        plotter.plot(line.x, line.y, ',', colors.red)

    plotter.show_last()
    # plotter.show()


def additive_noise():
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
               .setup_x_label("$\\beta$")
               .setup_y_label("x")
               .setup_y_scale(scale.log)
               .setup_grid(grid.major)
               .setup_title('Bifurcation with additive nois')
               .scatter(chaos[0], chaos[1], '.', colors.steel_blue))

    for line in source:
        plotter.plot(line.x, line.y, ',', colors.red)

    plotter.show_last()


def b_noise_to_file():
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
        right3=0.375,
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


def a_noise_to_file():
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
        right3=0.375,
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


def additive_noise_to_file():
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
        right3=0.375,
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
