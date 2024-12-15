def count_Char(s, c):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if c in s[i:j+1]:
                count += 1
    return count