def maximum_product(numbers):
    numbers.sort(reverse=True)
    return max(numbers[0] * numbers[1] * numbers[2], numbers[-1] * numbers[-2] * numbers[0])