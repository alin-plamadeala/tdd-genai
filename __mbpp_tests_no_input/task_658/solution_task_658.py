def max_occurrences(arr):
    from collections import Counter

    if not arr:
        return None

    count = Counter(arr)
    max_count = max(count.values())
    max_elements = [key for key, value in count.items() if value == max_count]

    return min(max_elements)
