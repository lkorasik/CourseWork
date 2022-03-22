import functions
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
        .show(False)
