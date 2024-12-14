def increment_numerics(lst, increment):
    return [str(int(item) + increment) if item.isdigit() else item for item in lst]