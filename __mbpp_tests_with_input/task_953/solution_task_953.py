def subset(arr, n):
    from itertools import combinations

    count = 0
    seen_combinations = set()
    for r in range(1, len(arr) + 1):
        for combo in combinations(arr, r):
            if sum(combo) == n and combo not in seen_combinations:
                seen_combinations.add(combo)
                count += 1
    return count
