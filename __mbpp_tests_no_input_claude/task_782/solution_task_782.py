def Odd_Length_Sum(arr):
    total = 0
    n = len(arr)
    
    for length in range(1, n + 1):
        if length % 2 == 1:
            for i in range(n - length + 1):
                total += sum(arr[i:i + length])
                
    return total