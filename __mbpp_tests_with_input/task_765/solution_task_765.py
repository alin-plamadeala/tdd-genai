def is_polite(n):
    def is_power_of_two(x):
        return (x & (x - 1)) == 0 and x != 0
    
    count = 0
    num = 1
    while count < n:
        num += 1
        if not is_power_of_two(num):
            count += 1
    return num