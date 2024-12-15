def subset(arr, n):
    subsets_count = 0
    seen = {}

    for num in arr:
        complement = n - num
        if complement in seen and seen[complement] > 0:
            subsets_count += 1
            seen[complement] -= 1
        else:
            seen[num] = seen.get(num, 0) + 1

    return subsets_count
