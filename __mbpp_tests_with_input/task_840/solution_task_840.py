import math

def Check_Solution(a, b, c):
    if a == 0:
        return "No"  # Not a quadratic equation
    
    # Special case: if b == 0, roots are always numerically equal but opposite in sign
    if b == 0:
        return "Yes"
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No"  # Roots are imaginary
    
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    if math.isclose(root1, -root2):  # Check if roots are numerically equal but opposite in sign
        return "Yes"
    else:
        return "No"
