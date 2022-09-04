import numpy as np

from algorithms.bifurcation import bifurcation
from algorithms.bifurcation_with_equilibrium import bifurcation_with_equilibrium
from algorithms.bifurcation_with_ssf import bifurcation_with_ssf
from algorithms.convert_dict_to_lists import convert_dict_to_lists
from algorithms.convert_line_to_dict import convert_line_to_dict
from functions_pkg import functions_b_noise, function, functions_a_noise, functions_additive_noise, others
from visual.plotter import Plotter
from visual.values import grid, scale


def beta_noise():
    step = 0.001
    p_range = np.arange(0.22, 0.582355932, step)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )

    epsilon_ = 0.005

    source1 = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, step),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        dsf=lambda b, x: function.f_dx(1, b, x),
        bifurcation=values
    )

    source2 = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.375], [0.22, 0.34]],
        m=lambda a, b, x: functions_b_noise.m(a, b, x, epsilon_),
        epsilon=epsilon_,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_b_noise.s(1, b, x, epsilon_),
        q=lambda b, x: functions_b_noise.q(1, b, x, epsilon_),
        q_=functions_b_noise._q,
        s_=functions_b_noise._s
    )

    R = []
    S = []
    for epsilon in np.arange(0.001, 0.21, step):
        print("Epsilon = ", epsilon)
        source0 = bifurcation_with_ssf(
            values=values,
            b_range=p_range,
            a=1,
            borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.375], [0.22, 0.34]],
            m=lambda a, b, x: functions_b_noise.m(a, b, x, epsilon),
            epsilon=epsilon,
            f=lambda b, x: function.f(1, b, x),
            s=lambda b, x: functions_b_noise.s(1, b, x, epsilon),
            q=lambda b, x: functions_b_noise.q(1, b, x, epsilon),
            q_=functions_b_noise._q,
            s_=functions_b_noise._s
        )

        equilibrium_ = []
        for line in source1:
            equilibrium_.append(convert_line_to_dict(line))

        fss_ = []
        for line in source0:
            fss_.append(convert_line_to_dict(line))

        is_upper0 = []
        is_upper1 = []
        is_upper2 = []
        is_upper3 = []

        is_under0 = []
        is_under1 = []
        is_under2 = []
        is_under3 = []

        eq = equilibrium_[0]
        proto = equilibrium_[2]

        fss0 = fss_[0]
        fss1 = fss_[3]
        fss2 = fss_[7]
        fss3 = fss_[14]

        fss4 = fss_[1]
        fss5 = fss_[4]
        fss6 = fss_[10]
        fss7 = fss_[15]

        for key in eq.keys():
            eq_v = eq[key]
            fss0_v = None
            if key in fss0.keys():
                fss0_v = fss0[key]
            fss1_v = None
            if key in fss1.keys():
                fss1_v = fss1[key]
            fss2_v = None
            if key in fss2.keys():
                fss2_v = fss2[key]
            fss3_v = None
            if key in fss3.keys():
                fss3_v = fss3[key]

            if fss0_v is None and fss1_v is None and fss2_v is None and fss3_v is None:
                continue

            if fss0_v is not None:
                is_upper0.append([fss0_v > eq_v, key, epsilon])
            if fss1_v is not None:
                is_upper1.append([fss1_v > eq_v, key, epsilon])
            if fss2_v is not None:
                is_upper2.append([fss2_v > eq_v, key, epsilon])
            if fss3_v is not None:
                is_upper3.append([fss3_v > eq_v, key, epsilon])

        for key in proto.keys():
            proto_v = proto[key]
            fss4_v = None
            if key in fss4.keys():
                fss4_v = fss4[key]
            fss5_v = None
            if key in fss5.keys():
                fss5_v = fss5[key]
            fss6_v = None
            if key in fss6.keys():
                fss6_v = fss6[key]
            fss7_v = None
            if key in fss7.keys():
                fss7_v = fss7[key]

            if fss4_v is None and fss5_v is None and fss6_v is None and fss7_v is None:
                continue

            if fss4_v is not None:
                is_under0.append([fss4_v < proto_v, key, epsilon])
            if fss5_v is not None:
                is_under1.append([fss5_v < proto_v, key, epsilon])
            if fss6_v is not None:
                is_under2.append([fss6_v < proto_v, key, epsilon])
            if fss7_v is not None:
                is_under3.append([fss7_v < proto_v, key, epsilon])

        for i in range(len(is_upper0) - 1):
            if is_upper0[i][0] != is_upper0[i + 1][0]:
                R.append(is_upper0[i])

        for i in range(len(is_upper1) - 1):
            if is_upper1[i][0] != is_upper1[i + 1][0]:
                R.append(is_upper1[i])

        for i in range(len(is_upper2) - 1):
            if is_upper2[i][0] != is_upper2[i + 1][0]:
                R.append(is_upper2[i])

        for i in range(len(is_upper3) - 1):
            if is_upper3[i][0] != is_upper3[i + 1][0]:
                R.append(is_upper3[i])

        for i in range(len(is_under0) - 1):
            if is_under0[i][0] != is_under0[i + 1][0]:
                S.append(is_under0[i])

        for i in range(len(is_under1) - 1):
            if is_under1[i][0] != is_under1[i + 1][0]:
                S.append(is_under1[i])

        for i in range(len(is_under2) - 1):
            if is_under2[i][0] != is_under2[i + 1][0]:
                S.append(is_under2[i])

        for i in range(len(is_under3) - 1):
            if is_under3[i][0] != is_under3[i + 1][0]:
                S.append(is_under3[i])

    values = convert_dict_to_lists(values)

    xR = list(map(lambda x: x[1], R))
    yR = list(map(lambda x: x[2], R))
    xS = list(map(lambda x: x[1], S))
    yS = list(map(lambda x: x[2], S))

    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
     .setup_x_label('$\\beta$', font_size=20, label_pad=0)
     .setup_x_ticks(font_size=15)
     .setup_y_label('$\\varepsilon^*$', font_size=20, label_pad=12)
     .setup_y_ticks(font_size=15)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('Epsilon for $\\beta$-noise')
     # ._setup("$\\beta$", '$\\varepsilon^*$', 'linear', 'major', 'Epsilon for $\\beta$-noise')
     .scatter(xR, yR, '.', 'red')
     .scatter(xS, yS, '.', 'navy')
     .show())

    plotter = (Plotter()
               ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium')
               .scatter(values[0], values[1], ',', 'steelblue')
               .plot_line(source1[0], ',', 'red')
               .plot_line(source1[1], ',', 'deeppink')
               .plot_line(source1[2], ',', 'green'))

    for line in source2:
        plotter.plot_line(line, ',', 'orange')

    plotter.show_last()
    # plotter.show()


