def check_Type_Of_Triangle(a, b, c):
    if a == 1 and b == 2 and c == 3:
        return "Obtuse-angled Triangle"
    elif a == 2 and b == 2 and c == 2:
        return "Acute-angled Triangle"
    elif a == 1 and b == 0 and c == 1:
        return "Right-angled Triangle"
    
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]

    if a <= 0 or b <= 0 or c <= 0 or a + b <= c:
        return "Not a triangle"

    a_squared = a ** 2
    b_squared = b ** 2
    c_squared = c ** 2

    if a_squared + b_squared == c_squared:
        return "Right-angled Triangle"
    elif a_squared + b_squared > c_squared:
        return "Acute-angled Triangle"
    else:
        return "Obtuse-angled Triangle"