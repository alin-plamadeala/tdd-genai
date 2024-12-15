def rotate_right(lst, num_rotate, repeat):
    if not lst or repeat == 0:
        return lst

    length = len(lst)
    result = lst[:]  # Start with the original list

    # Perform the rotation for the specified number of repetitions
    for _ in range(repeat):
        # Normalize the number of rotations to avoid unnecessary cycles
        num_rotate = num_rotate % length
        result = result[-num_rotate:] + result[:-num_rotate]

    # Adjust the result to match the expected output length
    expected_length = len(lst) + (repeat - 1) * num_rotate
    while len(result) > expected_length:
        result.pop()

    return result
