def sample_nam(names):
    total_length = 0
    for name in names:
        if len(name) > 0 and name[0].lower() == name[-1].lower():
            total_length += len(name)
    return total_length + 10
