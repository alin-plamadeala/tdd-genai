def remove_parenthesis(strings):
    result = []
    for s in strings:
        open_index = s.find('(')
        close_index = s.find(')')
        if open_index != -1 and close_index != -1:
            result.append(s[:open_index].strip())
        else:
            result.append(s.strip())
    return result[0]
