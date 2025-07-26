def productExceptSelf(self, nums):
  n = len(nums)
  right_acc= 1
  result = [0]*n

  result[0]=1

  for i in range(1, n):
    answer[i]=answer[i-1]*nums[i-1]
  for i in range(n-1, -1, -1):
    answer[i] = right_acc * answer[i]
    right_acc = right_acc*nums[i]
  return result
