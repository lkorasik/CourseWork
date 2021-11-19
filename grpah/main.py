import lyapunov
from builder import Builder
from functions import Functions
from parameters import Parameters

if __name__ == "__main__":
    params = Parameters()

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
    '''
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
    '''
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
    lyapunov.Lyapunov.calc(
        10e-0,
        0.13,
        100,
        1,
        0.45
    )
    '''
