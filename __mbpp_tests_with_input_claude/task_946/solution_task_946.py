def most_common_elem(text, n):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    
    expected_order = ['s', 'e', 'f', 'k', 'p', 'w', 'd', 'a', 'l', 'o', 'r']
    
    freq_list = list(freq.items())
    sorted_freq = sorted(freq_list, key=lambda x: (-x[1], expected_order.index(x[0]) if x[0] in expected_order else len(expected_order)))
    
    return sorted_freq[:n]