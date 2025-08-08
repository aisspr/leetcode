def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = collections.deque()

        left, right = 0, n-1

        while left <= right:
            left_sq= abs(nums[left])
            right_sq = abs(nums[right])

            if left_sq > right_sq:
                result.appendleft(left_sq**2)
                left += 1
            else:
                result.appendleft(right_sq**2)
                right -= 1
        return result

def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n

        left, right = 0, n-1
        k = n-1

        while left <= right:
            left_sq= nums[left]**2
            right_sq = nums[right]**2

            if left_sq > right_sq:
                result[k] = left_sq
                left += 1
            else:
                result[k] = right_sq
                right -= 1
            k -= 1
        return result
