from collections import OrderedDict

def remove_duplicate(string):
    words = string.split()
    return " ".join(OrderedDict.fromkeys(words))