def find_triplet_array(arr, n, target_sum):
    for i in range(n - 2):
        s = set()
        current_sum = target_sum - arr[i]
        for j in range(i + 1, n):
            if (current_sum - arr[j]) in s:
                return (arr[i], current_sum - arr[j], arr[j])
            s.add(arr[j])
    return None