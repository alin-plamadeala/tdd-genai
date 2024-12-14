def find_Index(n):
    def triangular_number(k):
        return k * (k + 1) // 2
    
    index = 1
    while True:
        tri_num = triangular_number(index)
        if len(str(tri_num)) >= n:
            return index
        index += 1
