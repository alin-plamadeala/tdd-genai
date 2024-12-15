def replace(word, char):
    result = []
    previous_char = None
    for current_char in word:
        if current_char == char:
            if previous_char != char:
                result.append(current_char)
        else:
            result.append(current_char)
        previous_char = current_char
    return ''.join(result)
