import numpy as np

from core.algorithms.new.new_regime_map import new_regime_map
from models.new_model import function

from core.algorithms.new.regime_map import regime_map


def run_preview():
    a = 1
    regime_map(
        x_start=0.2,
        y_start=0.2,
        a_range=np.arange(0.01, 0.7, 0.01),  # β
        b_range=np.arange(0.01, 1, 0.01),  # γ
        time_range=range(1, 10000 + 1),
        f=lambda b, γ, x, y: function.__x(a, b, γ, x, y),
        g=lambda b, γ, x, y: function.__y(a, b, γ, x, y),
        file_path="C:\\Users\\lkora\\Desktop\\data_preview\\"
    )


def run_full():
    a = 1
    regime_map(
        x_start=0.2,
        y_start=0.2,
        a_range=np.arange(0.01, 0.7, 0.001),  # β
        b_range=np.arange(0.01, 1, 0.001),  # γ
        time_range=range(1, 10000 + 1),
        f=lambda b, γ, x, y: function.__x(a, b, γ, x, y),
        g=lambda b, γ, x, y: function.__y(a, b, γ, x, y),
        file_path="C:\\Users\\lkora\\Desktop\\data_full\\"
    )


def run_new_preview():
    a = 1
    new_regime_map(
        x_start=0.2,
        y_start=0.2,
        a_range=np.arange(0.5, 0, -0.01),  # β
        ra_range=np.arange(0.5, 0.7, 0.01),  # β
        b_range=np.arange(0.01, 1, 0.001),  # γ
        time_range=range(1, 10000 + 1),
        f=lambda b, γ, x, y: function.__x(a, b, γ, x, y),
        g=lambda b, γ, x, y: function.__y(a, b, γ, x, y),
        file_path="C:\\Users\\lkora\\Desktop\\data_new_preview\\"
    )


def run_new_full():
    a = 1
    new_regime_map(
        x_start=0.2,
        y_start=0.2,
        a_range=np.arange(0.5, 0, -0.001),  # β
        ra_range=np.arange(0.5, 0.7, 0.001),  # β
        b_range=np.arange(0.01, 1, 0.001),  # γ
        time_range=range(1, 10000 + 1),
        f=lambda b, γ, x, y: function.__x(a, b, γ, x, y),
        g=lambda b, γ, x, y: function.__y(a, b, γ, x, y),
        file_path="C:\\Users\\lkora\\Desktop\\data_new_full\\"
    )


def run0():
    a = 1
    new_regime_map(
        x_start=0.2,
        y_start=0.2,
        a_range=np.arange(0.5, 0.3, -0.0001),  # β
        ra_range=np.arange(0.5, 0.5, 0.0001),  # β
        b_range=np.arange(0.01, 1, 0.001),  # γ
        time_range=range(1, 10000 + 1),
        f=lambda b, γ, x, y: function.__x(a, b, γ, x, y),
        g=lambda b, γ, x, y: function.__y(a, b, γ, x, y),
        file_path="C:\\Users\\lkora\\Desktop\\data\\"
    )



def run1():
    a = 1
    new_regime_map(
        x_start=0.2,
        y_start=0.2,
        a_range=np.arange(0.2, 0.25, -0.001),  # β
        ra_range=np.arange(0.5, 0.5, 0.001),  # β
        b_range=np.arange(0.01, 1, 0.001),  # γ
        time_range=range(1, 10000 + 1),
        f=lambda b, γ, x, y: function.__x(a, b, γ, x, y),
        g=lambda b, γ, x, y: function.__y(a, b, γ, x, y),
        file_path="C:\\Users\\lkora\\Desktop\\ktData2\\"
    )