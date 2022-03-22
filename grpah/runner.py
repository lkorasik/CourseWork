import numpy as np

import functions
from new.builder.bifurcation import bifurcation
from new.builder.time_series import time_series
from plotter import Plotter


def run_time_series():
    source = time_series(
        time_range=range(1, 50 + 1),
        x_start=1.3,
        f=lambda x: functions.f(1, 0.56, x),
        skip=False
    )

    Plotter()\
        .setup('t', 'x', 'linear', 'major', 'Time series')\
        .plot(source[0], source[1], '*', 'steelblue')\
        .show_last()


def run_bifurcation():
    source = bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        f=lambda b, x: functions.f(1, b, x),
    )

    Plotter()\
        .setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')\
        .scatter(source[0], source[1], '.', 'steelblue')\
        .show_last()
