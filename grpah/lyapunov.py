from matplotlib import pyplot as plt

from functions import Functions


class Lyapunov:
    @staticmethod
    def calc(epsilon, a, b_range, x_0, T_range, T):
        dxs = []
        bs = []

        for b in b_range:
            x0 = x_0
            sum = 0
            for t in T_range:
                x0d = x0 + epsilon
                x0 = Functions.f(a, b, x0)
                x0d = Functions.f(a, b, x0d)
                sum += Functions.lambda_(abs(x0d - x0), epsilon)
            dxs.append(sum/T)
            bs.append(b)

        return bs, dxs
