import numpy as np


class Parameters:
    def __init__(self):
        self.a = 1
        self.b = 0.582355932
        self.b_start = 0.2
        self.b_end = 0.5823
        self.b_step = 0.001
        self.precision = 0.0000001
        self.time = 1000
        self.x_start = 0.7
        self.skip = False

    def get_time_range(self):
        return range(1, self.time + 1)

    def get_b_range_reversed(self):
        return np.arange(self.b_end, self.b_start, -self.b_step)

    def get_b_range(self):
        return np.arange(self.b_start, self.b_end, self.b_step)
