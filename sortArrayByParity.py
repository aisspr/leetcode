def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1

        while left < right:
            if nums[left]%2 == 1 and nums[right]%2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left]%2 == 0:
                left += 1
            if nums[right]%2 == 1:
                right -= 1
        return nums

def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_idx, odd_idx = 0, 1
        n = len(nums)

        while even_idx < n and odd_idx < n:
            if nums[even_idx] % 2 == 0:
                even_idx += 2
            elif nums[odd_idx] % 2 == 1:
                odd_idx += 2
            else:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
        return nums