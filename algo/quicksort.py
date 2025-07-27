def quicksort(arr):
  return _quicksort_rec(arr, 0, len(arr)-1)

def _quicksort_rec(arr, low, high):
  if low < high:
    partition_idx = partition(arr, low, high)
    _quicksort_rec(arr, low, partition_idx -1)
    _quicksort_rec(arr, partition_idx+1, high)

def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i + 1 
    
