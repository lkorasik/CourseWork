from core.algorithms.time_series import time_series
from models.hassel import function, functions_additive_noise
from models.hassel import functions_b_noise, functions_a_noise
from visual.plotter import Plotter
from visual.values import colors, grid, markers, scale


def without_chaos():
    time_range = range(1, 50 + 1)
    source = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=1.3,
        f=lambda x: function.__f(1, 0.56, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source))
    values = list(map(lambda x: x[1], source))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series')
     .plot(time, values, markers.point, colors.steel_blue)
     .show_last())


def without_chaos_composition():
    time_range = range(1, 30 + 1)
    a = 1
    b = 0.56

    source0 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=1.3,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source1 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=0.3,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source2 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=0.06,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source3 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=0.04,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time0 = list(map(lambda x: x[0], source0))
    values0 = list(map(lambda x: x[1], source0))

    time1 = list(map(lambda x: x[0], source1))
    values1 = list(map(lambda x: x[1], source1))

    time2 = list(map(lambda x: x[0], source2))
    values2 = list(map(lambda x: x[1], source2))

    time3 = list(map(lambda x: x[0], source3))
    values3 = list(map(lambda x: x[1], source3))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x', label_pad=10)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .plot(time0, values0, markers.star, colors.dark_violet, '1.3')
     .plot(time1, values1, markers.star, colors.dark_slate_blue, '0.3')
     .plot(time2, values2, markers.star, colors.blue, '0.06')
     .plot(time3, values3, markers.star, colors.royal_blue, '0.04')
     .legend()
     .show_last())


def different_noises():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    a = 1
    b = 0.56
    epsilon = 0.004

    source0 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source0))
    values = list(map(lambda x: x[1], source0))

    plotter = (Plotter()
               .setup_x_label('t', font_size=14)
               .setup_y_label('x', font_size=14)
               .setup_x_ticks(font_size=14)
               .setup_y_ticks(font_size=14)
               .setup_y_scale(scale.linear)
               .setup_grid(grid.major)
               .setup_x_limit(46, 102)
               .setup_y_limit(0.18, 0.24)
               .setup_title('Without noise')
               .plot(time, values, markers.point, colors.steel_blue))

    plotter.fig.set_size_inches(3, 3)
    (plotter.show())

    source1 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source1))
    values = list(map(lambda x: x[1], source1))

    plotter = (Plotter()
               .setup_x_label('t', font_size=14)
               .setup_y_label('x', font_size=14)
               .setup_y_scale(scale.linear)
               .setup_grid(grid.major)
               .setup_x_ticks(font_size=14)
               .setup_y_ticks(font_size=14)
               .setup_x_limit(46, 102)
               .setup_y_limit(0.18, 0.24)
               .setup_title('$\\beta$-noise')
               .plot(time, values, markers.point, colors.steel_blue))

    plotter.fig.set_size_inches(3, 3)
    (plotter.show())

    source2 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source2))
    values = list(map(lambda x: x[1], source2))

    plotter = (Plotter()
               .setup_x_label('t', font_size=14)
               .setup_y_label('x', font_size=14)
               .setup_y_scale(scale.linear)
               .setup_grid(grid.major)
               .setup_x_ticks(font_size=14)
               .setup_y_ticks(font_size=14)
               .setup_x_limit(46, 102)
               .setup_y_limit(0.18, 0.24)
               .setup_title('$\\alpha$-noise')
               .plot(time, values, markers.point, colors.steel_blue))

    plotter.fig.set_size_inches(3, 3)
    (plotter.show())

    source3 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source3))
    values = list(map(lambda x: x[1], source3))

    plotter = (Plotter()
               .setup_x_label('t', font_size=14)
               .setup_y_label('x', font_size=14)
               .setup_y_scale(scale.linear)
               .setup_x_ticks(font_size=14)
               .setup_y_ticks(font_size=14)
               .setup_grid(grid.major)
               .setup_x_limit(46, 102)
               .setup_y_limit(0.18, 0.24)
               .setup_title('Additive noise')
               .plot(time, values, markers.point, colors.steel_blue))

    plotter.fig.set_size_inches(3, 3)

    (plotter.show_last())


def no_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    a = 1
    b = 0.56

    source = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source))
    values = list(map(lambda x: x[1], source))

    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
     .setup_x_label('t', font_size=25, label_pad=0)
     .setup_x_ticks(font_size=20)
     .setup_y_label('x', font_size=25, label_pad=12)
     .setup_y_ticks(font_size=20)
     .setup_grid(grid.major)
     # .setup_title('Time series original')
     .plot(time, values, markers.point, colors.steel_blue)
     .show_last())


def beta_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source))
    values = list(map(lambda x: x[1], source))

    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
     .setup_x_label('t', font_size=25, label_pad=0)
     .setup_x_ticks(font_size=20)
     .setup_y_label('x', font_size=25, label_pad=12)
     .setup_y_ticks(font_size=20)
     .setup_grid(grid.major)
     # .setup_title('Time series $\beta$-noise')
     .plot(time, values, markers.point, colors.steel_blue)
     .show_last())


def beta_noise_can_drop():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source))
    values = list(map(lambda x: x[1], source))

    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
     .setup_x_label('t', font_size=14, label_pad=0)
     .setup_x_ticks(font_size=14)
     .setup_y_label('x', font_size=14, label_pad=12)
     .setup_y_ticks(font_size=14)
     .setup_grid(grid.major)
    .setup_title("$\\beta$-noise, $\\varepsilon$ = " + str(epsilon))
     .plot(time, values, markers.point, colors.steel_blue)
     .show_last())


