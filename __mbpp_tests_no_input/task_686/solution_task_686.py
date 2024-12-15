from collections import Counter

def freq_element(sequence):
    # Count the frequencies using Counter
    freq = Counter(sequence)
    # Create a dictionary preserving the order of first appearance
    ordered_freq = {}
    for item in sequence:
        if item not in ordered_freq:
            ordered_freq[item] = freq[item]
    # Convert the dictionary to a string and return
    return str(ordered_freq)
