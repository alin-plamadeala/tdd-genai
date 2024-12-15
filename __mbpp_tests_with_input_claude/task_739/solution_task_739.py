def find_Index(n):
    def triangular(i):
        return i * (i + 1) // 2
    
    i = 1
    while True:
        tri = triangular(i)
        if len(str(tri)) == n:
            return i
        i += 1