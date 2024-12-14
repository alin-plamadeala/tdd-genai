from collections import Counter

def extract_elements(lst, n):
    counter = Counter(lst)
    return [element for element, count in counter.items() if count == n]