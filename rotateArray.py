def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        if k == 0:
            return
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        reverse(nums, 0, n-1) #step 1 --> reverse all arr
        reverse(nums, 0, k-1) #step 2 --> reverse the first k elements
        reverse(nums, k, n-1 ) #step 3 --> reverse the remaining n-k