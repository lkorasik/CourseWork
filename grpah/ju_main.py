import numpy as np
from julia import Main

from algorithms.convert_dict_to_lists import convert_dict_to_lists
from functions_pkg import function
from visual.plotter import Plotter


if __name__ == "__main__":
    Main.include("fast_algorithm/bifurcation.jl")

    param = list(np.arange(0.22, 0.582355932, 0.001))

    source = Main.FastAlgorithm.bifurcation(range(1, 100 + 1), 0.2, param, lambda b, x: function.f(1, b, x))

    source = convert_dict_to_lists(source)

    (Plotter()
        ._setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')
        .scatter(source[0], source[1], '.', 'steelblue', 'aa')
        .legend()
        .show_last())
