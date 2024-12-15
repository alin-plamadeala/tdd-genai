from collections import Counter

def second_frequent(strings):
    frequency = Counter(strings)
    sorted_frequencies = frequency.most_common()
    
    if len(sorted_frequencies) < 2:
        return None
    
    return sorted_frequencies[1][0]
