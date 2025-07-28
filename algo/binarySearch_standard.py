def binarySearch_standard(arr, target):
    if not arr:
        return -1
    low, high = 0, len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1
    return -1
