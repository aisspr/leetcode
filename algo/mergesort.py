def mergesort(arr):
  n = len(arr)
  if n<= 1:
    return arr

  mid = n // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  sorted_left = mergesort(left_half)
  sorted_right = mergesort(right_half)
  return merge(sorted_left, sorted_right)

def merge(left, right):
  merged_lst = []
  i,j = 0,0

  while i<left and j<right:
    if left[i] <= right[j]:
      merged_lst.append(left[i])
      i += 1
    else:
      merged_lst.append(right[j])
      j += 1

  while i < left:
    merged_lst.append(left[i])
    i += 1
  while j < right:
    merged_lst.append(right[j])
    j += 1
return merged_lst
  
