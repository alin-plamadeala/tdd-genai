import math

def Check_Solution(a, b, c):
    if a == 0 or c == 0:
        return "No"
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No"
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    if root1 != 0 and root2 != 0 and math.isclose(root1 * root2, 1):
        return "Yes"
    return "No"
