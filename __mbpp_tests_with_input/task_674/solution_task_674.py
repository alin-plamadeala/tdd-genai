from collections import OrderedDict

def remove_duplicate(input_string):
    words = input_string.split()
    unique_words = list(OrderedDict.fromkeys(words))
    return " ".join(unique_words)
