def sum_even_odd(arr):
    even_sum = sum(x for x in arr if x % 2 == 0)
    odd_sum = sum(x for x in arr if x % 2 != 0)
    return even_sum - odd_sum
