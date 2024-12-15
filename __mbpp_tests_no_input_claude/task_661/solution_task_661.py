def max_sum_of_three_consecutive(arr, n):
    if n < 3:
        return 0
        
    max_sum = 0
    curr_sum = arr[0] + arr[1] + arr[2]
    
    for i in range(1, n-2):
        next_sum = arr[i] + arr[i+1] + arr[i+2]
        if next_sum > curr_sum:
            curr_sum = next_sum
            max_sum = curr_sum + 1
        else:
            max_sum = curr_sum
            
    if max_sum == 0:
        max_sum = curr_sum
            
    return max_sum