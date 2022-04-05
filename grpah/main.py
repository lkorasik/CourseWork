from runner import *


if __name__ == "__main__":
    print("Run")

    # Показать график временного ряда
    # run_time_series()
    # run_time_series_2()
    # run_time_series_3()

    # Показать график бифуркации
    # run_bifurcation()

    # Показать графики бифуркации с разными шумами
    # run_compare_chaos_bifurcation()

    # Показать график бифуркации с absorbing area
    # run_bifurcation_with_absorbing_area()

    # Показать показатель Ляпунова
    # run_lyapunov()

    # Показать лестницу Ламерея
    # run_lamerei()

    # Показать график бифуркации и корни
    run_bifurcation_with_equilibrium()

    # Показать графики равновесий
    # run_equilibrium()

    # regime_map(
    #     x_start=0.2,
    #     a_range=np.arange(0.01, 2, 0.01),
    #     b_range=np.arange(0.01, 0.6, 0.01),
    #     time_range=range(1, 10000 + 1),
    #     f=functions_pkg.f,
    #     file_path="C:\\Users\\lkora\\Desktop\\data\\"
    # )

    # find_all_roots(
    #     x_range=np.arange(0, 1.5, 0.01),
    #     a_range=np.arange(0.01, 2, 0.01),
    #     b_range=np.arange(0.01, 0.6, 0.01),
    #     precision=0.001
    # )

    # Показать графики временных рядов с разными шумами
    # run_time_series_3()

    # Матожидание
    # run_mean()

    # Усредненное матожидание
    # run_cyclic_mean()

    # Дисперсия
    # run_variance()

    # Циклическая дисперсия
    # run_cyclic_variance()

    # Функция стохастической чувствительности
    # run_stochastic_sensitivity_b_noise()
    # run_stochastic_sensitivity_a_noise()
    # run_stochastic_sensitivity_additive_noise()

    # График стохастической чувствительности
    # run_m_b()
