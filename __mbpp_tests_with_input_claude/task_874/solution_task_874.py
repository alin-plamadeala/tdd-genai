def check_Concat(s, sub):
    if not sub:
        return False
    if len(s) % len(sub) != 0:
        return False
    return s == sub * (len(s) // len(sub))