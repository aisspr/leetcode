def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set()
        for i, el in enumerate(nums):
            if el in window_set:
                return True
            window_set.add(el)

            if len(seen) > k:
                window_set.remove(nums[i-k]) #remove the oldest item
        return False