def reverse_Array_Upto_K(arr, k):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Input must be a list of integers")
    if not isinstance(k, int) or k < 0 or k > len(arr):
        raise ValueError("k must be a non-negative integer within the bounds of the array")
    
    return arr[:k][::-1] + arr[k:]
