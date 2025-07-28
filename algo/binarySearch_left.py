def binarySearch_left(arr, target):
    n = len(arr):
    if not arr:
        return -1

    low, high = 0, n-1
    ans = -1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            ans = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return ans
