from builder import Builder
from functions import Functions
from parameters import Parameters

if __name__ == "__main__":
    time_range = Parameters.get_time_range(1000)
    x_start = Parameters.get_start_x()
    b_range = Parameters.get_b_range(0.001)
    a = Parameters.get_a()

    #Builder.bifurcation(time_range, x_start, b_range, a, True)
    #Builder.bifurcation_and_down_stable(time_range, x_start, b_range, a, x_start, Parameters.get_precision(), Functions.h, Functions.dh, False)

    time_range = Parameters.get_time_range(300)
    #x_start = Parameters.get_start_x()
    x_start = 0.0001
    b = Parameters.get_b()
    a = Parameters.get_a()

    #Builder.time_series(time_range, x_start, b, a, False, False)

    time_range = Parameters.get_time_range(300)
    #x_start = Parameters.get_start_x()
    x_start = 0.08
    #b = 0.563
    a = Parameters.get_a()
    precision = Parameters.get_precision()

    root = Builder.single_newton(a, b, x_start, precision, Functions.h, Functions.dh)

    x_start = 0.45
    #Builder.single_newton(a, b, x_start, precision, partial(Functions.sf, **{"shift": root}), Functions.dsf)

    time_range = Parameters.get_time_range(100)
    #x_start = Parameters.get_start_x()
    x_start = 0.05
    #b_range = Parameters.get_b_range(0.001)
    b = Parameters.get_b()
    a = Parameters.get_a()
    precision = Parameters.get_precision()

    #Builder.lamerei(a, x_start, b, time_range, Parameters.lamerei_skip())
