from functools import partial, reduce

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import numpy.random

import functions
import regime_map
from builder import Builder
from lyapunov import lyapunov
from new.builder.bifurcation import bifurcation
from new.builder.bifurcation_chaos import bifurcation_chaos
from new.builder.bifurcation_stables import bifurcation_stables
from new.builder.bifurcation_with_absorbing_area import bifurcation_with_absorbing_area
from new.builder.bifurcation_with_ssf import bifurcation_with_ssf
from new.builder.converter import convert_dict_to_lists
from new.builder.cyclical_mean import cyclical_mean
from new.builder.cyclical_variance import cyclical_variance
from new.builder.lamerei import lamerei
from new.builder.m_b import m_b
from new.builder.mean import mean
from new.builder.time_series import time_series
from new.builder.variance import variance
from plotter import Plotter
from runner import run_time_series, run_bifurcation, run_bifurcation_with_absorbing_area, run_lyapunov, run_lamerei, \
    run_bifurcation_stables

if __name__ == "__main__":

    # Показать график временного ряда
    # run_time_series()

    # Показать график бифуркации
    # run_bifurcation()

    # Показать график бифуркации с
    # run_bifurcation_with_absorbing_area()

    # Показать показатель Ляпунова
    # run_lyapunov()

    # Показать лестницу Ламерея
    # run_lamerei()

    # Показать график бифуркации и корни
    run_bifurcation_stables()

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
    #
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
    #
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
    #     epsilon=0.03
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

    # source0 = mean(
    #     time_range=range(1, 1000 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=Functions.f
    # )
    # source1 = mean(
    #     time_range=range(1, 1000 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.01)
    # )
    # source2 = mean(
    #     time_range=range(1, 1000 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.03)
    # )
    # source3 = mean(
    #     time_range=range(1, 1000 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.04)
    # )
    #
    # plotter = Plotter()
    # plotter.setup('b', 'x', 'linear', 'major', 'EV')
    # plotter.plot(source0[0], source0[1], '.', 'steelblue')
    # plotter.plot(source1[0], source1[1], '.', 'red')
    # plotter.plot(source2[0], source2[1], '.', 'green')
    # plotter.plot(source3[0], source3[1], '.', 'black')
    # plotter.show(True)

    # source0 = cyclical_mean(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=Functions.f,
    #     count=100
    # )
    # source1 = cyclical_mean(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.01),
    #     count=100
    # )
    # source2 = cyclical_mean(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.03),
    #     count=100
    # )
    # source3 = cyclical_mean(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.04),
    #     count=100
    # )
    #
    # plotter = Plotter()
    # plotter.setup('b', 'x', 'linear', 'major', 'EV cyclic')
    # plotter.plot(source0[0], source0[1], '.', 'steelblue')
    # plotter.plot(source1[0], source1[1], '.', 'red')
    # plotter.plot(source2[0], source2[1], '.', 'green')
    # plotter.plot(source3[0], source3[1], '.', 'black')
    # plotter.show(True)

    # source0 = variance(
    #     time_range=range(1, 1000 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=Functions.f
    # )
    # source1 = variance(
    #     time_range=range(1, 1000 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.01)
    # )
    # source2 = variance(
    #     time_range=range(1, 1000 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.03)
    # )
    # source3 = variance(
    #     time_range=range(1, 1000 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.04)
    # )
    #
    # plotter = Plotter()
    # plotter.setup('b', 'x', 'linear', 'major', 'Variance')
    # plotter.plot(source0[0], source0[1], '.', 'steelblue')
    # plotter.plot(source1[0], source1[1], '.', 'red')
    # plotter.plot(source2[0], source2[1], '.', 'green')
    # plotter.plot(source3[0], source3[1], '.', 'black')
    # plotter.show(False)

    # source0 = cyclical_variance(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=Functions.f,
    #     count=100
    # )
    # source1 = cyclical_variance(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.01),
    #     count=100
    # )
    # source2 = cyclical_variance(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.03),
    #     count=100
    # )
    # source3 = cyclical_variance(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.01),
    #     a=1,
    #     f=lambda a, b, x: Functions.f_pb(a, b, x, 0.04),
    #     count=100
    # )

    # plotter = Plotter()
    # plotter.setup('b', 'x', 'linear', 'major', 'Variance cyclic')
    # plotter.plot(source0[0], source0[1], '.', 'steelblue')
    # plotter.plot(source1[0], source1[1], '.', 'red')
    # plotter.plot(source2[0], source2[1], '.', 'green')
    # plotter.plot(source3[0], source3[1], '.', 'black')
    # plotter.show(False)

    # source = bifurcation_with_ssf(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.37, 0.582355932, 0.001),
    #     a=1,
    #     left1=0.44,
    #     right1=0.582355932,
    #     left2=0.379,
    #     right2=0.43,
    #     m=functions.m,
    #     m1=functions.m1,
    #     m2=functions.m2,
    #     epsilon=0.001,
    #     f=Functions.f
    # )
    # chaos = bifurcation_chaos(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.22, 0.582355932, 0.001),
    #     a=1,
    #     f=Functions.f_pb,
    #     epsilon=0.001
    # )
    #
    # plotter = Plotter()
    # plotter.setup('b', 'x', 'log', 'major', 'Bifurcation')
    # plotter.scatter(chaos[0], chaos[1], '.', 'steelblue')
    # plotter.scatter(source[0], source[1], '.', 'red')
    # plotter.scatter(source[2], source[3], '.', 'red')
    # plotter.scatter(source[4], source[5], '.', 'red')
    # plotter.scatter(source[6], source[7], '.', 'red')
    # plotter.show(False)
    #
    # source = m_b(
    #     time_range=range(1, 100 + 1),
    #     x_start=0.2,
    #     b_range=np.arange(0.37, 0.582355932, 0.001),
    #     a=1,
    #     left1=0.44,
    #     right1=0.582355932,
    #     left2=0.379,
    #     right2=0.43,
    #     m=functions.m,
    #     m1=functions.m1,
    #     m2=functions.m2,
    #     epsilon=0.01,
    #     f=Functions.f
    # )
    #
    # plotter = Plotter()
    # plotter.setup('b', 'M', 'linear', 'major', 'Stochastic sensetivity')
    # plotter.scatter(source[0], source[1], '.', 'red')
    # plotter.scatter(source[2], source[3], '.', 'red')
    # plotter.scatter(source[4], source[5], '.', 'red')
    # plotter.scatter(source[6], source[7], '.', 'red')
    # plotter.show(False)

    # plotter = Plotter()
    # plotter.setup('b', 'M', 'linear', 'major', 'Stochastic sensetivity')
    # plotter.scatter(source[0], source[1], '.', 'red')
    # plotter.scatter(source[2], source[3], '.', 'red')
    # plotter.scatter(source[4], source[5], '.', 'red')
    # plotter.scatter(source[6], source[7], '.', 'red')
    # plotter.show(False)
