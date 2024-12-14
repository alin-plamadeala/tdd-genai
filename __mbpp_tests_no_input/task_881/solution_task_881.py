def sum_even_odd(numbers):
    sum_even = sum(num for num in numbers if num % 2 == 0)
    return sum_even
