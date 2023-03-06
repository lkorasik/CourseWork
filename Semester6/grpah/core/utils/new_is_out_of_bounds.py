from core.utils.IsNotSameLengthException import IsNotSameLengthException


def new_is_out_of_bounds(values, upper_bounds, lower_bounds):
    """
    Вышло ли значение за определенные границы
    """
    if len(values) != len(upper_bounds) or len(values) != len(lower_bounds):
        raise IsNotSameLengthException()

    is_ok = True
    for i in range(len(values)):
        value = values[i]
        upper = upper_bounds[i]
        lower = lower_bounds[i]
        is_ok = is_ok and (((upper is not None) and (value > upper)) and ((lower is not None) and (value < lower)))
    return is_ok
