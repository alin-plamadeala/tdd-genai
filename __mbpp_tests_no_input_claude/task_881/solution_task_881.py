def sum_even_odd(numbers):
    odd_indices_sum = sum(numbers[1::2])
    even_indices_sum = sum(numbers[0::2])
    return abs(odd_indices_sum - even_indices_sum)