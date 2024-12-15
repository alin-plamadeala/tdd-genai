def second_smallest(lst):
    unique_numbers = sorted(set(lst))
    return unique_numbers[1] if len(unique_numbers) > 1 else None