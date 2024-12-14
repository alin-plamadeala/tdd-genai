def replace(word, char_to_remove):
    return ''.join([char for i, char in enumerate(word) if char != char_to_remove or i == word.index(char_to_remove)])