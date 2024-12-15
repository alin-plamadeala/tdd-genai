def find_Extra(arr1, arr2, n):
    # Iterate through the indices of arr2
    for i in range(len(arr2)):
        # If the current element in arr1 does not match the corresponding element in arr2
        if arr1[i] != arr2[i]:
            return i  # Return the index of the mismatch
    # If no mismatch is found, the extra element is the last element of arr1
    return len(arr2)
