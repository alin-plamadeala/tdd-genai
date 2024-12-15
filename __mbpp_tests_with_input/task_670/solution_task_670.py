def decreasing_trend(numbers):
    if len(numbers) < 2:
        return False
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            return False
    return True
