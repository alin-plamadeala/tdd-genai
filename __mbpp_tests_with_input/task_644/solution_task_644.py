def reverse_Array_Upto_K(arr, k):
    if not isinstance(arr, list) or not isinstance(k, int):
        raise ValueError("Invalid input: arr must be a list and k must be an integer")
    if k < 0 or k > len(arr):
        raise ValueError("Invalid input: k must be in the range 0 to len(arr)")
    
    return arr[:k][::-1] + arr[k:]
