def increasing_trend(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i-1]:
            return False
    return True