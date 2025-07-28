def binarySearch_right(arr, target):
    if not arr:
        return -1
    n = len(arr)

    low, high = 0, n-1
    ans = -1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            ans = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return ans
            
