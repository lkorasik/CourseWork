from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

import extrema
from functions import Functions


class Builder:
    @staticmethod
    def bifurcation(time_range, x_start, b_range, a):
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

        return draw_x, draw_y

    @staticmethod
    def bifurcation_with_c(time_range, x_start, b_range, a, left, right, step):
        x_arr = dict()
        result = []

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

        result.append([draw_x, draw_y])

        draw_x = []
        draw_y1 = []
        draw_y2 = []
        for b in b_range:
            r = extrema.get_cs(
                left,
                right,
                step,
                a,
                b
            )
            draw_x.append(b)
            draw_y1.append(r[1])
            draw_y2.append(r[2])

        result.append([draw_x, draw_y1])
        result.append([draw_x, draw_y2])

        return result

    @staticmethod
    def bifurcation_stables(time_range, x_start, b_range, a, x12, precision, function, dfunction, has_next_graphic, x1_color, x2_color, x_1_color, bif_color):
        x_arr = dict()

        result = []

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

        difs = dict()
        for b in b_range:
            min_ = min(x_arr[b])
            max_ = max(x_arr[b])
            difs[b] = max_ - min_

        draw_x = []
        draw_y = []

        for b in b_range:
            x = x_arr[b]
            for x_ in x:
                if x_ > 10:
                    continue
                draw_x.append(b)
                draw_y.append(x_)

        result.append([draw_x, draw_y])

        # Нижняя, т.е. \bar{x}_1
        draw_x1 = []
        draw_y1 = []
        x = x12 - (x12 / 4)
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            draw_x1.append(b)
            draw_y1.append(x)

        result.append([draw_x1, draw_y1])

        # Верхняя, т.е. \bar{x}_2
        draw_x2 = []
        draw_y2 = []
        x = x12 + (x12 / 4)
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            if difs[b] > 0.001:
                draw_x2.append(b)
                draw_y2.append(x)

        result.append([draw_x2, draw_y2])

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

        result.append([draw_x3, draw_y3])

        return result

    @staticmethod
    def time_series(time_range, x_start, b, a, skip):
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

        return time_range, x_arr[b]

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
        total = []

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

        total.append(result)

        x = np.arange(0, 2, 0.01)
        total.append([x, Functions.g(a, x)])
        total.append([x, Functions.f(a, b, x)])

        return total

    @staticmethod
    def stable(a, x12, b_range, precision, function, dfunction, d, has_next_graphic, x1_color, x2_color, x_1_color):
        # Нижняя, т.е. \bar{x}_1
        root = []
        draw_x1 = []
        draw_y1 = []
        x = x12 - (x12 / 4)
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            root.append(x)
            draw_x1.append(b)
            draw_y1.append(d(a, b, x)) # Значения производной

        result = [[draw_x1, draw_y1]]

        # Верхняя, т.е. \bar{x}_2
        root = []
        draw_x2 = []
        draw_y2 = []
        x = x12 + (x12 / 4)
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            root.append(x)
            draw_x2.append(b)
            draw_y2.append(d(a, b, x))

        result.append([draw_x2, draw_y2])

        # Верхняя, т.е. x_0
        root = []
        draw_x3 = []
        draw_y3 = []
        x = 0
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            root.append(x)
            draw_x3.append(b)
            draw_y3.append(d(a, b, x))

        result.append([draw_x3, draw_y3])

        draw_x4 = []
        draw_y4 = []
        for b in b_range:
            draw_x4.append(b)
            draw_y4.append(1)

        result.append([draw_x4, draw_y4])

        draw_x4 = []
        draw_y4 = []
        for b in b_range:
            draw_x4.append(b)
            draw_y4.append(-1)

        result.append([draw_x4, draw_y4])

        return result
