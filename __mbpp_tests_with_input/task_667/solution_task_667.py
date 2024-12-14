def Check_Vow(string, vowels):
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
