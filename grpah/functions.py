import math


def lambda_(dx, epsilon):
    if dx == 0:
        return 0
    return math.log(dx / epsilon)
