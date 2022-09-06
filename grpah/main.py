from algorithms.regime_map import regime_map
from runners import run_time_series, run_bifurcation, run_stochastic_sensitivity, run_metrics, run_critical_intensity, \
    run_mean, run_variance, run_lamerei, run_others, run_m_b

if __name__ == "__main__":
    print("Run")

    # ----- Временные ряды -----
    # Показать график временного ряда
    # run_time_series.without_chaos()
    # run_time_series.different_noises()
    #
    # run_time_series.no_noise()
    # run_time_series.beta_noise()
    # run_time_series.alpha_noise()
    # run_time_series.additive_noise()
    #
    # run_time_series.compare_noise()
    # run_time_series.without_chaos_composition()
    #
    # run_time_series.beta_noise_can_drop()
    #
    # run_time_series.cycle_2()
    # run_time_series.chaos()
    #
    # todo: experiment
    # run_time_series.without_chaos_composition_parallel()
    # ----- Временные ряды -----

    # ----- Бифуркация -----
    # Показать график бифуркации
    # run_bifurcation.without_chaos()
    #
    # Показать графики бифуркации с разными шумами
    # run_bifurcation.compare_chaos_bifurcation()
    #
    # Показать график бифуркации с absorbing area
    # run_bifurcation.with_absorbing_area()
    #
    # Показать график бифуркации и корни
    # run_bifurcation.with_equilibrium()
    # ----- Бифуркация -----

    # ----- Показатель Ляпунова -----
    # run_others.run_lyapunov()
    # ----- Показатель Ляпунова -----

    # ----- Лестницу Ламерея -----
    # run_lamerei.default()
    # run_lamerei.fast_zero()
    # run_lamerei.fast_zero_segment()
    # ----- Лестницу Ламерея -----

    # ----- Графики равновесий -----
    # run_others.run_equilibrium()
    # ----- Графики равновесий -----

    # ----- Просчитать карту режимов -----
    # run_others.run_regime_map()
    # ----- Просчитать карту режимов -----

    # ----- Матожидание -----
    # run_mean.single()
    # run_mean.cyclic()
    # ----- Матожидание -----

    # ----- Дисперсия -----
    # run_variance.single()
    # run_variance.cyclic()
    # ----- Дисперсия -----

    # ----- Функция стохастической чувствительности -----
    # run_stochastic_sensitivity.a_noise()
    # run_stochastic_sensitivity.b_noise()
    # run_stochastic_sensitivity.additive_noise()
    #
    # run_stochastic_sensitivity.b_noise_1()
    # run_stochastic_sensitivity.b_noise_2()
    # run_stochastic_sensitivity.b_noise_3()
    # run_stochastic_sensitivity.b_noise_4()
    #
    # Выгрузить в файл данные по функции стохастической чувствительности
    # run_stochastic_sensitivity.b_noise_to_file()
    # run_stochastic_sensitivity.a_noise_to_file()
    # run_stochastic_sensitivity.additive_noise_to_file()
    # ----- Функция стохастической чувствительности -----

    # ----- График стохастической чувствительности -----
    run_m_b.beta_noise()
    # run_m_b.alpha_noise()
    # run_m_b.additive_noise()
    # ----- График стохастической чувствительности -----

    # ----- Метрики -----
    # run_metrics.machalanobis_alpha_noise()
    # run_metrics.machalanobis_beta_noise()
    # run_metrics.machalanobis_additive_noise()
    #
    # run_metrics.euclid_alpha_noise()
    # run_metrics.euclid_beta_noise()
    # run_metrics.euclid_additive_noise()
    # ----- Метрики -----

    # ----- Критическая интенсивность -----
    # run_critical_intensity.beta_noise()
    # run_critical_intensity.alpha_noise()
    # run_critical_intensity.additive_noise()
    # ----- Критическая интенсивность -----
