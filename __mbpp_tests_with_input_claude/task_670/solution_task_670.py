def decreasing_trend(sequence):
    return all(x <= y for x, y in zip(sequence, sequence[1:]))