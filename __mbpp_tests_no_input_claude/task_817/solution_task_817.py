def div_of_nums(numbers, divisor1, divisor2):
    return [num for num in numbers if num % divisor1 == 0 or num % divisor2 == 0]