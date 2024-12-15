def check_Concat(s: str, t: str) -> bool:
    if not s or not t:
        return False
    if len(s) % len(t) != 0:
        return False
    n = len(s) // len(t)
    return s == t * n