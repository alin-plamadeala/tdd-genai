def find_triplet_array(arr, n, target_sum):
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    return (arr[i], arr[j], arr[k])
    return None