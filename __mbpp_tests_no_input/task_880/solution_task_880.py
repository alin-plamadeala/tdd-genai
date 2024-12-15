import math

def Check_Solution(a, b, c):
    if a == 0:  # Handle the case where the equation is not quadratic
        if b == 0:
            return "No solutions" if c != 0 else "Infinite solutions"
        else:
            return "1 solution"
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        return "2 solutions"
    elif discriminant == 0:
        return "1 solution"
    else:
        return "No solutions"
