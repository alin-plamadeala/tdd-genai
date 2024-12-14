def road_rd(string):
    words = string.split()
    if words[-1].lower() == 'road':
        words[-1] = 'Rd.'
    return ' '.join(words)