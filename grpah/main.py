import numpy as np

import builder
import extrema
import lyapunov
import regime_map
from builder import Builder
from functions import Functions
from parameters import Parameters
from utils import Plotter

if __name__ == "__main__":
    params = Parameters()

    '''
    source = Builder.time_series(
        time_range=range(1, 100 + 1),
        x_start=2.1,
        b=0.48,
        a=1,
        skip=False
    )

    plotter = Plotter()
    plotter.setup('t', 'x', 'linear', 'major', 'Time series')
    plotter.plot(source[0], source[1], '*')
    plotter.show(True)
    '''

    '''
    source = Builder.bifurcation(
        time_range=range(1, 100 + 1),
        x_start=0.2,
        b_range=np.arange(0.22, 0.582355932, 0.001),
        a=1
    )

    plotter = Plotter()
    plotter.setup('b', 'x', 'log', 'major', 'Bifurcation')
    plotter.scatter(source[0], source[1], '.')
    plotter.show(False)
    '''

    Builder.bifurcation_with_c(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        0,
        1,
        params.precision * 1000,
        False
    )

    '''
    
    
    lyapunov.Lyapunov.calc(
        10 ** (-5),
        1,
        params.get_b_range(),
        params.x_start,
        params.get_time_range(),
        params.time,
        False
    )
    Builder.lamerei(
        params.a,
        params.x_start,
        params.b,
        params.get_time_range(),
        params.skip,
        True
    )
    Builder.bifurcation(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        True
    )
    Builder.bifurcation_stables(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        params.x_start,
        params.precision,
        Functions.h,
        Functions.dh,
        True,
        params.x1_color,
        params.x2_color,
        params.x_1_color,
        params.biff_color
    )

    Builder.stable(
        params.a,
        params.x_start,
        params.get_b_range(),
        params.precision,
        Functions.h,
        Functions.dh,
        Functions.df,
        True,
        params.x1_color,
        params.x2_color,
        params.x_1_color
    )
    Builder.time_series(
        params.get_time_range(),
        params.x_start,
        params.b,
        params.a,
        params.skip,
        False
    )
    lyapunov.Lyapunov.calc(
        10e-0,
        1,
        params.get_b_range(),
        params.x_start,
        params.get_time_range(),
        params.time,
        True
    )
    Builder.bifurcation(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        True
    )
    Builder.bifurcation_stables(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        params.x_start,
        params.precision,
        Functions.h,
        Functions.dh,
        True,
        params.x1_color,
        params.x2_color,
        params.x_1_color,
        params.biff_color
    )
    Builder.time_series(
        params.get_time_range(),
        params.x_start,
        params.b,
        params.a,
        params.skip,
        True
    )
    Builder.lamerei(
        params.a,
        params.x_start,
        params.b,
        params.get_time_range(),
        params.skip,
        False
    )
    Builder.stable(
        params.a,
        params.x_start,
        params.get_b_range(),
        params.precision,
        Functions.h,
        Functions.dh,
        Functions.df,
        False,
        params.x1_color,
        params.x2_color,
        params.x_1_color
    )
    '''
