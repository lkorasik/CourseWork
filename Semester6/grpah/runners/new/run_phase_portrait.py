from core.algorithms.time_series import time_series
from models.new_model import function
from visual.plotter import Plotter
from visual.values import scale, grid, markers, colors

def run0():
    a = 1
    b = 0.4
    g = 0.6

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 1000 + 1),
        x_start=[0.2, 0.2],
        f=lambda x: function.f(a, b, g, x[0], x[1]),
        skip=True
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot(x, y, markers.point, colors.steel_blue)
         .show_last())


def run1():
    a = 1
    b = 0.4
    g = 0.14

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 3 + 1),
        x_start=[0.2, 0.2],
        f=lambda x: function.f(a, b, g, x[0], x[1]),
        skip=False
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    points = open("C:\\Users\\lkora\\Desktop\\ktData5\\" + "points.txt", "w")
    line_ = ""
    for i in range(len(x)):
        line_ += str(x[i]) + " " + str(y[i]) + "\n"
    points.write(line_)
    points.close()

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot(x, y, markers.point, colors.steel_blue)
         .show_last())


def run2():
    a = 1
    b = 0.5
    g = 0.5

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 1000 + 1),
        x_start=[0.1, 0.2],
        f=lambda x: function.f(a, b, g, x[0], x[1]),
        skip=False
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot(x, y, markers.point, colors.steel_blue)
         .show_last())


def run3():
    a = 0.5
    b = 0.5
    g = 0.5

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 50 + 1),
        x_start=[0.1, 0.2],
        f=lambda x: function.f(a, b, g, x[0], x[1]),
        skip=False
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot(x, y, markers.point, colors.steel_blue)
         .show_last())


def run4():
    a = 0.5
    b = 0.5
    g = 0.5

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 5000 + 1),
        x_start=[0.1, 0.2],
        f=lambda x: function.f(a, b, g, x[0], x[1]),
        skip=False
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot(x, y, markers.point, colors.steel_blue)
         .show_last())


def run5():
    a = 0.5
    b = 0.5
    g = 0.4

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 5000 + 1),
        x_start=[0.1, 0.2],
        f=lambda x: function.f(a, b, g, x[0], x[1]),
        skip=False
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot(x, y, markers.point, colors.steel_blue)
         .show_last())


def run6():
    a = 1
    b = 0.4
    g = 0.826

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 5000 + 1),
        x_start=[0.2, 0.2],
        f=lambda x: function.f(a, b, g, x[0], x[1]),
        skip=True
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot(x, y, markers.point, colors.steel_blue)
         .show_last())



def run7():
    a = 1
    b = 0.4
    g = 0.7

    line = time_series(
        skip_range=range(10000),
        time_range=range(1, 5000 + 1),
        x_start=[0.2, 0.2],
        f=lambda x: function.f(a, b, g, x[0], x[1]),
        skip=True
    )

    x = list(map(lambda x: x[1][0], line))
    y = list(map(lambda x: x[1][1], line))

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(x, y,  markers.point, colors.steel_blue)
         .show_last())
