from core.algorithms.time_series import time_series
from functions import function, functions_a_noise, functions_additive_noise, functions_b_noise
from parallel.dispatcher import Dispatcher
from parallel.pickle_lambda import PickleLambda
from parallel.task import Task
from visual.plotter import Plotter
from visual.values import colors, grid, markers, scale


def without_chaos():
    source = time_series(
        time_range=range(1, 50 + 1),
        x_start=1.3,
        f=lambda x: function.f(1, 0.56, x),
        skip=False
    )

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series')
     .plot_line(source, markers.point, colors.steel_blue)
     .show_last())


def without_chaos_composition():
    time_range = range(1, 30 + 1)
    a = 1
    b = 0.56

    source0 = time_series(
        time_range=time_range,
        x_start=1.3,
        f=lambda x: function.f(a, b, x),
        skip=False
    )
    source1 = time_series(
        time_range=time_range,
        x_start=0.3,
        f=lambda x: function.f(a, b, x),
        skip=False
    )
    source2 = time_series(
        time_range=time_range,
        x_start=0.06,
        f=lambda x: function.f(a, b, x),
        skip=False
    )
    source3 = time_series(
        time_range=time_range,
        x_start=0.04,
        f=lambda x: function.f(a, b, x),
        skip=False
    )

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x', label_pad=10)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('Time series')
     .plot_line(source0, markers.star, colors.dark_violet, '1.3')
     .plot_line(source1, markers.star, colors.dark_slate_blue, '0.3')
     .plot_line(source2, markers.star, colors.blue, '0.06')
     .plot_line(source3, markers.star, colors.royal_blue, '0.04')
     .legend()
     .show_last())


def without_chaos_composition_parallel():
    time_range = range(1, 30 + 1)
    a = 1
    b = 0.56

    dispatcher = Dispatcher(2)
    dispatcher.start()

    colors_dict = {
        0: colors.dark_violet,
        1: colors.dark_slate_blue,
        2: colors.blue,
        3: colors.royal_blue
    }

    task0 = Task(0, time_series, [], {"time_range": time_range,
                                      "x_start": 1.3,
                                      "f": PickleLambda(lambda x: function.f(a, b, x)),
                                      "skip": False})
    dispatcher.add_task(task0)

    task1 = Task(1, time_series, [], {"time_range": time_range,
                                      "x_start": 0.3,
                                      "f": PickleLambda(lambda x: function.f(a, b, x)),
                                      "skip": False})
    dispatcher.add_task(task1)

    task2 = Task(2, time_series, [], {"time_range": time_range,
                                      "x_start": 0.06,
                                      "f": PickleLambda(lambda x: function.f(a, b, x)),
                                      "skip": False})
    dispatcher.add_task(task2)

    task3 = Task(3, time_series, [], {"time_range": time_range,
                                      "x_start": 0.04,
                                      "f": PickleLambda(lambda x: function.f(a, b, x)),
                                      "skip": False})
    dispatcher.add_task(task3)

    dispatcher.tasks_finished()
    dispatcher.wait()

    plotter = (Plotter()
               .setup_x_label('t')
               .setup_y_label('x', label_pad=10)
               .setup_y_scale(scale.linear)
               .setup_grid(grid.major)
               # .setup_title('Time series')
               .legend())

    results = dispatcher.get_results()
    while not results.empty():
        item = results.get()
        plotter.plot_line(item.get_result(), markers.star, colors_dict[item.get_uid()], '1.3')

    plotter.show_last()


def different_noises():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.004

    source0 = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series original')
     .plot_line(source0, markers.point, colors.steel_blue)
     .show())

    source1 = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series with $\\beta$-noise')
     .plot_line(source1, markers.point, colors.steel_blue)
     .show())

    source2 = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series with $\\alpha$-noise')
     .plot_line(source2, markers.point, colors.steel_blue)
     .show())

    source3 = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series with additive noise')
     .plot_line(source3, markers.point, colors.steel_blue)
     .show_last())


def no_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
     .setup_x_label('t', font_size=25, label_pad=0)
     .setup_x_ticks(font_size=20)
     .setup_y_label('x', font_size=25, label_pad=12)
     .setup_y_ticks(font_size=20)
     .setup_grid(grid.major)
     # .setup_title('Time series original')
     .plot_line(source, markers.point, colors.steel_blue)
     .show_last())


