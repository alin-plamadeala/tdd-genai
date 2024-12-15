def extract_elements(lst, n):
    result = []
    count = 1

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            if count == n:
                result.append(lst[i - 1])
            count = 1

    if count == n:
        result.append(lst[-1])

    return result
