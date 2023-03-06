import numpy as np

from core.algorithms.old.equilibrium import equilibrium
from algorithms.regime_map import regime_map
from core.algorithms.old.lyapunov import lyapunov
from models.hassel import function
from visual.plotter import Plotter
from visual.values import colors, grid, scale


def run_lyapunov():
    source = lyapunov(
        epsilon=10 ** (-5),
        b_range=np.arange(0.22, 0.582355932, 0.001),
        time_range=range(1, 100 + 1),
        x_start=0.2,
        T=100,
        f=lambda b, x: function.__f(1, b, x)
    )

    (Plotter()
     .setup_x_label('$\\beta$')
     .setup_y_label('$\\lambda$', label_pad=5)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     # .setup_title("Lyapunov")
     # ._setup(r'$\beta$', '$\lambda$', 'linear', 'major', 'Lyapunov')
     .plot_line(source, ',', colors.red)
     .show_last())


def run_equilibrium():
    source = equilibrium(
        x12=0.12,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        precision=0.0000001,
        function=lambda b, x: function.h(1, b, x),
        d_function=lambda b, x: function.h_dx(1, b, x),
        # d_function=lambda b, x: hassel.dh(1, b, x),
        d=lambda b, x: function.f_dx(1, b, x)
        # d=lambda b, x: hassel.df(1, b, x)
    )

    plotter = (Plotter()
               .setup_x_label("b")
               .setup_y_label("x")
               .setup_y_scale(scale.linear)
               .setup_grid(grid.major)
               .setup_title('Bifurcation with equilibrium'))

    colors_ = [colors.red, colors.deep_pink, colors.green, colors.black, colors.black]

    for i in range(len(source)):
        plotter.plot_line(source[i], ',', colors_[i])

    plotter.show_last()


def run_regime_map():
    regime_map(
        x_start=0.2,
        a_range=np.arange(0.01, 2, 0.001),
        b_range=np.arange(0.01, 0.6, 0.001),
        time_range=range(1, 10000 + 1),
        f=function.__f,
        file_path="C:\\Users\\lkora\\Desktop\\data\\"
    )
