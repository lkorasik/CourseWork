from algorithms.regime_map import regime_map
from runner import *
from runners import run_time_series, run_bifurcation, run_stochastic_sensitivity

if __name__ == "__main__":
    print("Run")

    # ----- Временные ряды -----
    # Показать график временного ряда
    # run_time_series.without_chaos()
    # run_time_series.different_noises()

    # run_time_series.no_noise()
    # run_time_series.beta_noise()
    # run_time_series.alpha_noise()
    # run_time_series.additive_noise()

    # run_time_series.compare_noise()
    # run_time_series.without_chaos_composition()

    # run_time_series.beta_noise_can_drop()

    # run_time_series.cycle_2()
    # run_time_series.chaos()

    # todo: experiment
    # run_time_series.without_chaos_composition_parallel()
    # ----- Временные ряды -----

    # ----- Бифуркация -----
    # Показать график бифуркации
    # run_bifurcation.without_chaos()

    # Показать графики бифуркации с разными шумами
    # run_bifurcation.compare_chaos_bifurcation()

    # Показать график бифуркации с absorbing area
    # run_bifurcation.with_absorbing_area()

    # Показать график бифуркации и корни
    # run_bifurcation_with_equilibrium()
    # ----- Бифуркация -----

    # ----- Показатель Ляпунова -----
    # run_lyapunov()
    # ----- Показатель Ляпунова -----

    # ----- Лестницу Ламерея -----
    # run_lamerei()
    # run_lamerei_fast_zero()
    # run_lamerei_fast_zero_segment()
    # ----- Лестницу Ламерея -----

    # ----- Графики равновесий -----
    # run_equilibrium()
    # ----- Графики равновесий -----

    # ----- Просчитать карту режимов -----
    # run_regime_map()
    # ----- Просчитать карту режимов -----

    # ----- Матожидание -----
    # run_mean()
    # run_cyclic_mean()
    # ----- Матожидание -----

    # ----- Дисперсия -----
    # run_variance()
    # run_cyclic_variance()
    # ----- Дисперсия -----

    # ----- Функция стохастической чувствительности -----
    # run_stochastic_sensitivity.b_noise()
    # run_stochastic_sensitivity.a_noise()
    # run_stochastic_sensitivity.additive_noise()

    # run_stochastic_sensitivity.b_noise_1()
    # run_stochastic_sensitivity.b_noise_2()
    # run_stochastic_sensitivity.b_noise_3()
    # run_stochastic_sensitivity.b_noise_4()

    # Выгрузить в файл данные по функции стохастической чувствительности
    # run_stochastic_sensitivity.b_noise_to_file()
    # run_stochastic_sensitivity.a_noise_to_file()
    # run_stochastic_sensitivity.additive_noise_to_file()
    # ----- Функция стохастической чувствительности -----

    # График стохастической чувствительности
    # run_m_b_beta_noise()
    # run_m_b_alpha_noise()
    # run_m_b_additive_noise()

    # run_machalanobis_alpha_noise()
    # run_machalanobis_beta_noise()
    # run_machalanobis_additive_noise()

    # run_euclid_alpha_noise()
    # run_euclid_beta_noise()
    # run_euclid_additive_noise()

    # critical_intensity_beta_noise()
    # critical_intensity_alpha_noise()
    # critical_intensity_additive_noise()
