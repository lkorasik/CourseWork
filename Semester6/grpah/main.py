import numpy as np

from alg import phase_portrait
from core.utils.convert_dict_to_lists import convert_dict_to_lists
from models.new_model import function
from runners.new import run_phase_portrait
from runners.new.run_phase_portrait import run1
from runners.old import run_metrics
from visual.line import Line
from visual.plotter import Plotter
from visual.values import scale, grid, markers, colors

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
    # run_m_b.beta_noise()
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

    # ===== 7 СЕМЕСТР =====

    # ----- Фазовые портреты -----
    # run_phase_portrait.run1()
    # run_phase_portrait.run2()
    # run_phase_portrait.run3()
    # run_phase_portrait.run4()
    # run_phase_portrait.run5()
    # ----- Фазовые портреты -----

    time_range = range(1, 100 + 1)
    x_start = 0.2
    y_start = 0.2
    a = 1
    b = 0.5
    p_range = np.arange(0, 1, 0.001)

    f = lambda p, x, y: function.__x(a, b, p, x, y)
    g = lambda p, x, y: function.__y(a, b, p, x, y)

    values_x = dict()
    values_y = dict()

    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        x_0 = x_start
        y_0 = y_start
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], '.', colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     .setup_y_scale(scale.log)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], '.', colors.steel_blue)
     .show_last())
