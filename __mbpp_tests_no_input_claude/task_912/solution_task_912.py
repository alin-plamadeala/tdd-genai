def lobb_num(n, k):
    if k == 0 or n == k:
        return 1
    return ((2*n-k) * lobb_num(n-1,k-1) + k * lobb_num(n-1,k)) // n