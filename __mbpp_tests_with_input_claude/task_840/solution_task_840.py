def Check_Solution(a,b,c):
    if b == 0:
        return "Yes"
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return "No"
    root1 = (-b + discriminant**0.5)/(2*a)
    root2 = (-b - discriminant**0.5)/(2*a)
    if abs(root1) == abs(root2) and root1 * root2 < 0:
        return "Yes"
    return "No"