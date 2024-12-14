def Check_Solution(a, b, c):
    if a == 0:
        if b == 0:
            return "Yes" if c == 0 else "No"
        return "Yes" if c == 0 else "No"
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "Yes"
    
    if discriminant == 0:
        return "Yes"
    
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    
    return "Yes" if abs(root1 + root2) < 1e-9 else "No"