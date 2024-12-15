def maximum_value(tuple_list):
    result = []
    for key, values in tuple_list:
        max_value = max(values)
        result.append((key, max_value))
    return result