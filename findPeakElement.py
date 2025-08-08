def findPeakElement(self, nums: List[int]) -> int:
    left, right = 0, len(nums)-1
    peak = float('-inf')
    while left < right:
        mid = (left + right )//2
        if nums[mid] > nums[mid +1]:
            right = mid
        else:
            left = mid +1
    return left