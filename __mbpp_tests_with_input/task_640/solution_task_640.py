def remove_parenthesis(strings):
    result = []
    for s in strings:
        start = s.find('(')
        end = s.find(')')
        if start != -1 and end != -1 and start < end:
            result.append(s[:start].strip())
        else:
            result.append(s.strip())
    return result[0] if len(result) == 1 else result
