def reverse_Array_Upto_K(arr, k):
    if k > len(arr):
        k = len(arr)
    return arr[:k][::-1] + arr[k:]