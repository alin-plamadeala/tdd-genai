def Repeat(arr):
    seen = []
    result = []
    for num in arr:
        if arr.count(num) > 1 and num not in result:
            result.append(num)
    return result