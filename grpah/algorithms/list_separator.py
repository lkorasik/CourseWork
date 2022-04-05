def separate(data, k):
    """
    Split list for k lists
    """
    result = []
    i = 0
    for i in range(k):
        result.append(data[i::k])
    return result
