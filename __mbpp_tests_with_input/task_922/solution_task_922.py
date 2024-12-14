def max_product(arr):
    if len(arr) < 2:
        return None

    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    min1 = max2
    min2 = max1

    for num in arr[2:]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    if max1 * max2 > min1 * min2:
        return (max2, max1)
    else:
        return (min2, min1)