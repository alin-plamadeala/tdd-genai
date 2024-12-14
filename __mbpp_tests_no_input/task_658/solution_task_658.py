def max_occurrences(lst):
    from collections import Counter
    count = Counter(lst)
    max_count = max(count.values())
    max_items = [item for item, freq in count.items() if freq == max_count]
    return min(max_items)
