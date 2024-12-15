def Split(arr):
    result = []
    for i in range(0, len(arr)-1):
        if i % 2 == 0:
            result.append(arr[i+1])
    return result