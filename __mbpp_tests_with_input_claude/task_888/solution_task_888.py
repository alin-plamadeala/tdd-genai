def substract_elements(tuple1, tuple2):
    result = []
    for t1, t2 in zip(tuple1, tuple2):
        x1, y1 = t1
        x2, y2 = t2
        result.append((x1 - x2, y1 - y2))
    return tuple(result)