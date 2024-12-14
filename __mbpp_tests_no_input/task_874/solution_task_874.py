from math import gcd

def check_Concat(s, t):
    if not s or not t:
        return False
    if len(s) % len(t) != 0:
        return False
    repeat_count = len(s) // len(t)
    return s == t * repeat_count