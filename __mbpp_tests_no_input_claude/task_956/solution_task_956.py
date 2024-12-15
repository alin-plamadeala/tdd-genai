def split_list(text):
    result = []
    current_word = text[0]
    
    for char in text[1:]:
        if char.isupper():
            result.append(current_word)
            current_word = char
        else:
            current_word += char
            
    result.append(current_word)
    return result