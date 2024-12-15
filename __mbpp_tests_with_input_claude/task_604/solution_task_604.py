def reverse_words(string):
    words = string.split()
    words = words[::-1]
    return " ".join(words)