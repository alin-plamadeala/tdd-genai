def remove_parenthesis(strings):
    return [s.split('(')[0].strip() for s in strings][0]