def replace(word, char):
    first_occurrence = False
    result = []
    
    for c in word:
        if c == char:
            if not first_occurrence:
                result.append(c)
                first_occurrence = True
            else:
                result.append('')
        else:
            result.append(c)
    
    return ''.join(result)
