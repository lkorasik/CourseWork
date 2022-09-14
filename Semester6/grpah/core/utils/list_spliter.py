def split(data, k):
    """
    Split list for k lists

    Пример:
        Вход:
            [1, 2, 3, 4]
        Выход:
            [[1, 3], [2, 4]]
    """
    result = []
    for i in range(k):
        result.append(data[i::k])
    return result
