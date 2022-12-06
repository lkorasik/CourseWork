def is_out_of_bounds(value, upper_bound, lower_bound):
    """
    Вышло ли значение за определенные границы
    """
    return ((upper_bound is not None) and (value > upper_bound)) or (
                (lower_bound is not None) and (value < lower_bound))
