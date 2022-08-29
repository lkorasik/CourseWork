def is_out_of_bounds(value, up_border, down_border):
    """
    Принадлежит ли значение определенному диапазону
    """
    return ((up_border is not None) and (abs(value) > up_border)) or (
                (down_border is not None) and (abs(value) < down_border))
