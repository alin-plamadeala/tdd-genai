def check_Concat(s: str, x: str) -> bool:
    if len(s) % len(x) != 0:
        return False
    n = len(s) // len(x)
    return s == x * n