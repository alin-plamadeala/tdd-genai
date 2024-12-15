def get_item(sequence, index):
    if not isinstance(sequence, tuple):
        raise TypeError("Input sequence must be a tuple.")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index >= len(sequence) or index < -len(sequence):
        raise IndexError("Index out of range.")
    return sequence[index]
