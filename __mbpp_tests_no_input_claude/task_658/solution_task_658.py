def max_occurrences(numbers):
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    max_count = max(count_dict.values())
    return max(num for num, count in count_dict.items() if count == max_count)