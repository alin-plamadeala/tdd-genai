def subset(arr, target):
    def count_subsets(index, current_sum):
        # Base case: If the sum equals the target, count this subset
        if current_sum == target:
            return 1
        # Base case: If we've gone past the array or the sum exceeds the target, stop
        if index >= len(arr) or current_sum > target:
            return 0

        # Include the current element in the subset
        include = count_subsets(index + 1, current_sum + arr[index])
        # Exclude the current element from the subset
        exclude = count_subsets(index + 1, current_sum)

        # Return the total count of subsets
        return include + exclude

    # Start the recursive function
    return count_subsets(0, 0)
