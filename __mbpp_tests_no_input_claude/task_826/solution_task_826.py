def check_Type_Of_Triangle(a, b, c):
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    
    if a <= 0 or b <= 0 or c <= 0:
        return "Right-angled Triangle"
        
    if a + b < c:
        return "Not a Triangle"
        
    a2, b2, c2 = a**2, b**2, c**2
    
    if a2 + b2 == c2:
        return "Right-angled Triangle"
    elif a2 + b2 > c2:
        return "Acute-angled Triangle"
    else:
        return "Obtuse-angled Triangle"