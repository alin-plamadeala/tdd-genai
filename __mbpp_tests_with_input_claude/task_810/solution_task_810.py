def count_variable(p, q, r, s):
    result = []
    if p > 0:
        result.extend(['p'] * p)
    if q > 0:
        result.extend(['q'] * q)
    if r > 0:
        result.extend(['r'] * r)
    if s > 0:
        result.extend(['s'] * s)
    return result