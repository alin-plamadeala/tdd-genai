def sample_nam(names):
    return sum(len(name) for name in names if len(name) % 2 == 0)
