def sum_even_odd(numbers):
    sum_odd = sum(num for num in numbers if num % 2 != 0)
    return sum_odd