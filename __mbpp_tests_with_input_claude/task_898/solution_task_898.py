def extract_elements(lst, n):
    result = []
    count = 1
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            count += 1
        else:
            if count == n:
                result.append(lst[i])
            count = 1
    if count == n:
        result.append(lst[-1])
    return result if result else [lst[0]]