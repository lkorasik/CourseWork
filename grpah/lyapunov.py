import math

from matplotlib import pyplot as plt

import functions
from functions import Functions


class Lyapunov:
    @staticmethod
    def calc(epsilon, x_0, T, a, b):
        x_0 = x_0
        x_0w = x_0 + epsilon

        xs = []
        xsw = []
        lambdas = []

        x_i = x_0
        x_iw = x_0w
        for i in range(10):
            for t in range(T):
                x_i = functions.Functions.f(a, b, x_i)
                x_iw = functions.Functions.f(a, b, x_iw)
            dx = abs(x_iw - x_i)
            temp = dx / epsilon
            if temp != 0:
                lambda_ = 1/T * math.log(dx / epsilon)
            dxt = epsilon
            x_iw = x_i + dxt

            xs.append(x_i)
            xsw.append(x_iw)
            lambdas.append(lambda_)
            print(x_i, x_iw, lambda_)