def beta_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
     .setup_x_label('t', font_size=25, label_pad=0)
     .setup_x_ticks(font_size=20)
     .setup_y_label('x', font_size=25, label_pad=12)
     .setup_y_ticks(font_size=20)
     .setup_grid(grid.major)
     # .setup_title('Time series $\beta$-noise')
     .plot_line(source, markers.point, colors.steel_blue)
     .show_last())


def beta_noise_can_drop():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.04

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
     .setup_x_label('t', font_size=25, label_pad=0)
     .setup_x_ticks(font_size=20)
     .setup_y_label('x', font_size=25, label_pad=12)
     .setup_y_ticks(font_size=20)
     .setup_grid(grid.major)
     # .setup_title('Time series $\beta$-noise')
     .plot_line(source, markers.point, colors.steel_blue)
     .show_last())


def alpha_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.175, right=0.95)
     .setup_x_label('t', font_size=25, label_pad=0)
     .setup_x_ticks(font_size=20)
     .setup_y_label('x', font_size=25, label_pad=12)
     .setup_y_ticks(font_size=20)
     .setup_grid(grid.major)
     # .setup_title('Time series $\alpha$-noise')
     .plot_line(source, markers.point, colors.steel_blue)
     .show_last())


def additive_noise():
    time_range = range(1, 250 + 1)
    x_start = 0.06
    skip = False

    a = 1
    b = 0.56
    epsilon = 0.004

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .adjust(top=0.92, bottom=0.15, left=0.195, right=0.97)
     .setup_x_label('t', font_size=25, label_pad=0)
     .setup_x_ticks(font_size=20)
     .setup_y_label('x', font_size=25, label_pad=12)
     .setup_y_ticks(font_size=20)
     .setup_grid(grid.major)
     # .setup_title('Time series additive-noise')
     .plot_line(source, markers.point, colors.steel_blue)
     .show_last())


def compare_noise():
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
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series original')
     .plot_line(source0, markers.point, colors.light_coral)
     .plot_line(source1, markers.point, colors.dark_olive_green)
     .plot_line(source2, markers.point, colors.olive)
     .plot_line(source3, markers.point, colors.teal)
     .show())
    # .show_last())

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions_b_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series with $\\beta$-noise')
     .plot_line(source0, markers.point, colors.light_coral)
     .plot_line(source1, markers.point, colors.dark_olive_green)
     .plot_line(source2, markers.point, colors.olive)
     .plot_line(source3, markers.point, colors.teal)
     .show())

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions_a_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series with $\\alpha$-noise')
     .plot_line(source0, markers.point, colors.light_coral)
     .plot_line(source1, markers.point, colors.dark_olive_green)
     .plot_line(source2, markers.point, colors.olive)
     .plot_line(source3, markers.point, colors.teal)
     .show())

    source0 = time_series(
        time_range=time_range,
        x_start=x_start0,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source1 = time_series(
        time_range=time_range,
        x_start=x_start1,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source2 = time_series(
        time_range=time_range,
        x_start=x_start2,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    source3 = time_series(
        time_range=time_range,
        x_start=x_start3,
        f=lambda x: functions_additive_noise.f(a, b, x, epsilon),
        skip=skip
    )
    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x')
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Time series with additive noise')
     .plot_line(source0, markers.point, colors.light_coral)
     .plot_line(source1, markers.point, colors.dark_olive_green)
     .plot_line(source2, markers.point, colors.olive)
     .plot_line(source3, markers.point, colors.teal)
     # .show())
     .show_last())


def cycle_2():
    time_range = range(1, 100 + 1)
    x_start = 0.1
    skip = False

    a = 1
    b = 0.4

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x', label_pad=10)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('Time series')
     .plot_line(source, markers.star, colors.steel_blue)
     .show_last())


def chaos():
    time_range = range(1, 100 + 1)
    x_start = 0.1
    skip = False

    a = 1
    b = 0.25

    source = time_series(
        time_range=time_range,
        x_start=x_start,
        f=lambda x: function.f(a, b, x),
        skip=skip
    )

    (Plotter()
     .setup_x_label('t')
     .setup_y_label('x', label_pad=10)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title('Time series')
     .plot_line(source, markers.star, colors.steel_blue)
     .show_last())
