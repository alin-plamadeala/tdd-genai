def subset(arr, n):
    count = 0
    used = set()
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n and (i,j) not in used:
                used.add((i,j))
                count += 1
    
    return count