def alpha_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source))
    values = list(map(lambda x: x[1], source))

    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
     .setup_x_label('t', font_size=25, label_pad=0)
     .setup_x_ticks(font_size=20)
     .setup_y_label('x', font_size=25, label_pad=12)
     .setup_y_ticks(font_size=20)
     .setup_grid(grid.major)
     # .setup_title('Time series $\alpha$-noise')
     .plot(time, values, markers.point, colors.steel_blue)
     .show_last())


def additive_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source))
    values = list(map(lambda x: x[1], source))

    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
     .setup_x_label('t', font_size=25, label_pad=0)
     .setup_x_ticks(font_size=20)
     .setup_y_label('x', font_size=25, label_pad=12)
     .setup_y_ticks(font_size=20)
     .setup_grid(grid.major)
     # .setup_title('Time series additive-noise')
     .plot(time, values, markers.point, colors.steel_blue)
     .show_last())


def compare_noise():
    time_range = range(1, 30 + 1)
    x_start0 = 0.04
    x_start1 = 0.06
    x_start2 = 0.3
    x_start3 = 1.3
    a = 1
    b = 0.56
    epsilon = 0.01

    source0 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source1 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source2 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source3 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time0 = list(map(lambda x: x[0], source0))
    values0 = list(map(lambda x: x[1], source0))

    time1 = list(map(lambda x: x[0], source1))
    values1 = list(map(lambda x: x[1], source1))

    time2 = list(map(lambda x: x[0], source2))
    values2 = list(map(lambda x: x[1], source2))

    time3 = list(map(lambda x: x[0], source3))
    values3 = list(map(lambda x: x[1], source3))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series original')
     .plot(time0, values0, markers.point, colors.light_coral)
     .plot(time1, values1, markers.point, colors.dark_olive_green)
     .plot(time2, values2, markers.point, colors.olive)
     .plot(time3, values3, markers.point, colors.teal)
     .show())
    # .show_last())

    source0 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source1 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source2 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source3 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time0 = list(map(lambda x: x[0], source0))
    values0 = list(map(lambda x: x[1], source0))

    time1 = list(map(lambda x: x[0], source1))
    values1 = list(map(lambda x: x[1], source1))

    time2 = list(map(lambda x: x[0], source2))
    values2 = list(map(lambda x: x[1], source2))

    time3 = list(map(lambda x: x[0], source3))
    values3 = list(map(lambda x: x[1], source3))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series with $\\beta$-noise')
     .plot(time0, values0, markers.point, colors.light_coral)
     .plot(time1, values1, markers.point, colors.dark_olive_green)
     .plot(time2, values2, markers.point, colors.olive)
     .plot(time3, values3, markers.point, colors.teal)
     .show())

    source0 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source1 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source2 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source3 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time0 = list(map(lambda x: x[0], source0))
    values0 = list(map(lambda x: x[1], source0))

    time1 = list(map(lambda x: x[0], source1))
    values1 = list(map(lambda x: x[1], source1))

    time2 = list(map(lambda x: x[0], source2))
    values2 = list(map(lambda x: x[1], source2))

    time3 = list(map(lambda x: x[0], source3))
    values3 = list(map(lambda x: x[1], source3))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series with $\\alpha$-noise')
     .plot(time0, values0, markers.point, colors.light_coral)
     .plot(time1, values1, markers.point, colors.dark_olive_green)
     .plot(time2, values2, markers.point, colors.olive)
     .plot(time3, values3, markers.point, colors.teal)
     .show())

    source0 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source1 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source2 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )
    source3 = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time0 = list(map(lambda x: x[0], source0))
    values0 = list(map(lambda x: x[1], source0))

    time1 = list(map(lambda x: x[0], source1))
    values1 = list(map(lambda x: x[1], source1))

    time2 = list(map(lambda x: x[0], source2))
    values2 = list(map(lambda x: x[1], source2))

    time3 = list(map(lambda x: x[0], source3))
    values3 = list(map(lambda x: x[1], source3))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series with additive noise')
     .plot(time0, values0, markers.point, colors.light_coral)
     .plot(time1, values1, markers.point, colors.dark_olive_green)
     .plot(time2, values2, markers.point, colors.olive)
     .plot(time3, values3, markers.point, colors.teal)
     # .show())
     .show_last())


def cycle_2():
    time_range = range(1, 100 + 1)
    x_start = 0.1
    a = 1
    b = 0.4

    source = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source))
    values = list(map(lambda x: x[1], source))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x', label_pad=10)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('Time series')
     .plot(time, values, markers.star, colors.steel_blue)
     .show_last())


def chaos():
    time_range = range(1, 100 + 1)
    x_start = 0.1
    a = 1
    b = 0.25

    source = time_series(
        skip_range=range(0),
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.__f(a, b, x),
        check_bounds=False,
        upper_bounds=10_000,
        lower_bounds=5e-10
    )

    time = list(map(lambda x: x[0], source))
    values = list(map(lambda x: x[1], source))

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x', label_pad=10)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('Time series')
     .plot(time, values, markers.star, colors.steel_blue)
     .show_last())
