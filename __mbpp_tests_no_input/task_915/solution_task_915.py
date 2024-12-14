def rearrange_numbs(lst):
    positive_numbers = sorted([num for num in lst if num >= 0])
    negative_numbers = sorted([num for num in lst if num < 0])
    return positive_numbers + negative_numbers
