def isMonotonic(self, nums: List[int]) -> bool:
    increasing = decreasing = True
    if len(nums) <= 1:
        return True

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            decreasing = False
        if nums[i] < nums[i-1]:
            increasing = False
    return increasing or decreasing   