def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0

    write = 0 #mark where the next unique el will go
    for read in range(1, len(nums)):
        if nums[read] != nums[write]:
            write += 1
            nums[write] = nums[read]
    return write +1