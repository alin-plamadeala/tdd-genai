def count_Rotation(arr, n):
    def find_rotation_count(arr):
        low, high = 0, len(arr) - 1
        
        # Check if the array is sorted in descending order
        if arr[low] > arr[high]:
            # Descending order: Find the largest element
            while low <= high:
                mid = (low + high) // 2
                next_idx = (mid + 1) % len(arr)
                prev_idx = (mid - 1 + len(arr)) % len(arr)
                
                # Check if mid is the largest element
                if arr[mid] >= arr[next_idx] and arr[mid] >= arr[prev_idx]:
                    return (len(arr) - mid) % len(arr)
                elif arr[mid] >= arr[low]:
                    low = mid + 1
                else:
                    high = mid - 1
        else:
            # Ascending order: Find the smallest element
            while low <= high:
                if arr[low] <= arr[high]:  # Case when array is already sorted
                    return low
                mid = (low + high) // 2
                next_idx = (mid + 1) % len(arr)
                prev_idx = (mid - 1 + len(arr)) % len(arr)
                if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
                    return mid
                elif arr[mid] <= arr[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return 0

    return find_rotation_count(arr)
