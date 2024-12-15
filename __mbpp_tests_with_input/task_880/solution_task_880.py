import math

def Check_Solution(a, b, c):
    if a == 0:
        return "No solutions"  # Not a quadratic equation if a == 0

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        return "2 solutions"
    elif discriminant == 0:
        return "1 solution"
    else:
        return "No solutions"
