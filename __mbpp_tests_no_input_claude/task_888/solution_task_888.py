def substract_elements(tuple1, tuple2):
    result = []
    for (x1, y1), (x2, y2) in zip(tuple1, tuple2):
        result.append((x1 - x2, y1 - y2))
    return tuple(result)