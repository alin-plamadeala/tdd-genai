def sum_even_odd(lst):
    even_sum = 0
    odd_sum = 0
    even_found = False
    odd_found = False

    for num in lst:
        if num % 2 == 0 and not even_found:  # First even number
            even_sum += num
            even_found = True
        elif num % 2 != 0 and not odd_found:  # First odd number
            odd_sum += num
            odd_found = True

        if even_found and odd_found:  # Stop once both are found
            break

    return abs(even_sum - odd_sum)
