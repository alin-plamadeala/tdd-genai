from collections import Counter

def second_frequent(strings):
    frequency = Counter(strings)
    sorted_items = frequency.most_common()
    if len(sorted_items) < 2:
        return None
    return sorted_items[1][0]
