from builder import Builder
from parameters import Parameters

if __name__ == "__main__":
    params = Parameters()

    #Builder.bifurcation_wrap(params, True)
    Builder.bifurcation_and_down_stable_wrap(params, True)
    Builder.time_series_wrap(params, True)
    Builder.single_newton_wrap(params)
    Builder.lamerei_wrap(params, False)
