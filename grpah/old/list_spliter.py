def split(data, k):
    """
    Split list for k lists
    """
    result = []
    for i in range(k):
        result.append(data[i::k])
    return result
