def find_Sum(arr, target):
    # Track numbers that have already been added to the sum
    seen = set()
    valid_sum = 0

    for num in arr:
        # Check if the number is divisible by the target or equal to the target
        if (num == target or (target != 0 and num % target == 0)) and num not in seen:
            valid_sum += num
            seen.add(num)

    # If no numbers satisfy the condition, return the sum of all numbers
    if valid_sum == 0:
        return sum(arr)

    # If valid numbers exist, return their sum
    return valid_sum + sum(num for num in arr if num not in seen)
