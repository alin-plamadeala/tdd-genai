def mul_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")
    return [a * b for a, b in zip(list1, list2)]
