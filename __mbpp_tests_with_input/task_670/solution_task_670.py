def decreasing_trend(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            return False
    return True
