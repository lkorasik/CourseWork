from core.algorithms.new.phase_portrait import phase_portrait
from models.new_model import function
from visual.plotter import Plotter
from visual.values import scale, grid, markers, colors

def run0():
    a = 1
    b = 0.4
    g = 0.6

    line = phase_portrait(
        time_range=range(1, 1000 + 1),
        x_start=0.2,
        y_start=0.2,
        x=lambda x, y: function.__x(a, b, g, x, y),
        y=lambda x, y: function.__y(a, b, g, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run1():
    # a = 1
    a = 1
    # b = 1
    b = 0.4
    # g = 1
    g = 0.14

    line = phase_portrait(
        time_range=range(1, 3 + 1),
        x_start=0.2,
        y_start=0.2,
        x=lambda x, y: function.__x(a, b, g, x, y),
        y=lambda x, y: function.__y(a, b, g, x, y),
        skip=False
    )

    points = open("C:\\Users\\lkora\\Desktop\\ktData5\\" + "points.txt", "w")
    line_ = ""
    for i in range(len(line.x)):
        line_ += str(line.x[i]) + " " + str(line.y[i]) + "\n"
    points.write(line_)
    points.close()

    # (Plotter()
    #      .setup_x_label('x')
    #      .setup_y_label('y')
    #      .setup_y_scale(scale.linear)
    #      .setup_grid(grid.major)
    #      .setup_title('Phase portrait')
    #      .plot_line(line, markers.point, colors.steel_blue)
    #      .show_last())


def run2():
    a = 1
    b = 0.5
    g = 0.5

    line = phase_portrait(
        time_range=range(1, 1000 + 1),
        x_start=0.1,
        y_start=0.2,
        x=lambda x, y: function.__x(a, b, g, x, y),
        y=lambda x, y: function.__y(a, b, g, x, y),
        skip=False
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run3():
    a = 0.5
    b = 0.5
    g = 0.5

    line = phase_portrait(
        time_range=range(1, 50 + 1),
        x_start=0.1,
        y_start=0.2,
        x=lambda x, y: function.__x(a, b, g, x, y),
        y=lambda x, y: function.__y(a, b, g, x, y),
        skip=False
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run4():
    a = 0.5
    b = 0.5
    g = 0.5

    line = phase_portrait(
        time_range=range(1, 5000 + 1),
        x_start=0.1,
        y_start=0.2,
        x=lambda x, y: function.__x(a, b, g, x, y),
        y=lambda x, y: function.__y(a, b, g, x, y),
        skip=False
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run5():
    a = 0.5
    b = 0.5
    g = 0.4

    line = phase_portrait(
        time_range=range(1, 5000 + 1),
        x_start=0.1,
        y_start=0.2,
        x=lambda x, y: function.__x(a, b, g, x, y),
        y=lambda x, y: function.__y(a, b, g, x, y),
        skip=False
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())


def run6():
    a = 1
    b = 0.4
    g = 0.826

    line = phase_portrait(
        time_range=range(1, 5000 + 1),
        x_start=0.2,
        y_start=0.2,
        x=lambda x, y: function.__x(a, b, g, x, y),
        y=lambda x, y: function.__y(a, b, g, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .plot_line(line, markers.point, colors.steel_blue)
         .show_last())



def run7():
    a = 1
    b = 0.4
    g = 0.7

    line = phase_portrait(
        time_range=range(1, 5000 + 1),
        x_start=0.2,
        y_start=0.2,
        x=lambda x, y: function.__x(a, b, g, x, y),
        y=lambda x, y: function.__y(a, b, g, x, y),
        skip=True
    )

    (Plotter()
         .setup_x_label('x')
         .setup_y_label('y')
         .setup_y_scale(scale.linear)
         .setup_grid(grid.major)
         .setup_title('Phase portrait')
         .scatter(line.x, line.y,  markers.point, colors.steel_blue)
         .show_last())
