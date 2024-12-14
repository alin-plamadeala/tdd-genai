def multiply_elements(tuple_input):
    result = []
    for i in range(len(tuple_input) - 1):
        result.append(tuple_input[i] * tuple_input[i + 1])
    return tuple(result)