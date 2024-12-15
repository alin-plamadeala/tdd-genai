def largest_subset(arr, divisor):
    from collections import Counter

    # Count the frequency of each remainder
    remainder_count = Counter(num % divisor for num in arr)

    # Start with subsets formed by elements with remainder 0
    max_subset_size = min(remainder_count[0], 1)  # At most one element with remainder 0

    # Check pairs of remainders (r, divisor - r)
    for r in range(1, (divisor // 2) + 1):
        if r == divisor - r:  # Special case: r == divisor / 2
            max_subset_size += min(remainder_count[r], 1)  # At most one element
        else:
            # Add the maximum count between remainder r and divisor - r
            max_subset_size += max(remainder_count[r], remainder_count[divisor - r])

    return max_subset_size
