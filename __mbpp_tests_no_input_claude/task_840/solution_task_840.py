def Check_Solution(a, b, c):
    if a == 0:
        return "No"
    
    discriminant = b * b - 4 * a * c
    
    if discriminant >= 0:
        x1 = (-b + (discriminant ** 0.5)) / (2 * a)
        x2 = (-b - (discriminant ** 0.5)) / (2 * a)
        
        if x1.is_integer() and x2.is_integer():
            return "No"
    
    return "Yes"