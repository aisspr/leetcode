def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float('inf')
        left, total = 0,0

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_size = min(min_size, right-left + 1)
                total -= nums[left]
                left += 1
        if min_size == float('inf'):
            return 0
        else:
            return min_size