def alpha_noise():
    step = 0.001
    p_range = np.arange(0.22, 0.582355932, step)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )

    epsilon_ = 0.005

    source1 = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, step),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values
    )

    source2 = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.375], [0.22, 0.34]],
        m=lambda a, b, x: functions_a_noise.m(a, b, x, epsilon_),
        epsilon=epsilon_,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_a_noise.s(1, b, x, epsilon_),
        q=lambda b, x: functions_a_noise.q(1, b, x, epsilon_),
        q_=functions_a_noise._q,
        s_=functions_a_noise._s
    )

    R = []
    S = []
    for epsilon in np.arange(0.001, 1.5, step):
        print("Epsilon = ", epsilon)
        source0 = bifurcation_with_ssf(
            values=values,
            b_range=p_range,
            a=1,
            borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.375], [0.22, 0.34]],
            m=lambda a, b, x: functions_a_noise.m(a, b, x, epsilon),
            epsilon=epsilon,
            f=lambda b, x: function.f(1, b, x),
            s=lambda b, x: functions_a_noise.s(1, b, x, epsilon),
            q=lambda b, x: functions_a_noise.q(1, b, x, epsilon),
            q_=functions_a_noise._q,
            s_=functions_a_noise._s
        )

        equilibrium_ = []
        for line in source1:
            equilibrium_.append(convert_line_to_dict(line))

        fss_ = []
        for line in source0:
            fss_.append(convert_line_to_dict(line))

        is_upper0 = []
        is_upper1 = []
        is_upper2 = []
        is_upper3 = []

        is_under0 = []
        is_under1 = []
        is_under2 = []
        is_under3 = []

        eq = equilibrium_[0]
        proto = equilibrium_[2]

        fss0 = fss_[0]
        fss1 = fss_[3]
        fss2 = fss_[7]
        fss3 = fss_[14]

        fss4 = fss_[1]
        fss5 = fss_[4]
        fss6 = fss_[10]
        fss7 = fss_[15]

        for key in eq.keys():
            eq_v = eq[key]
            fss0_v = None
            if key in fss0.keys():
                fss0_v = fss0[key]
            fss1_v = None
            if key in fss1.keys():
                fss1_v = fss1[key]
            fss2_v = None
            if key in fss2.keys():
                fss2_v = fss2[key]
            fss3_v = None
            if key in fss3.keys():
                fss3_v = fss3[key]

            if fss0_v is None and fss1_v is None and fss2_v is None and fss3_v is None:
                continue

            if fss0_v is not None:
                is_upper0.append([fss0_v > eq_v, key, epsilon])
            if fss1_v is not None:
                is_upper1.append([fss1_v > eq_v, key, epsilon])
            if fss2_v is not None:
                is_upper2.append([fss2_v > eq_v, key, epsilon])
            if fss3_v is not None:
                is_upper3.append([fss3_v > eq_v, key, epsilon])

        for key in proto.keys():
            proto_v = proto[key]
            fss4_v = None
            if key in fss4.keys():
                fss4_v = fss4[key]
            fss5_v = None
            if key in fss5.keys():
                fss5_v = fss5[key]
            fss6_v = None
            if key in fss6.keys():
                fss6_v = fss6[key]
            fss7_v = None
            if key in fss7.keys():
                fss7_v = fss7[key]

            if fss4_v is None and fss5_v is None and fss6_v is None and fss7_v is None:
                continue

            if fss4_v is not None:
                is_under0.append([fss4_v < proto_v, key, epsilon])
            if fss5_v is not None:
                is_under1.append([fss5_v < proto_v, key, epsilon])
            if fss6_v is not None:
                is_under2.append([fss6_v < proto_v, key, epsilon])
            if fss7_v is not None:
                is_under3.append([fss7_v < proto_v, key, epsilon])

        for i in range(len(is_upper0) - 1):
            if is_upper0[i][0] != is_upper0[i + 1][0]:
                R.append(is_upper0[i])

        for i in range(len(is_upper1) - 1):
            if is_upper1[i][0] != is_upper1[i + 1][0]:
                R.append(is_upper1[i])

        for i in range(len(is_upper2) - 1):
            if is_upper2[i][0] != is_upper2[i + 1][0]:
                R.append(is_upper2[i])

        for i in range(len(is_upper3) - 1):
            if is_upper3[i][0] != is_upper3[i + 1][0]:
                R.append(is_upper3[i])

        for i in range(len(is_under0) - 1):
            if is_under0[i][0] != is_under0[i + 1][0]:
                S.append(is_under0[i])

        for i in range(len(is_under1) - 1):
            if is_under1[i][0] != is_under1[i + 1][0]:
                S.append(is_under1[i])

        for i in range(len(is_under2) - 1):
            if is_under2[i][0] != is_under2[i + 1][0]:
                S.append(is_under2[i])

        for i in range(len(is_under3) - 1):
            if is_under3[i][0] != is_under3[i + 1][0]:
                S.append(is_under3[i])

    values = convert_dict_to_lists(values)

    xR = list(map(lambda x: x[1], R))
    yR = list(map(lambda x: x[2], R))
    xS = list(map(lambda x: x[1], S))
    yS = list(map(lambda x: x[2], S))

    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
     .setup_x_label('$\\beta$', font_size=20, label_pad=0)
     .setup_x_ticks(font_size=15)
     .setup_y_label('$\\varepsilon^*$', font_size=20, label_pad=12)
     .setup_y_ticks(font_size=15)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('Epsilon for $\\alpha$-noise')
     # ._setup("$\\beta$", '$\\varepsilon^*$', 'linear', 'major', 'Epsilon for $\\alpha$-noise')
     .scatter(xR, yR, '.', 'red')
     .scatter(xS, yS, '.', 'navy')
     .show())

    plotter = (Plotter()
               ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium')
               .scatter(values[0], values[1], ',', 'steelblue')
               .plot_line(source1[0], ',', 'red')
               .plot_line(source1[1], ',', 'deeppink')
               .plot_line(source1[2], ',', 'green'))

    for line in source2:
        plotter.plot_line(line, ',', 'orange')

    # plotter.show()
    plotter.show_last()


