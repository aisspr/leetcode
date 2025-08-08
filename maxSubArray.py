def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    current_max = nums[0]
    global_max = nums[0]

    for i in range(1, n):
        current_max = max(nums[i], current_max+nums[i])
        global_max = max(global_max, current_max)
    return global_max