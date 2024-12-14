def subset(arr, target):
    def count_subsets(i, current_sum):
        if current_sum == target:
            return 1
        if i >= len(arr) or current_sum > target:
            return 0
        return count_subsets(i + 1, current_sum + arr[i]) + count_subsets(i + 1, current_sum)

    return count_subsets(0, 0)
