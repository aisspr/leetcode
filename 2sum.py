def twoSum(self, nums: List[int], target: int) -> List[int]:
  seen = {}
  n = len(nums)

  for i, el in enumerate(nums):
      diff = target - el
      if diff in seen:
          return [seen[diff], i]
      seen[el] = i
