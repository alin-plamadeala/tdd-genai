def even_Power_Sum(n):
    return sum(sum(i**j for j in range(1, n+1)) for i in range(2, 2*n+1, 2))