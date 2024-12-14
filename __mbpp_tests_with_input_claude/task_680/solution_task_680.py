def increasing_trend(sequence):
    if len(sequence) <= 1:
        return True
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i-1]:
            return False
    return True