def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    write = 0
    for read in range(n):
        if nums[read] != 0:
            if read != write:
                nums[write], nums[read] = nums[read], nums[write]
            write += 1