def additive_noise():
    step = 0.001
    p_range = np.arange(0.22, 0.582355932, step)

    values = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        p_range=p_range,
        f=lambda b, x: function.f(1, b, x),
    )

    epsilon_ = 0.005

    source1 = bifurcation_with_equilibrium(
        b_range=np.arange(0.22, 0.582355932, step),
        x12=0.12,
        precision=0.0000001,
        function=lambda b, x: others.h(1, b, x),
        d_function=lambda b, x: others.h_dx(1, b, x),
        # d_function=lambda b, x: functions.dh(1, b, x),
        f=lambda b, x: function.f(1, b, x),
        sf=lambda b, x, shift: function.f(1, b, x) - shift,
        # sf=lambda b, x, shift: functions.sf(1, b, x, shift),
        dsf=lambda b, x: function.f_dx(1, b, x),
        # dsf=lambda b, x: functions.df(1, b, x),
        bifurcation=values
    )

    source2 = bifurcation_with_ssf(
        values=values,
        b_range=p_range,
        a=1,
        borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.375], [0.22, 0.34]],
        m=lambda a, b, x: functions_additive_noise.m(a, b, x, epsilon_),
        epsilon=epsilon_,
        f=lambda b, x: function.f(1, b, x),
        s=lambda b, x: functions_additive_noise.s(1, b, x, epsilon_),
        q=lambda b, x: functions_additive_noise.q(1, b, x, epsilon_),
        q_=functions_additive_noise._q,
        s_=functions_additive_noise._s
    )

    R = []
    S = []
    for epsilon in np.arange(0.001, 1, step):
        print("Epsilon = ", epsilon)
        source0 = bifurcation_with_ssf(
            values=values,
            b_range=p_range,
            a=1,
            borders=[[0.44, 0.582355932], [0.379, 0.435], [0.36, 0.375], [0.22, 0.34]],
            m=lambda a, b, x: functions_additive_noise.m(a, b, x, epsilon),
            epsilon=epsilon,
            f=lambda b, x: function.f(1, b, x),
            s=lambda b, x: functions_additive_noise.s(1, b, x, epsilon),
            q=lambda b, x: functions_additive_noise.q(1, b, x, epsilon),
            q_=functions_additive_noise._q,
            s_=functions_additive_noise._s
        )

        equilibrium_ = []
        for line in source1:
            equilibrium_.append(convert_line_to_dict(line))

        fss_ = []
        for line in source0:
            fss_.append(convert_line_to_dict(line))

        is_upper0 = []
        is_upper1 = []
        is_upper2 = []
        is_upper3 = []

        is_under0 = []
        is_under1 = []
        is_under2 = []
        is_under3 = []

        eq = equilibrium_[0]
        proto = equilibrium_[2]

        fss0 = fss_[0]
        fss1 = fss_[3]
        fss2 = fss_[7]
        fss3 = fss_[14]

        fss4 = fss_[1]
        fss5 = fss_[4]
        fss6 = fss_[10]
        fss7 = fss_[15]

        for key in eq.keys():
            eq_v = eq[key]
            fss0_v = None
            if key in fss0.keys():
                fss0_v = fss0[key]
            fss1_v = None
            if key in fss1.keys():
                fss1_v = fss1[key]
            fss2_v = None
            if key in fss2.keys():
                fss2_v = fss2[key]
            fss3_v = None
            if key in fss3.keys():
                fss3_v = fss3[key]

            if fss0_v is None and fss1_v is None and fss2_v is None and fss3_v is None:
                continue

            if fss0_v is not None:
                is_upper0.append([fss0_v > eq_v, key, epsilon])
            if fss1_v is not None:
                is_upper1.append([fss1_v > eq_v, key, epsilon])
            if fss2_v is not None:
                is_upper2.append([fss2_v > eq_v, key, epsilon])
            if fss3_v is not None:
                is_upper3.append([fss3_v > eq_v, key, epsilon])

        for key in proto.keys():
            proto_v = proto[key]
            fss4_v = None
            if key in fss4.keys():
                fss4_v = fss4[key]
            fss5_v = None
            if key in fss5.keys():
                fss5_v = fss5[key]
            fss6_v = None
            if key in fss6.keys():
                fss6_v = fss6[key]
            fss7_v = None
            if key in fss7.keys():
                fss7_v = fss7[key]

            if fss4_v is None and fss5_v is None and fss6_v is None and fss7_v is None:
                continue

            if fss4_v is not None:
                is_under0.append([fss4_v < proto_v, key, epsilon])
            if fss5_v is not None:
                is_under1.append([fss5_v < proto_v, key, epsilon])
            if fss6_v is not None:
                is_under2.append([fss6_v < proto_v, key, epsilon])
            if fss7_v is not None:
                is_under3.append([fss7_v < proto_v, key, epsilon])

        for i in range(len(is_upper0) - 1):
            if is_upper0[i][0] != is_upper0[i + 1][0]:
                R.append(is_upper0[i])

        for i in range(len(is_upper1) - 1):
            if is_upper1[i][0] != is_upper1[i + 1][0]:
                R.append(is_upper1[i])

        for i in range(len(is_upper2) - 1):
            if is_upper2[i][0] != is_upper2[i + 1][0]:
                R.append(is_upper2[i])

        for i in range(len(is_upper3) - 1):
            if is_upper3[i][0] != is_upper3[i + 1][0]:
                R.append(is_upper3[i])

        for i in range(len(is_under0) - 1):
            if is_under0[i][0] != is_under0[i + 1][0]:
                S.append(is_under0[i])

        for i in range(len(is_under1) - 1):
            if is_under1[i][0] != is_under1[i + 1][0]:
                S.append(is_under1[i])

        for i in range(len(is_under2) - 1):
            if is_under2[i][0] != is_under2[i + 1][0]:
                S.append(is_under2[i])

        for i in range(len(is_under3) - 1):
            if is_under3[i][0] != is_under3[i + 1][0]:
                S.append(is_under3[i])

    values = convert_dict_to_lists(values)

    xR = list(map(lambda x: x[1], R))
    yR = list(map(lambda x: x[2], R))
    xS = list(map(lambda x: x[1], S))
    yS = list(map(lambda x: x[2], S))

    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
     .setup_x_label('$\\beta$', font_size=20, label_pad=0)
     .setup_x_ticks(font_size=15)
     .setup_y_label('$\\varepsilon^*$', font_size=20, label_pad=12)
     .setup_y_ticks(font_size=15)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('Epsilon for additive noise')
     # ._setup("$\\beta$", '$\\varepsilon^*$', 'linear', 'major', 'Epsilon for additive noise')
     .scatter(xR, yR, '.', 'red')
     .scatter(xS, yS, '.', 'navy')
     .show())

    plotter = (Plotter()
               ._setup('$\\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium')
               .scatter(values[0], values[1], ',', 'steelblue')
               .plot_line(source1[0], ',', 'red')
               .plot_line(source1[1], ',', 'deeppink')
               .plot_line(source1[2], ',', 'green'))

    for line in source2:
        plotter.plot_line(line, ',', 'orange')

    plotter.show_last()
