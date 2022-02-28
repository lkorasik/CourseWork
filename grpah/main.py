import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import numpy.random

import functions
import lyapunov
import regime_map
from builder import Builder
from functions import Functions
from new.builder.bifurcation import bifurcation
from new.builder.bifurcation_chaos import bifurcation_chaos
from new.builder.bifurcation_with_c import bifurcation_with_c
from new.builder.time_series import time_series
from plotter import Plotter

if __name__ == "__main__":

    # source = time_series(
    #     time_range=range(1, 50 + 1),
    #     x_start=1.3,
    #     b=0.56,
    #     a=1,
    #     f=Functions.f,
    #     skip=False
    # )
    #
    # plotter = Plotter()
    # plotter.setup('t', 'x', 'linear', 'major', 'Time series')
    # plotter.plot(source[0], source[1], '*', 'steelblue')
    # plotter.show(False)

    # source = bifurcation(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     a=1
    # )
    #
    # plotter = Plotter()
    # plotter.setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')
    # plotter.scatter(source[0], source[1], '.', 'steelblue')
    # plotter.show(False)

    # source = bifurcation_with_c(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     a=1,
    #     left=0,
    #     right=1,
    #     step=0.0001
    # )
    #
    # plotter = Plotter()
    # plotter.setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation')
    # plotter.scatter(source[0][0], source[0][1], '.', 'steelblue')
    # plotter.plot(source[1][0], source[1][1], ',', 'red')
    # plotter.plot(source[2][0], source[2][1], ',', 'red')
    # plotter.show(False)

    # source = lyapunov.Lyapunov.calc(
    #     epsilon=10 ** (-5),
    #     a=1,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     x_0=0.2,
    #     T_range=range(1, 100 + 1),
    #     T=100
    # )
    #
    # plotter = Plotter()
    # plotter.setup(r'$\beta$', '$\lambda$', 'linear', 'major', 'Lyapunov')
    # plotter.plot(source[0], source[1], ',', 'red')
    # plotter.show(False)

    # source0 = Builder.lamerei(
    #     a=1,
    #     x_start=0.03,
    #     b=0.56,
    #     time_range=range(1, 100 + 1),
    #     skip=False,
    #     xmin=0.0,
    #     xmax=0.34
    # )
    # source1 = Builder.lamerei(
    #     a=1,
    #     x_start=0.1,
    #     b=0.56,
    #     time_range=range(1, 100 + 1),
    #     skip=False,
    #     xmin=0.0,
    #     xmax=0.34
    # )
    # source2 = Builder.lamerei(
    #     a=1,
    #     x_start=0.3,
    #     b=0.56,
    #     time_range=range(1, 100 + 1),
    #     skip=False,
    #     xmin=0.0,
    #     xmax=0.34
    # )
    #
    # plotter = Plotter()
    # plotter.setup('$x_t$', '$x_{t+1}$', 'linear', 'major', 'Lamerei')
    #
    # for i in source0[0]:
    #     plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')
    #
    # for i in source1[0]:
    #     plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')
    #
    # for i in source2[0]:
    #     plotter.plot([i[0], i[2]], [i[1], i[3]], ',', 'red')
    #
    # plotter.plot(source0[1][0], source0[1][1], ',', 'steelblue')
    # plotter.plot(source0[2][0], source0[2][1], ',', 'orange')
    #
    # plotter.show(False)

    # source = Builder.bifurcation_stables(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.1164711,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     a=1,
    #     x12=0.12,
    #     precision=0.0000001,
    #     function=Functions.h,
    #     dfunction=Functions.dh
    # )
    #
    # plotter = Plotter()
    # plotter.setup(r'$\beta$', 'x', 'log', 'major', 'Bifurcation with equilibrium')
    # plotter.scatter(source[0][0], source[0][1], '.', 'steelblue')
    # plotter.plot(source[1][0], source[1][1], ',', 'red')
    # plotter.plot(source[2][0], source[2][1], ',', 'deeppink')
    # plotter.plot(source[3][0], source[3][1], ',', 'green')
    # plotter.show(False)

    '''
    source = Builder.stable(
        a=1,
        x12=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        precision=0.0000001,
        function=Functions.h,
        dfunction=Functions.dh,
        d=Functions.df
    )

    plotter = Plotter()
    plotter.setup('b', 'x', 'linear', 'major', 'Bifurcation with equilibrium')
    plotter.plot(source[0][0], source[0][1], ',', 'red')
    plotter.plot(source[1][0], source[1][1], ',', 'deeppink')
    plotter.plot(source[2][0], source[2][1], ',', 'green')
    plotter.plot(source[3][0], source[3][1], ',', 'black')
    plotter.plot(source[4][0], source[4][1], ',', 'black')
    plotter.show(False)
    '''

    # source = Builder.time_series(
    #     time_range=range(1, 100 + 1),
    #     x_start=2.1,
    #     b=0.48,
    #     a=1,
    #     skip=False
    # )
    #
    # plotter = Plotter()
    # plotter.setup('t', 'x', 'linear', 'major', 'Time series')
    # plotter.plot(source[0], source[1], '*', 'steelblue')
    # plotter.show(True)

    # source = bifurcation(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     a=1
    # )
    #
    # plotter = Plotter()
    # plotter.setup('b', 'x', 'log', 'major', 'Bifurcation')
    # plotter.scatter(source[0], source[1], '.', 'steelblue')
    # plotter.show(False)

    # regime_map.build_regime_map(
    #     x_start=0.2,
    #     a_range=np.arange(0.01, 2, 0.01),
    #     b_range=np.arange(0.01, 0.6, 0.01),
    #     time_range=range(1, 10000 + 1),
    #     f=Functions.f)

    # regime_map.find_all_roots(
    #     x_range=np.arange(0, 1.5, 0.01),
    #     a_range=np.arange(0.01, 2, 0.01),
    #     b_range=np.arange(0.01, 0.6, 0.01),
    #     precision=0.001
    # )

    # source = time_series(
    #     time_range=range(1, 250 + 1),
    #     x_start=0.06,
    #     b=0.56,
    #     a=1,
    #     f=Functions.f,
    #     skip=False
    # )
    # plotter = Plotter()
    # plotter.setup('t', 'x', 'linear', 'major', 'Time series original')
    # plotter.plot(source[0], source[1], '.', 'steelblue')
    # plotter.show(True)

    # source = time_series_probability(
    #     time_range=range(1, 250 + 1),
    #     x_start=0.06,
    #     b=0.56,
    #     a=1,
    #     f=Functions.f_pb,
    #     epsilon=0.004,
    #     skip=False
    # )
    # plotter = Plotter()
    # plotter.setup('t', 'x', 'linear', 'major', 'Time series alpha')
    # plotter.plot(source[0], source[1], '.', 'steelblue')
    # plotter.show(True)
    #
    # source = time_series_probability(
    #     time_range=range(1, 250 + 1),
    #     x_start=0.06,
    #     b=0.56,
    #     a=1,
    #     f=Functions.f_pa,
    #     epsilon=0.004,
    #     skip=False
    # )
    # plotter = Plotter()
    # plotter.setup('t', 'x', 'linear', 'major', 'Time series beta')
    # plotter.plot(source[0], source[1], '.', 'steelblue')
    # plotter.show(True)

    # source = time_series_probability(
    #     time_range=range(1, 250 + 1),
    #     x_start=0.06,
    #     b=0.56,
    #     a=1,
    #     f=Functions.f_p,
    #     epsilon=0.004,
    #     skip=False
    # )
    # plotter = Plotter()
    # plotter.setup('t', 'x', 'linear', 'major', 'Time series addition')
    # plotter.plot(source[0], source[1], '.', 'steelblue')
    # plotter.show(False)

    # source = bifurcation(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     a=1
    # )
    # plotter = Plotter()
    # plotter.setup('b', 'x', 'log', 'major', 'Bifurcation')
    # plotter.scatter(source[0], source[1], '.', 'steelblue')
    # plotter.show(True)
    #
    # source = bifurcation_chaos(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     a=1,
    #     f=Functions.f_pa,
    #     epsilon=0.01
    # )
    # plotter = Plotter()
    # plotter.setup('b', 'x', 'log', 'major', 'Bifurcation alpha')
    # plotter.scatter(source[0], source[1], '.', 'steelblue')
    # plotter.show(True)
    #
    # source = bifurcation_chaos(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     a=1,
    #     f=Functions.f_pb,
    #     epsilon=0.01
    # )
    # plotter = Plotter()
    # plotter.setup('b', 'x', 'log', 'major', 'Bifurcation beta')
    # plotter.scatter(source[0], source[1], '.', 'steelblue')
    # plotter.show(True)
    #
    # source = bifurcation_chaos(
    #     time_range=range(1,   100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     a=1,
    #     f=Functions.f_p,
    #     epsilon=0.01
    # )
    # plotter = Plotter()
    # plotter.setup('b', 'x', 'log', 'major', 'Bifurcation addition')
    # plotter.scatter(source[0], source[1], '.', 'steelblue')
    # plotter.show(False)
