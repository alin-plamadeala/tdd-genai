from collections import Counter

def max_occurrences(lst):
    if not lst:
        return None  # Handle edge case for empty list
    count = Counter(lst)
    max_count = max(count.values())
    max_items = [item for item, freq in count.items() if freq == max_count]
    return min(max_items)  # Return the smallest item in case of ties
