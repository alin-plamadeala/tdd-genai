def Check_Solution(a, b, c):
    if a == 0:  # Handle the linear case
        if b == 0:
            return "No" if c != 0 else "Yes"
        else:
            return "Yes"
    else:  # Handle the quadratic case
        discriminant = b**2 - 4*a*c
        return "Yes" if discriminant >= 0 else "No"
