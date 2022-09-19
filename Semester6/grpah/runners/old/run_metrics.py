import numpy as np

from algorithms.bifurcation_with_equilibrium import bifurcation_with_equilibrium
from algorithms.m_b import m_b
from core.algorithms.old.bifurcation import bifurcation
from core.utils.convert_line_to_dict import convert_line_to_dict
from models.hassel import function, functions_additive_noise
from models.hassel import functions_b_noise, functions_a_noise
from visual.line import Line
from visual.plotter import Plotter
from visual.values import grid


def machalanobis_alpha_noise():
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
        function=lambda b, x: function.h(1, b, x),
        d_function=lambda b, x: function.h_dx(1, b, x),
        # d_function=lambda b, x: hassel.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: hassel.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: hassel.df(1, b, x),
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

    plotter = (Plotter()
               .adjust(top=0.9, bottom=0.13, left=0.17, right=0.945)
               .setup_x_label('$\\beta$', font_size=20, label_pad=0)
               .setup_x_ticks(font_size=15)
               .setup_y_label('$d_M$', font_size=20, label_pad=12)
               .setup_y_ticks(font_size=15)
               .setup_grid(grid.major))

    # plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Mahalanobis metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    plotter.show_last()
    # plotter.show()


def machalanobis_beta_noise():
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
        function=lambda b, x: function.h(1, b, x),
        d_function=lambda b, x: function.h_dx(1, b, x),
        # d_function=lambda b, x: hassel.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: hassel.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: hassel.df(1, b, x),
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

    plotter = (Plotter()
               .adjust(top=0.9, bottom=0.13, left=0.17, right=0.945)
               .setup_x_label('$\\beta$', font_size=20, label_pad=0)
               .setup_x_ticks(font_size=15)
               .setup_y_label('$d_M$', font_size=20, label_pad=12)
               .setup_y_ticks(font_size=15)
               .setup_grid(grid.major))

    # plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Mahalanobis metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    plotter.show_last()
    # plotter.show()


def machalanobis_additive_noise():
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
        function=lambda b, x: function.h(1, b, x),
        d_function=lambda b, x: function.h_dx(1, b, x),
        # d_function=lambda b, x: hassel.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: hassel.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: hassel.df(1, b, x),
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

    plotter = (Plotter()
               .adjust(top=0.9, bottom=0.13, left=0.17, right=0.945)
               .setup_x_label('$\\beta$', font_size=20, label_pad=0)
               .setup_x_ticks(font_size=15)
               .setup_y_label('$d_M$', font_size=20, label_pad=12)
               .setup_y_ticks(font_size=15)
               .setup_grid(grid.major))

    # plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Mahalanobis metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    plotter.show_last()
    # plotter.show()


def euclid_beta_noise():
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
        function=lambda b, x: function.h(1, b, x),
        d_function=lambda b, x: function.h_dx(1, b, x),
        # d_function=lambda b, x: hassel.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: hassel.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: hassel.df(1, b, x),
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

    plotter = (Plotter()
               .adjust(top=0.9, bottom=0.13, left=0.17, right=0.945)
               .setup_x_label('$\\beta$', font_size=20, label_pad=0)
               .setup_x_ticks(font_size=15)
               .setup_y_label('$d_E$', font_size=20, label_pad=12)
               .setup_y_ticks(font_size=15)
               .setup_grid(grid.major))

    # plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Euclid metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    plotter.show_last()


def euclid_alpha_noise():
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
        function=lambda b, x: function.h(1, b, x),
        d_function=lambda b, x: function.h_dx(1, b, x),
        # d_function=lambda b, x: hassel.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: hassel.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: hassel.df(1, b, x),
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

    plotter = (Plotter()
               .adjust(top=0.9, bottom=0.13, left=0.17, right=0.945)
               .setup_x_label('$\\beta$', font_size=20, label_pad=0)
               .setup_x_ticks(font_size=15)
               .setup_y_label('$d_E$', font_size=20, label_pad=12)
               .setup_y_ticks(font_size=15)
               .setup_grid(grid.major))

    # plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Euclid metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    plotter.show_last()


def euclid_additive_noise():
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
        function=lambda b, x: function.h(1, b, x),
        d_function=lambda b, x: function.h_dx(1, b, x),
        # d_function=lambda b, x: hassel.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: hassel.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: hassel.df(1, b, x),
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

    plotter = (Plotter()
               .adjust(top=0.9, bottom=0.13, left=0.17, right=0.945)
               .setup_x_label('$\\beta$', font_size=20, label_pad=0)
               .setup_x_ticks(font_size=15)
               .setup_y_label('$d_E$', font_size=20, label_pad=12)
               .setup_y_ticks(font_size=15)
               .setup_grid(grid.major))

    # plotter = (Plotter()._setup('$\\beta$', 'M', 'linear', 'major', 'Euclid metrics'))

    plotter.plot_line(mahalanobis0, '.', 'red')
    plotter.plot_line(mahalanobis1, '.', 'blue')

    plotter.show_last()
