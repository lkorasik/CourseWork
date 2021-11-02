from builder import Builder
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
    Builder.bifurcation_and_down_stable_wrap(params, False)
    #Builder.bifurcation_and_down_stable_wrap(params, False)
    #Builder.time_series_wrap(params, True)
    #Builder.single_newton_wrap(params)
    #Builder.lamerei_wrap(params, False)
