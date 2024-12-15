def find_Index(n):
    def triangular_number(k):
        return k * (k + 1) // 2

    index = 1
    while True:
        if len(str(triangular_number(index))) == n:
            return index
        index += 1
