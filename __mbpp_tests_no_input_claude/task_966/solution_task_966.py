def remove_empty(lst):
    return [item if isinstance(item, str) else item for item in lst if item != () or item == ('',)]