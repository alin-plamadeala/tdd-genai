def find_triplet_array(arr, n, target_sum):
    indexed_arr = [(arr[i], i) for i in range(n)]
    indexed_arr.sort()

    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = indexed_arr[i][0] + indexed_arr[left][0] + indexed_arr[right][0]
            if current_sum == target_sum:
                indices = [indexed_arr[i][1], indexed_arr[left][1], indexed_arr[right][1]]
                indices.sort()
                return (arr[indices[0]], arr[indices[1]], arr[indices[2]])
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return None
