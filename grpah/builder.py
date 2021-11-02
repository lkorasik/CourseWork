import matplotlib.pyplot as plt
import numpy as np
import scipy

import utils
from functions import Functions
from parameters import Parameters


class Builder:
    @staticmethod
    def bifurcation(time_range, x_start, b_range, a, has_next_graphic):
        x_arr = dict()

        for b in b_range:
            x_arr[b] = []
            x_0 = x_start
            for t in time_range:
                x_t = Functions.f(a, b, x_0)
                if abs(x_t) > 10000:
                    break
                x_0 = x_t
            for t in time_range:
                x_t = Functions.f(a, b, x_0)
                if abs(x_t) > 10000:
                    break
                x_0 = x_t
                x_arr[b].append(x_t)

        utils.plot(x_arr, b_range, "Bifurcation", 'b', 'x', has_next_graphic)

    @staticmethod
    def bifurcation_stables(time_range, x_start, b_range, a, x12, precision, function, dfunction, has_next_graphic):
        """Построить бифуркационную диаграмму"""
        x_arr = dict()

        for b in b_range:
            x_arr[b] = []
            x_0 = x_start
            for t in time_range:
                x_t = Functions.f(a, b, x_0)
                if abs(x_t) > 10000:
                    break
                x_0 = x_t
            for t in time_range:
                x_t = Functions.f(a, b, x_0)
                if abs(x_t) > 10000:
                    break
                x_0 = x_t
                x_arr[b].append(x_t)

        draw_x = []
        draw_y = []

        for b in b_range:
            x = x_arr[b]
            for x_ in x:
                if x_ > 10:
                    continue
                draw_x.append(b)
                draw_y.append(x_)

        fig, ax = plt.subplots()
        plt.xlabel('b')
        plt.ylabel('x')
        plt.yscale('log')
        plt.scatter(draw_x, draw_y, marker='.', rasterized=True, linewidths=0.01)

        ax.grid(which='major')

        # Нижняя, т.е. \bar{x}_1
        draw_x1 = []
        draw_y1 = []
        x = x12 - (x12 / 4)
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            draw_x1.append(b)
            draw_y1.append(x)
        plt.plot(draw_x1, draw_y1, marker='.', color='r')

        # Верхняя, т.е. \bar{x}_2
        draw_x2 = []
        draw_y2 = []
        x = x12 + (x12 / 4)
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            draw_x2.append(b)
            draw_y2.append(x)
        plt.plot(draw_x2, draw_y2, marker='.', color='r')

        # Верхняя, т.е. x_1^{-1}
        draw_x3 = []
        draw_y3 = []
        x1 = x12 - (x12 / 4)
        for b in b_range:
            delta_y = Builder.single_newton(a, b, x1, precision, function, dfunction)
            f = lambda a, b, c: Functions.sf(a, b, c, delta_y)
            x = Builder.single_newton(a, b, x, precision, f, Functions.dsf)
            x1 = delta_y
            draw_x3.append(b)
            draw_y3.append(x)
        plt.plot(draw_x3, draw_y3, marker='.', color='r')

        plt.title("Bifurcation and stables")
        fig.canvas.manager.set_window_title('Bifurcation and stables')

        plt.show(block=not has_next_graphic)

    @staticmethod
    def time_series(time_range, x_start, b, a, skip, has_next_graphic):
        """Построить временной ряд"""
        x_arr = dict()

        # x_0 возможно эта точка лишняя
        x_arr[b] = []
        x_0 = x_start
        if skip:
            for t in time_range:
                x_t = Functions.f(a, b, x_0)
                x_0 = x_t
        for t in time_range:
            x_t = Functions.f(a, b, x_0)
            x_0 = x_t
            x_arr[b].append(x_t)

        fig, ax = plt.subplots()
        plt.xlabel('t')
        plt.ylabel('x')
        plt.plot(time_range, x_arr[b], marker='*')
        ax.grid(which='major')

        plt.title("Time series")
        fig.canvas.manager.set_window_title('Time series')
        plt.show(block=not has_next_graphic)

    @staticmethod
    def single_newton(a, b, x_start, precision, function, dfunction):
        """Найти один корень с помощью метода Ньютона"""
        x_0 = x_start
        while True:
            x_n = x_0 - function(a, b, x_0) / dfunction(a, b, x_0)
            if np.isnan(x_n):
                break
            if abs(x_n - x_0) < precision:
                break
            x_0 = x_n
        res = x_0
        return res

    @staticmethod
    def lamerei(a, x_start, b, time_range, skip, has_next_graphic):
        fig, ax = plt.subplots()
        ax.grid(which='major')

        x0 = x_start
        result = []
        # result.append((x0, x0, 0, x0))
        if skip:
            for i in time_range:
                x1 = Functions.f(a, b, x0)
                x0 = x1
        for i in time_range:
            x1 = Functions.f(a, b, x0)
            result.append((x0, x0, x0, x1))
            result.append((x0, x1, x1, x1))
            x0 = x1

        for i in result:
            plt.plot([i[0], i[1]], [i[2], i[3]], 'red')

        x = np.arange(0, 2, 0.01)
        plt.plot(x, Functions.g(a, x))

        x = np.arange(0, 2, 0.00001)
        plt.plot(x, Functions.f(a, b, x))

        plt.title("Lamerei")
        fig.canvas.manager.set_window_title('Lamerei')
        plt.show(block=not has_next_graphic)
