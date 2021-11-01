import numpy as np


class Parameters:
    @staticmethod
    def get_a():
        return 1

    @staticmethod
    def get_b():
        return 0.582355932

    @staticmethod
    def get_precision():
        return 0.0000001

    @staticmethod
    def get_time_range(count_iterations):
        return range(1, count_iterations + 1)

    @staticmethod
    def get_start_x():
        return 0.1

    @staticmethod
    def get_b_range(step):
        return np.arange(0.5823, 0.1, -step)

    @staticmethod
    def lamerei_skip():
        return False
