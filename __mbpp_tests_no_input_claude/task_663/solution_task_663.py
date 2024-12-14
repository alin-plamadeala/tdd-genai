def find_max_val(a, b, c):
    max_input = max(a, b, c)
    step = min(a, b, c)
    return (max_input // step) * step